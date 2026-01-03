# Nano Banana Pro Developer Guide

A comprehensive guide for developers who want to understand, modify, or extend Nano Banana Pro. Written for developers with traditional programming backgrounds (C, C++, Java) who may be new to Python and modern web/AI development.

---

## Table of Contents

1. [Introduction for Traditional Developers](#introduction-for-traditional-developers)
2. [Technology Stack Explained](#technology-stack-explained)
3. [Development Environment Setup](#development-environment-setup)
4. [Project Structure Deep Dive](#project-structure-deep-dive)
5. [Code Walkthrough](#code-walkthrough)
6. [How to Make Changes](#how-to-make-changes)
7. [Adding New Features](#adding-new-features)
8. [Testing Your Changes](#testing-your-changes)
9. [Common Development Tasks](#common-development-tasks)
10. [Python for C/C++/Java Developers](#python-for-cc-java-developers)
11. [Deployment and Distribution](#deployment-and-distribution)
12. [Contributing Guidelines](#contributing-guidelines)

---

## Introduction for Traditional Developers

If you're coming from C, C++, or Java, here's what's different about this project:

### Key Differences from Traditional Development

| Aspect | C/C++/Java | Python (This Project) |
|--------|------------|----------------------|
| **Compilation** | Compile then run | Run directly (interpreted) |
| **Type System** | Strict/static | Dynamic (with optional hints) |
| **Package Management** | Manual/CMake/Maven | UV/pip (automatic) |
| **Memory Management** | Manual (C/C++) or GC (Java) | Garbage collected |
| **Entry Point** | `main()` function | `if __name__ == "__main__":` |
| **Build System** | Makefiles/CMakeLists/Gradle | pyproject.toml |

### What You'll Recognize

- **Functions**: Work similarly to C/Java methods
- **Control flow**: `if`, `for`, `while` work the same way
- **Data structures**: Lists (like arrays), dicts (like HashMaps)
- **Classes**: Similar to Java/C++ classes
- **Error handling**: `try/except` instead of `try/catch`

---

## Technology Stack Explained

### Python 3.10+

**What it is**: The programming language this project is written in.

**Why 3.10+**: We use modern Python features like:
- Type hints with `|` union syntax: `str | None` instead of `Optional[str]`
- Better error messages
- Pattern matching (if needed)

**Equivalent concept**: Like choosing C++17 vs C++11 - newer version with better features.

### UV Package Manager

**What it is**: A fast tool for managing Python dependencies (like npm for Node.js, or Maven for Java).

**Why UV over pip**:
- 10-100x faster than pip
- Creates isolated environments automatically
- Handles dependency resolution better

**Key commands**:
```bash
uv sync          # Install all dependencies (like 'mvn install')
uv run python    # Run Python in the project environment
uv add package   # Add a new dependency
```

**Equivalent concept**: Like `npm install` or `maven dependency:resolve`.

### Google Gemini API

**What it is**: Google's AI service that generates images from text descriptions.

**How it works**:
1. You send a text prompt (and optionally images) to Google's servers
2. Their AI model processes the request
3. They send back generated image data

**Equivalent concept**: Like calling a REST API, but with AI processing.

### Pillow (PIL)

**What it is**: Python Imaging Library - handles image file operations.

**What we use it for**:
- Loading images from disk
- Saving generated images
- Converting between formats

**Equivalent concept**: Like ImageMagick or Java's BufferedImage.

### pyproject.toml

**What it is**: The project configuration file (like `pom.xml` for Maven or `CMakeLists.txt` for CMake).

**What it contains**:
- Project metadata (name, version)
- Dependencies
- Build system configuration

---

## Development Environment Setup

Follow these steps exactly to set up your development environment.

### Step 1: Install Python 3.10+

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.10 or newer
3. Run installer, **CHECK "Add Python to PATH"**
4. Complete installation

**Mac:**
```bash
# Using Homebrew (recommended)
brew install python@3.11
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv
```

**Verify installation:**
```bash
python --version
# or
python3 --version
# Should show: Python 3.10.x or higher
```

### Step 2: Install UV

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Mac/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Verify:**
```bash
uv --version
```

### Step 3: Clone/Download the Project

```bash
# If using Git
git clone <repository-url>
cd nano-banana

# Or download and extract ZIP, then navigate to folder
cd path/to/nano-banana
```

### Step 4: Install Dependencies

```bash
uv sync
```

This reads `pyproject.toml` and installs all required packages into an isolated environment.

### Step 5: Set Up API Key

**For development, create a `.env` file (optional but convenient):**

Create a file named `.env` in the project root:
```
GOOGLE_API_KEY=your-api-key-here
```

Then modify your shell to load it, or set it manually each session.

**Or set it in your shell:**
```bash
# Mac/Linux
export GOOGLE_API_KEY="your-api-key-here"

# Windows PowerShell
$env:GOOGLE_API_KEY="your-api-key-here"
```

### Step 6: Verify Setup

```bash
uv run python main.py test.png "A blue square"
```

If `test.png` is created, your environment is ready!

---

## Project Structure Deep Dive

```
nano-banana/
├── main.py                 # Main application (all code is here)
├── pyproject.toml          # Project configuration and dependencies
├── README.md               # Quick reference documentation
├── CLAUDE.md               # Context file for Claude Code AI
├── .env                    # (Optional) Environment variables
├── styles/                 # Style template files
│   └── blue_glass_3d.md    # Example style
├── docs/                   # Documentation
│   ├── QUICK_START.md      # Tutorial with examples
│   ├── USER_GUIDE.md       # End-user documentation
│   ├── DEVELOPER_GUIDE.md  # This file
│   ├── ARCHITECTURE.md     # Technical architecture
│   └── TROUBLESHOOTING.md  # Problem solutions
└── output/                 # (Created automatically) Generated images
```

### File-by-File Explanation

#### `main.py` (Core Application)

This is the entire application in one file (~150 lines). Unlike large Java/C++ projects with many files, Python projects often keep related code together.

**Structure:**
```python
# Imports (like #include in C or import in Java)
import argparse
import os
...

# Helper functions
def get_client(): ...
def load_style(): ...
def load_image(): ...
def build_prompt(): ...
def generate_image(): ...
def get_output_path(): ...

# Main entry point
def main(): ...

# Execution guard (explained below)
if __name__ == "__main__":
    main()
```

#### `pyproject.toml` (Configuration)

```toml
[project]
name = "nano-banana"        # Project name
version = "1.0.0"           # Semantic versioning
description = "..."         # What the project does
requires-python = ">=3.10"  # Minimum Python version

dependencies = [            # Required packages
    "google-genai>=1.0.0",  # Google's AI SDK
    "Pillow>=10.0.0",       # Image processing
]

[build-system]              # How to build the project
requires = ["hatchling"]
build-backend = "hatchling.build"
```

**Equivalent to:**
- `pom.xml` in Maven
- `package.json` in Node.js
- `CMakeLists.txt` in CMake

#### `styles/*.md` (Style Templates)

Plain text files containing natural language descriptions of visual styles. The entire file content is read and prepended to user prompts.

**Example (`styles/blue_glass_3d.md`):**
```markdown
# Blue Glass 3D Style

Generate a 3D rendered object with the following characteristics:

## Visual Style
- Material: Translucent blue glass with subtle reflections
...
```

**Why Markdown?**
- Human-readable and editable
- Can include formatting for organization
- The AI interprets it as natural language

---

## Code Walkthrough

Let's examine each part of `main.py` in detail.

### Imports Section

```python
#!/usr/bin/env python3
"""
Docstring - describes the module/file
"""

import argparse     # Command-line argument parsing (like getopt in C)
import os           # Operating system interface (like <stdlib.h>)
import sys          # System-specific parameters (like stderr)
from pathlib import Path  # Object-oriented file paths

from google import genai        # Google's AI SDK
from google.genai import types  # Type definitions for the API
from PIL import Image          # Image processing library
```

**C/C++ Equivalent:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// etc.
```

### get_client() Function

```python
def get_client() -> genai.Client:
    """Initialize Gemini client with API key from environment."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)
    return genai.Client(api_key=api_key)
```

**What it does:**
1. Gets the API key from environment variables
2. If not found, prints error and exits
3. Creates and returns a configured API client

**Type hints explained:**
- `-> genai.Client` means "this function returns a genai.Client object"
- Like `genai.Client get_client()` in Java/C++

**C equivalent concept:**
```c
ApiClient* get_client() {
    char* api_key = getenv("GOOGLE_API_KEY");
    if (api_key == NULL) {
        fprintf(stderr, "Error: API key not set\n");
        exit(1);
    }
    return create_client(api_key);
}
```

### load_style() Function

```python
def load_style(style_path: str) -> str:
    """Load style description from markdown file."""
    path = Path(style_path)
    if not path.exists():
        print(f"Error: Style file not found: {style_path}", file=sys.stderr)
        sys.exit(1)
    return path.read_text(encoding="utf-8").strip()
```

**What it does:**
1. Converts string path to Path object
2. Checks if file exists
3. Reads entire file content as string
4. Removes leading/trailing whitespace with `.strip()`

**f-strings explained:**
`f"Error: Style file not found: {style_path}"` is Python's string interpolation.
- Like `printf("Error: %s", style_path)` in C
- Like `String.format("Error: %s", stylePath)` in Java

### load_image() Function

```python
def load_image(image_path: str) -> Image.Image:
    """Load image from file path."""
    path = Path(image_path)
    if not path.exists():
        print(f"Error: Image file not found: {image_path}", file=sys.stderr)
        sys.exit(1)
    return Image.open(path)
```

**What it does:**
Opens an image file and returns a PIL Image object that can be manipulated or sent to the API.

### build_prompt() Function

```python
def build_prompt(user_prompt: str, style_content: str | None) -> str:
    """Build full prompt by combining style and user prompt."""
    if style_content:
        return f"{style_content}\n\nSubject: {user_prompt}"
    return user_prompt
```

**Type hint `str | None`:**
- Means "either a string or None (null)"
- Like `@Nullable String` in Java
- The `|` syntax requires Python 3.10+

### generate_image() Function

```python
def generate_image(
    client: genai.Client,
    prompt: str,
    model: str = "gemini-2.5-flash-preview-native-audio-dialog",
    aspect_ratio: str = "1:1",
    edit_image: Image.Image | None = None,
    ref_image: Image.Image | None = None,
) -> Image.Image | None:
```

**Default parameters:**
- `model: str = "gemini-..."` means if not provided, use this default
- Like default arguments in C++

**Function body explained:**

```python
    # Build contents list (what we send to the API)
    contents = []

    # Add image if editing or using reference
    if edit_image:
        contents.append(edit_image)
        prompt = f"Edit this image: {prompt}"
    elif ref_image:
        contents.append(ref_image)
        prompt = f"Using this image as a style reference, create: {prompt}"

    contents.append(prompt)

    # Configure the API request
    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],  # We want both text and image back
        image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
    )

    # Make the API call (this is where the actual HTTP request happens)
    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=config,
        )
    except Exception as e:
        print(f"API Error: {e}", file=sys.stderr)
        return None

    # Extract the image from the response
    for part in response.parts:
        if part.inline_data is not None:
            return part.as_image()  # Convert to PIL Image

    return None
```

### main() Function

The entry point that ties everything together:

```python
def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Generate images using Gemini API (Nano Banana Pro)",
    )

    # Define positional arguments (required)
    parser.add_argument("output", help="Output file path")
    parser.add_argument("prompts", nargs="+", help="Image prompt(s)")

    # Define optional arguments
    parser.add_argument("--style", help="Style markdown file path")
    parser.add_argument("--edit", help="Input image to edit")
    parser.add_argument("--ref", help="Reference image")
    parser.add_argument("--aspect", default="1:1", choices=[...])
    parser.add_argument("--model", default="...")

    # Parse the arguments
    args = parser.parse_args()

    # Rest of the logic...
```

**argparse explained:**
- Like `getopt()` in C but much more powerful
- Automatically generates `--help` output
- Validates choices, types, etc.

### The `if __name__ == "__main__":` Guard

```python
if __name__ == "__main__":
    main()
```

**What this does:**
- `__name__` is a special variable
- When running the file directly, `__name__ == "__main__"`
- When importing the file as a module, `__name__ == "nano_banana"` (or whatever)

**Why use it:**
- Allows the file to be both run directly AND imported as a library
- Like having `main()` vs library code in C

---

## How to Make Changes

### Modifying Existing Functionality

**Example: Add a new aspect ratio**

1. Find the `--aspect` argument in `main.py`:
```python
parser.add_argument(
    "--aspect",
    default="1:1",
    choices=["1:1", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
    help="Aspect ratio (default: 1:1)",
)
```

2. Add your new ratio to the `choices` list:
```python
    choices=["1:1", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9", "2:1"],  # Added 2:1
```

3. Test:
```bash
uv run python main.py test.png "wide banner" --aspect 2:1
```

### Adding a New Command-Line Argument

**Example: Add a `--quality` flag**

1. Add the argument definition:
```python
parser.add_argument(
    "--quality",
    choices=["low", "medium", "high"],
    default="medium",
    help="Output quality level",
)
```

2. Use it in the generation logic:
```python
# After args = parser.parse_args()
quality = args.quality
# Use quality variable as needed
```

### Debugging

**Add print statements:**
```python
print(f"DEBUG: prompt = {prompt}")
print(f"DEBUG: contents = {contents}")
```

**Check variable types:**
```python
print(f"DEBUG: type of response = {type(response)}")
```

**Use Python's debugger:**
```python
import pdb; pdb.set_trace()  # Breakpoint
```

---

## Adding New Features

### Feature: Save Generation Metadata

**Goal:** Save prompt and settings alongside the image.

**Implementation:**

```python
import json
from datetime import datetime

def save_metadata(output_path: str, prompt: str, args):
    """Save generation metadata as JSON."""
    metadata = {
        "prompt": prompt,
        "model": args.model,
        "aspect_ratio": args.aspect,
        "style": args.style,
        "timestamp": datetime.now().isoformat(),
    }

    # Create metadata filename
    meta_path = Path(output_path).with_suffix(".json")

    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2)
```

**Usage in main():**
```python
if image:
    image.save(output_path)
    save_metadata(output_path, full_prompt, args)  # Add this line
    print(f"Saved: {output_path}")
```

### Feature: Support JPEG Output

**Goal:** Allow saving as JPEG with quality control.

**Implementation:**

```python
def save_image(image: Image.Image, output_path: str, quality: int = 95):
    """Save image with format-specific options."""
    path = Path(output_path)

    if path.suffix.lower() in [".jpg", ".jpeg"]:
        # JPEG needs RGB mode (no transparency)
        if image.mode in ["RGBA", "P"]:
            image = image.convert("RGB")
        image.save(path, quality=quality)
    else:
        # PNG and others
        image.save(path)
```

---

## Testing Your Changes

### Manual Testing

Always test your changes with real commands:

```bash
# Test basic functionality
uv run python main.py test1.png "A red circle"

# Test with style
uv run python main.py test2.png "A cube" --style styles/blue_glass_3d.md

# Test edge cases
uv run python main.py test3.png ""  # Empty prompt - should it error?
uv run python main.py test4.png "test" --style nonexistent.md  # Missing file
```

### Creating Automated Tests

Create a file `test_main.py`:

```python
import unittest
from pathlib import Path
from main import load_style, build_prompt, get_output_path

class TestNanoBanana(unittest.TestCase):

    def test_build_prompt_without_style(self):
        result = build_prompt("A cube", None)
        self.assertEqual(result, "A cube")

    def test_build_prompt_with_style(self):
        result = build_prompt("A cube", "Blue glass style")
        self.assertIn("Blue glass style", result)
        self.assertIn("A cube", result)

    def test_get_output_path_single(self):
        result = get_output_path("output.png", 1, 1)
        self.assertEqual(result, "output.png")

    def test_get_output_path_multiple(self):
        result = get_output_path("output.png", 2, 3)
        self.assertEqual(result, "output_2.png")

if __name__ == "__main__":
    unittest.main()
```

**Run tests:**
```bash
uv run python -m pytest test_main.py
# or
uv run python test_main.py
```

---

## Common Development Tasks

### Adding a New Dependency

```bash
# Add a package
uv add requests

# Add a development-only package
uv add --dev pytest
```

This updates `pyproject.toml` automatically.

### Updating Dependencies

```bash
uv sync --upgrade
```

### Checking Code Style

```bash
# Install linter
uv add --dev ruff

# Run linter
uv run ruff check main.py

# Auto-fix issues
uv run ruff check --fix main.py
```

### Type Checking

```bash
# Install type checker
uv add --dev mypy

# Run type checker
uv run mypy main.py
```

---

## Python for C/C++/Java Developers

### Quick Reference Table

| C/C++/Java | Python |
|------------|--------|
| `int x = 5;` | `x = 5` or `x: int = 5` |
| `String s = "hello";` | `s = "hello"` or `s: str = "hello"` |
| `int[] arr = {1, 2, 3};` | `arr = [1, 2, 3]` |
| `HashMap<String, Int>` | `dict = {"key": 1}` |
| `for (int i = 0; i < 10; i++)` | `for i in range(10):` |
| `for (String s : list)` | `for s in list:` |
| `if (x == 5) { }` | `if x == 5:` |
| `null` | `None` |
| `true / false` | `True / False` |
| `&&` / `||` | `and` / `or` |
| `try { } catch { }` | `try: except:` |
| `this` | `self` |
| `// comment` | `# comment` |
| `/* block */` | `""" docstring """` |

### Common Gotchas

**Indentation matters:**
```python
# WRONG - inconsistent indentation
if condition:
print("hello")  # IndentationError!

# CORRECT
if condition:
    print("hello")
```

**No semicolons needed:**
```python
x = 5  # No semicolon at end
y = 10
```

**Truthy/Falsy values:**
```python
if some_list:    # True if list is not empty
if some_string:  # True if string is not empty
if some_number:  # True if number is not 0
if some_object:  # True if object is not None
```

**List comprehensions (powerful shorthand):**
```python
# Instead of:
squares = []
for x in range(10):
    squares.append(x ** 2)

# You can write:
squares = [x ** 2 for x in range(10)]
```

---

## Deployment and Distribution

### Creating a Distributable Package

1. Ensure `pyproject.toml` is complete
2. Build the package:
   ```bash
   uv build
   ```
3. This creates files in `dist/`:
   - `nano_banana-1.0.0.tar.gz` (source)
   - `nano_banana-1.0.0-py3-none-any.whl` (wheel)

### Installing on Another Machine

```bash
# From the wheel file
pip install nano_banana-1.0.0-py3-none-any.whl

# Or from source
pip install .
```

---

## Contributing Guidelines

### Code Style

- Use 4 spaces for indentation (not tabs)
- Maximum line length: 100 characters
- Use type hints for function parameters and return values
- Write docstrings for all public functions

### Commit Messages

Format: `type: description`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding tests

Examples:
```
feat: add support for JPEG output
fix: handle empty prompt gracefully
docs: update developer guide
```

### Pull Request Process

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Update documentation if needed
5. Submit PR with clear description

---

## Getting Help

- **Architecture questions**: See [ARCHITECTURE.md](ARCHITECTURE.md)
- **Common problems**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **API reference**: https://ai.google.dev/gemini-api/docs
- **Python reference**: https://docs.python.org/3/

---

You now have everything needed to understand, modify, and extend Nano Banana Pro. Happy coding!
