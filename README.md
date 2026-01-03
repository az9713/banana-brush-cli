# Banana Brush CLI - AI Image Generation Tool

A command-line tool for generating and editing images using Google's Gemini API. Designed for use with Claude Code to enable AI-assisted image generation, editing, and style-consistent asset creation.

---

## Documentation

| Document | Audience | Description |
|----------|----------|-------------|
| **[Quick Start Guide](docs/QUICK_START.md)** | Everyone | Get started in 5 minutes with 12 hands-on examples |
| **[User Guide](docs/USER_GUIDE.md)** | End Users | Complete guide for non-technical users |
| **[Developer Guide](docs/DEVELOPER_GUIDE.md)** | Developers | Technical guide for extending the project |
| **[Architecture](docs/ARCHITECTURE.md)** | Developers | System design and technical decisions |
| **[Troubleshooting](docs/TROUBLESHOOTING.md)** | Everyone | Solutions for common problems |

---

## Quick Setup (2 minutes)

### 1. Get an API Key
Visit https://aistudio.google.com/apikey and create a free API key.

### 2. Set Your API Key
```bash
# Mac/Linux
export GOOGLE_API_KEY="your-api-key-here"

# Windows (PowerShell)
$env:GOOGLE_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set GOOGLE_API_KEY=your-api-key-here
```

### 3. Install Dependencies
```bash
uv sync
```

### 4. Generate Your First Image
```bash
uv run python main.py my_image.png "A friendly robot waving hello"
```

---

## Usage Examples

### Basic Generation
```bash
uv run python main.py output.png "A 3D cube on black background"
```

### With Style Template
```bash
uv run python main.py output.png "A gear icon" --style styles/blue_glass_3d.md
```

### Multiple Images (Batch)
```bash
uv run python main.py icons.png "cube" "sphere" "pyramid" --style styles/blue_glass_3d.md
# Creates: icons_1.png, icons_2.png, icons_3.png
```

### Edit Existing Image
```bash
uv run python main.py edited.png "Change the rocket to a star" --edit original.png
```

### Use Reference for Consistency
```bash
uv run python main.py new.png "Same style but with a heart" --ref reference.png
```

### Different Aspect Ratios
```bash
uv run python main.py thumbnail.png "Epic landscape" --aspect 16:9    # YouTube
uv run python main.py story.png "Coffee aesthetic" --aspect 9:16      # Instagram Story
uv run python main.py post.png "Product photo" --aspect 1:1           # Square
```

---

## Command Reference

```
uv run python main.py <output> <prompts...> [options]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `output` | Yes | Output filename (e.g., `image.png`) |
| `prompts` | Yes | One or more text descriptions |
| `--style` | No | Path to style markdown file |
| `--edit` | No | Input image to modify |
| `--ref` | No | Reference image for style matching |
| `--aspect` | No | Aspect ratio (default: `1:1`) |
| `--model` | No | AI model to use |

### Supported Aspect Ratios
`1:1` | `3:4` | `4:3` | `4:5` | `5:4` | `9:16` | `16:9` | `21:9`

---

## Project Structure

```
nano-banana/
├── main.py                    # Core application
├── pyproject.toml             # Dependencies
├── README.md                  # This file
├── CLAUDE.md                  # Claude Code context
├── .env.example               # API key template
├── .gitignore                 # Git ignore rules
├── styles/
│   └── blue_glass_3d.md       # Example style template
├── images/                    # Generated images (from tutorial)
│   ├── 1_cube_basic.png
│   ├── 2_cube_styled.png
│   ├── 3_shapes_1.png
│   ├── 3_shapes_2.png
│   ├── 3_shapes_3.png
│   ├── 4_rocket.png
│   ├── 5_flag.png
│   └── 6_star.png
└── docs/
    ├── QUICK_START.md         # Tutorial with examples
    ├── USER_GUIDE.md          # End-user documentation
    ├── DEVELOPER_GUIDE.md     # Developer documentation
    ├── ARCHITECTURE.md        # Technical architecture
    └── TROUBLESHOOTING.md     # Problem solutions
```

---

## Creating Custom Styles

Style files are markdown documents describing visual characteristics:

```markdown
# My Custom Style

## Visual Properties
- Material: Glossy plastic with subtle reflections
- Colors: Vibrant primary colors (red, blue, yellow)
- Lighting: Soft studio lighting from above

## Background
- Solid white background (#FFFFFF)
- Clean, no shadows

## Composition
- Object centered
- Minimal, icon-like appearance
```

Save as `styles/my_style.md` and use:
```bash
uv run python main.py icon.png "A star" --style styles/my_style.md
```

---

## Tips for Best Results

1. **Be Descriptive**: "A golden retriever puppy in a sunny park" works better than "a dog"

2. **Specify Style**: Add "photorealistic", "cartoon", "minimalist", "3D rendered" to your prompts

3. **Avoid Gradients**: Solid colors work better for images you'll edit later

4. **Add Text Separately**: Use Canva/Photoshop for text overlays

5. **Use References**: The `--ref` flag helps maintain consistency across multiple images

---

## Available Models

| Model | Description |
|-------|-------------|
| `gemini-3-pro-image-preview` | High quality (default) |
| `gemini-2.5-flash-image` | Fast generation |
| `imagen-4.0-generate-001` | Imagen 4 model |

```bash
uv run python main.py output.png "prompt" --model gemini-2.5-flash-image
```

---

## Requirements

- Python 3.10+
- UV package manager
- Google API key (free tier available)

---

## Need Help?

- **Getting started?** → [Quick Start Guide](docs/QUICK_START.md)
- **Using the tool?** → [User Guide](docs/USER_GUIDE.md)
- **Developing/extending?** → [Developer Guide](docs/DEVELOPER_GUIDE.md)
- **Having problems?** → [Troubleshooting](docs/TROUBLESHOOTING.md)

---

## Acknowledgements

This project is inspired by the YouTube video **["I Added Unlimited Image Generation To Claude Code (Nano Banana)"](https://www.youtube.com/watch?v=NBibgD7I48w&t=10s)** by Zen van Riel. "Nano Banana Pro" is the community nickname for Google's Gemini image generation models.

All code and documentation were created by **Claude Code** and **Claude Opus 4.5**.

### References
- [Gemini Image Generation API Documentation](https://ai.google.dev/gemini-api/docs/image-generation)
