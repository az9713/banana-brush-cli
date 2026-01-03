# Banana Brush CLI - Project Context for Claude Code

This file provides context for Claude Code to understand and work with this project effectively.

## Project Overview

**Banana Brush CLI** is a command-line image generation tool that integrates Google's Gemini API (nicknamed "Nano Banana Pro") with Claude Code. It enables AI-assisted image generation, editing, and style-consistent asset creation directly from the terminal.

## Acknowledgements

This project is inspired by the YouTube video **["I Added Unlimited Image Generation To Claude Code (Nano Banana)"](https://www.youtube.com/watch?v=NBibgD7I48w&t=10s)** by Zen van Riel.

All code and documentation were created by **Claude Code** and **Claude Opus 4.5**.

### References
- [Gemini Image Generation API Documentation](https://ai.google.dev/gemini-api/docs/image-generation)

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Language | Python 3.10+ | Core implementation |
| Package Manager | UV | Fast dependency management |
| Image Generation | Google Gemini API | AI image generation |
| Image Processing | Pillow (PIL) | Image loading/saving |

## Project Structure

```
nano-banana/
├── main.py                      # Core CLI application
├── pyproject.toml               # Project dependencies
├── README.md                    # Quick reference
├── CLAUDE.md                    # This file (Claude Code context)
├── .env.example                 # API key template
├── .gitignore                   # Git ignore rules
├── styles/                      # Style templates
│   └── blue_glass_3d.md         # Example style
├── images/                      # Generated images (from tutorial)
└── docs/                        # Documentation
    ├── QUICK_START.md           # 10+ educational use cases
    ├── USER_GUIDE.md            # Non-technical user guide
    ├── DEVELOPER_GUIDE.md       # Developer documentation
    ├── ARCHITECTURE.md          # Technical architecture
    └── TROUBLESHOOTING.md       # Common issues & solutions
```

## Key Commands

### Generate Image
```bash
uv run python main.py output.png "A 3D cube on black background"
```

### Generate with Style
```bash
uv run python main.py output.png "gear icon" --style styles/blue_glass_3d.md
```

### Edit Existing Image
```bash
uv run python main.py output.png "change background to blue" --edit input.png
```

### Use Reference Image
```bash
uv run python main.py output.png "sphere in same style" --ref reference.png
```

### Multiple Prompts (Batch)
```bash
uv run python main.py output.png "cube" "sphere" "pyramid" --style styles/blue_glass_3d.md
# Creates: output_1.png, output_2.png, output_3.png
```

## CLI Arguments Reference

| Argument | Required | Description |
|----------|----------|-------------|
| `output` | Yes | Output file path (e.g., `output.png`) |
| `prompts` | Yes | One or more text prompts |
| `--style` | No | Path to style markdown file |
| `--edit` | No | Input image to edit |
| `--ref` | No | Reference image for style consistency |
| `--aspect` | No | Aspect ratio (default: 1:1) |
| `--model` | No | Gemini model to use |

## Aspect Ratios

Supported values: `1:1`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`

## Available Models

| Model | Description |
|-------|-------------|
| `gemini-3-pro-image-preview` | High quality (default) |
| `gemini-2.5-flash-image` | Fast generation |
| `imagen-4.0-generate-001` | Imagen 4 model |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_API_KEY` | Yes | Google AI Studio API key |

## Style File Format

Style files are markdown documents that describe visual characteristics:

```markdown
# Style Name

Description of the visual style including:
- Material properties (glass, metal, plastic, etc.)
- Lighting setup (soft, dramatic, natural)
- Background specifications
- Composition guidelines
```

The style content is prepended to the user's prompt automatically.

## Code Conventions

- **Python version**: 3.10+ (uses type hints with `|` union syntax)
- **Formatting**: Standard Python conventions
- **Error handling**: Errors printed to stderr, exit code 1 on failure
- **Output**: Status messages to stdout during generation

## Development Commands

```bash
# Install dependencies
uv sync

# Run the tool
uv run python main.py <args>

# Run with verbose output (see full prompts)
# Add print statements in main.py if needed
```

## Common Tasks for Claude Code

### Creating New Style Files
1. Create a new `.md` file in `styles/`
2. Describe the visual style in natural language
3. Include: materials, lighting, background, composition

### Adding New Features
1. Modify `main.py` - add new argparse arguments
2. Update the `generate_image()` function for new API options
3. Update `README.md` and documentation

### Debugging API Issues
1. Check `GOOGLE_API_KEY` is set correctly
2. Verify model name is valid
3. Check API quota/rate limits
4. Review error messages from the API response

## Important Notes

- **Gradients**: Avoid complex gradients in generated images - they degrade with iterative edits
- **Text**: Add text in post-production (Canva/Photoshop) for best results
- **Consistency**: Use `--ref` flag to maintain style across multiple generations
- **Batch generation**: Multiple prompts create numbered output files
