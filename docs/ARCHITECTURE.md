# Banana Brush CLI Architecture

A technical deep-dive into the architecture and design decisions of Banana Brush CLI. This document explains the "why" behind the code structure.

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Data Flow](#data-flow)
3. [Component Architecture](#component-architecture)
4. [API Integration](#api-integration)
5. [File Formats](#file-formats)
6. [Design Decisions](#design-decisions)
7. [Extension Points](#extension-points)
8. [Performance Considerations](#performance-considerations)
9. [Security Considerations](#security-considerations)

---

## System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                           User's Computer                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌─────────────────┐    ┌──────────────────┐    │
│  │   Terminal   │───▶│    main.py      │───▶│  Output Files    │    │
│  │   (CLI)      │    │  (Application)  │    │  (.png, .jpg)    │    │
│  └──────────────┘    └────────┬────────┘    └──────────────────┘    │
│                               │                                      │
│                               │ HTTP/HTTPS                          │
│                               ▼                                      │
│                      ┌─────────────────┐                            │
│                      │  Style Files    │                            │
│                      │  (.md)          │                            │
│                      └─────────────────┘                            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ Internet
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        Google Cloud                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    Gemini API                                │    │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐    │    │
│  │  │ Authentication│  │  AI Model     │  │ Image Output  │    │    │
│  │  │ (API Key)     │──▶│ Processing    │──▶│ Generation   │    │    │
│  │  └───────────────┘  └───────────────┘  └───────────────┘    │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Interface** | argparse | Command-line argument parsing |
| **Application** | Python 3.10+ | Core business logic |
| **Image Processing** | Pillow (PIL) | Image I/O operations |
| **API Client** | google-genai | Gemini API communication |
| **Package Management** | UV | Dependency management |
| **Configuration** | pyproject.toml | Project metadata |

---

## Data Flow

### Standard Generation Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │     │  Argument   │     │   Prompt    │     │    API      │
│   Input     │────▶│   Parser    │────▶│  Builder    │────▶│   Client    │
└─────────────┘     └─────────────┘     └─────────────┘     └──────┬──────┘
                                                                    │
                                                                    ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Output    │     │   Image     │     │  Response   │     │   Google    │
│   File      │◀────│   Saver     │◀────│  Parser     │◀────│   Gemini    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### Detailed Step-by-Step Flow

1. **User Input**
   - User types command in terminal
   - Example: `uv run python main.py out.png "A cube" --style styles/blue.md`

2. **Argument Parsing**
   - `argparse` validates and parses command-line arguments
   - Extracts: output path, prompts list, optional flags

3. **Resource Loading**
   - If `--style`: Read markdown file contents
   - If `--edit`: Load input image with PIL
   - If `--ref`: Load reference image with PIL

4. **Prompt Construction**
   - Combine style content (if any) with user prompt
   - Add context for edit/reference modes

5. **API Request**
   - Create `GenerateContentConfig` with settings
   - Send request to Gemini API
   - Contents include: images (if any) + text prompt

6. **Response Processing**
   - Parse API response
   - Extract image data from `inline_data`
   - Convert to PIL Image object

7. **Output**
   - Save image to specified path
   - Print confirmation message

### Edit Mode Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Original   │     │   Edit      │     │   Modified  │
│   Image     │────▶│  Prompt     │────▶│   Image     │
└─────────────┘     └──────┬──────┘     └─────────────┘
                          │
                          │
                    ┌─────▼─────┐
                    │   Gemini   │
                    │    API     │
                    └───────────┘
```

The original image and edit instructions are sent together. The API interprets the edit request and modifies the image accordingly.

### Batch Generation Flow

```
                    ┌──────────────────────────────────────┐
                    │        Multiple Prompts              │
                    │   ["cube", "sphere", "pyramid"]      │
                    └──────────────────┬───────────────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
              ▼                        ▼                        ▼
       ┌─────────────┐          ┌─────────────┐          ┌─────────────┐
       │  Generate   │          │  Generate   │          │  Generate   │
       │  "cube"     │          │  "sphere"   │          │  "pyramid"  │
       └──────┬──────┘          └──────┬──────┘          └──────┬──────┘
              │                        │                        │
              ▼                        ▼                        ▼
       ┌─────────────┐          ┌─────────────┐          ┌─────────────┐
       │ output_1.png│          │ output_2.png│          │ output_3.png│
       └─────────────┘          └─────────────┘          └─────────────┘
```

Prompts are processed sequentially (not in parallel) to:
- Maintain predictable ordering
- Avoid API rate limiting
- Provide clear progress feedback

---

## Component Architecture

### Function Responsibility Map

```
main.py
│
├── get_client()
│   └── Responsibility: API authentication
│       - Reads GOOGLE_API_KEY from environment
│       - Creates and configures genai.Client
│       - Error handling for missing key
│
├── load_style()
│   └── Responsibility: Style file I/O
│       - Validates file existence
│       - Reads file content as UTF-8
│       - Returns clean string content
│
├── load_image()
│   └── Responsibility: Image file I/O
│       - Validates file existence
│       - Loads image using PIL
│       - Returns PIL.Image object
│
├── build_prompt()
│   └── Responsibility: Prompt construction
│       - Combines style + user prompt
│       - Handles None style gracefully
│       - Returns formatted prompt string
│
├── generate_image()
│   └── Responsibility: Core generation logic
│       - Constructs API request
│       - Handles edit/reference modes
│       - Makes API call
│       - Parses response
│       - Returns PIL.Image or None
│
├── get_output_path()
│   └── Responsibility: Output file naming
│       - Handles single vs batch naming
│       - Preserves file extension
│       - Returns appropriate path string
│
└── main()
    └── Responsibility: Application orchestration
        - Argument parsing
        - Workflow coordination
        - User feedback (print statements)
        - Error handling
```

### Dependency Graph

```
main()
  │
  ├── argparse (stdlib)
  │
  ├── get_client()
  │     └── google.genai
  │
  ├── load_style()
  │     └── pathlib (stdlib)
  │
  ├── load_image()
  │     ├── pathlib (stdlib)
  │     └── PIL.Image
  │
  ├── build_prompt()
  │     └── (no dependencies)
  │
  ├── generate_image()
  │     ├── google.genai
  │     ├── google.genai.types
  │     └── PIL.Image
  │
  └── get_output_path()
        └── pathlib (stdlib)
```

---

## API Integration

### Gemini API Request Structure

```python
# Request Configuration
config = types.GenerateContentConfig(
    response_modalities=["TEXT", "IMAGE"],  # What we want back
    image_config=types.ImageConfig(
        aspect_ratio="16:9"  # Desired dimensions
    ),
)

# Request Payload
contents = [
    PIL.Image,  # Optional: input image for edit/reference
    str,        # Text prompt
]

# API Call
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-native-audio-dialog",
    contents=contents,
    config=config,
)
```

### Response Structure

```python
# Response object
response.parts = [
    Part(text="Description of generated image"),  # Optional
    Part(inline_data=ImageData(...)),             # The generated image
]

# Extracting the image
for part in response.parts:
    if part.inline_data is not None:
        pil_image = part.as_image()  # Converts to PIL.Image
```

### Available Models

| Model ID | Characteristics |
|----------|-----------------|
| `gemini-2.5-flash-preview-native-audio-dialog` | Fast, cost-effective |
| `gemini-2.0-flash-exp` | Experimental features |
| `gemini-2.5-flash-image` | Image-focused |
| `gemini-3-pro-image-preview` | Higher quality, 1K/2K/4K |

### Rate Limiting

The Google API has rate limits:
- Requests per minute: ~60 (varies by plan)
- Tokens per minute: varies
- Images per day: varies by quota

Current implementation handles this by:
- Sequential processing (not parallel)
- Natural pacing between requests
- Error messages on failures

---

## File Formats

### Style Files (.md)

**Format**: Plain Markdown text

**Structure** (recommended but flexible):
```markdown
# Style Name

Brief description of the overall aesthetic.

## Category 1 (e.g., Visual Style)
- Bullet point details
- More details

## Category 2 (e.g., Composition)
- Details about layout
- Positioning guidance
```

**How it's used**:
1. Entire file is read as a string
2. String is prepended to user prompt
3. AI interprets as natural language instructions

**Why Markdown?**
- Human-readable and editable
- Familiar format for documentation
- Headers/bullets aid organization (for humans)
- AI treats it as plain text regardless

### Input Images

**Supported formats**: PNG, JPEG, WebP, GIF (first frame)

**Requirements**:
- Valid image file
- Readable by PIL
- Reasonable size (very large images may cause issues)

**Processing**:
- Loaded via `PIL.Image.open()`
- Passed directly to API (library handles encoding)

### Output Images

**Default format**: PNG (preserves transparency)

**Naming convention**:
- Single prompt: Uses exact filename provided
- Multiple prompts: `basename_N.extension`
  - Example: `icon.png` → `icon_1.png`, `icon_2.png`, `icon_3.png`

---

## Design Decisions

### Why Single-File Architecture?

**Decision**: All code in `main.py` (~150 lines)

**Rationale**:
- Simple projects benefit from simplicity
- Easy to understand entire codebase at once
- No import complexity
- Suitable for the scope (CLI tool, not a framework)

**When to split**:
- If adding significant new features
- If code exceeds ~500 lines
- If distinct concerns emerge (e.g., web interface)

### Why Sequential Processing for Batches?

**Decision**: Process prompts one at a time, not in parallel

**Rationale**:
- Predictable output numbering
- Avoids API rate limit issues
- Clearer progress feedback
- Simpler error handling
- Sufficient for typical use cases

**Trade-off**: Slower for large batches

### Why Markdown for Styles?

**Decision**: Plain markdown files, not JSON/YAML config

**Rationale**:
- Natural language is the AI's native format
- No parsing/validation needed
- Human-friendly to write and edit
- Flexible structure (no schema to follow)
- Easy to understand what will be sent

**Alternative considered**: JSON with structured fields
**Why rejected**: Added complexity without benefit

### Why UV over pip?

**Decision**: Use UV as package manager

**Rationale**:
- 10-100x faster than pip
- Automatic virtual environment management
- Better dependency resolution
- Modern, actively developed
- Simple `uv run` syntax

### Why Exit on Errors?

**Decision**: `sys.exit(1)` on errors rather than exceptions

**Rationale**:
- CLI tools should have clear exit codes
- 0 = success, non-zero = failure
- Enables scripting (check `$?` in bash)
- Simpler than exception hierarchies for this scope

---

## Extension Points

### Adding New Argument Types

```python
# In main(), after existing arguments:
parser.add_argument(
    "--new-option",
    type=int,           # or str, float, bool
    default=100,        # default value
    choices=[50, 100, 200],  # optional: restrict choices
    help="Description of this option",
)

# Access it:
args.new_option  # Note: dashes become underscores
```

### Adding New Generation Modes

```python
def generate_image(..., new_mode: bool = False):
    contents = []

    if new_mode:
        # Custom logic for new mode
        prompt = f"Special instruction: {prompt}"

    # ... rest of function
```

### Adding Post-Processing

```python
def post_process(image: Image.Image) -> Image.Image:
    """Apply post-processing to generated image."""
    # Example: Add watermark, resize, filter, etc.
    return image

# In main(), after generation:
if image:
    image = post_process(image)
    image.save(output_path)
```

### Adding Output Formats

```python
def save_image(image: Image.Image, path: str, format_options: dict):
    """Save image with format-specific options."""
    suffix = Path(path).suffix.lower()

    if suffix in ['.jpg', '.jpeg']:
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image.save(path, quality=format_options.get('quality', 95))
    elif suffix == '.webp':
        image.save(path, quality=format_options.get('quality', 90))
    else:
        image.save(path)
```

---

## Performance Considerations

### API Latency

- **Network round-trip**: 100-500ms typical
- **AI processing**: 2-10 seconds depending on complexity
- **Total per image**: 3-15 seconds typical

### Memory Usage

- **PIL Images**: Size depends on resolution
  - 1024x1024 RGBA: ~4MB in memory
  - 4096x4096 RGBA: ~64MB in memory
- **Style files**: Negligible (typically < 10KB)

### Optimization Opportunities

1. **Parallel API calls** (if rate limits allow)
   - Use `asyncio` or `concurrent.futures`
   - Would speed up batch generation significantly

2. **Caching**
   - Cache API client (already done implicitly)
   - Cache loaded styles (if reusing frequently)

3. **Streaming**
   - Not currently supported by image generation API
   - Would reduce perceived latency

---

## Security Considerations

### API Key Protection

**Current approach**: Environment variable

**Best practices**:
- Never commit API keys to version control
- Use environment variables or secure vaults
- Rotate keys periodically
- Monitor usage for anomalies

### Input Validation

**Current approach**: Minimal validation

**What's validated**:
- File existence (style, edit, ref)
- Aspect ratio choices (argparse)

**What's NOT validated**:
- Prompt content (passed directly to API)
- Image content (passed directly to API)
- Output path (could overwrite files)

**Recommendations for production**:
- Sanitize or validate prompts if accepting untrusted input
- Validate output paths to prevent overwriting important files
- Add size limits for input images

### Network Security

- All API communication uses HTTPS
- API key transmitted in request headers
- No sensitive data stored locally (except optional .env)

---

## Future Architecture Considerations

### Potential Enhancements

1. **Configuration File**
   - `~/.nanobanana/config.yaml` for defaults
   - Override with CLI arguments

2. **Plugin System**
   - Post-processing plugins
   - Custom style loaders
   - Alternative API backends

3. **Web Interface**
   - Flask/FastAPI wrapper
   - Would need different architecture (async, etc.)

4. **Caching Layer**
   - Cache similar prompts
   - Reduce API costs for repeated requests

### Scalability Concerns

If scaling beyond CLI tool:
- API rate limiting becomes critical
- Need request queuing
- Consider async architecture
- May need database for job tracking

---

This architecture documentation should help you understand not just *what* the code does, but *why* it's structured this way. Use this knowledge to make informed decisions when extending or modifying the system.
