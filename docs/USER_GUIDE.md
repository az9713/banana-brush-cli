# Banana Brush CLI User Guide

A complete guide for users who want to generate AI images using Banana Brush CLI. No programming experience required.

---

## Table of Contents

1. [What is Banana Brush CLI?](#what-is-banana-brush-cli)
2. [Understanding the Basics](#understanding-the-basics)
3. [Installation Guide](#installation-guide)
4. [How to Use Banana Brush CLI](#how-to-use-banana-brush-cli)
5. [Working with Styles](#working-with-styles)
6. [Editing Images](#editing-images)
7. [Advanced Features](#advanced-features)
8. [Best Practices](#best-practices)
9. [Frequently Asked Questions](#frequently-asked-questions)

---

## What is Banana Brush CLI?

Banana Brush CLI is a tool that lets you create images using artificial intelligence (AI). It uses Google's Gemini image generation API (nicknamed "Nano Banana Pro" by the community). Instead of drawing or using photo editing software, you describe what you want in plain English, and the AI creates it for you.

### What Can You Create?

- **Icons** for apps and websites
- **Logos** and brand graphics
- **Social media images** in various sizes
- **Product mockups** for presentations
- **Artistic images** for any purpose
- **Consistent image sets** with matching styles

### How Does It Work?

1. You type a description (called a "prompt") of what you want
2. Banana Brush CLI sends your description to Google's AI
3. The AI generates an image based on your description
4. The image is saved to your computer

It's like having a professional designer who can create any image you describe!

---

## Understanding the Basics

Before we start, let's understand some key concepts.

### What is a Terminal/Command Line?

A terminal (also called command line or console) is a text-based way to interact with your computer. Instead of clicking buttons, you type commands.

**How to open the terminal:**

| Operating System | How to Open |
|-----------------|-------------|
| **Windows 10/11** | Press `Win + R`, type `cmd`, press Enter |
| **Mac** | Press `Cmd + Space`, type `Terminal`, press Enter |
| **Linux** | Press `Ctrl + Alt + T` |

### What is a Command?

A command is an instruction you type in the terminal. For Banana Brush CLI, commands look like this:

```
uv run python main.py output.png "A red apple"
```

Let's break this down:

| Part | What It Means |
|------|---------------|
| `uv run python` | "Run the Python program using UV" |
| `main.py` | The name of Banana Brush CLI's program file |
| `output.png` | The name you want for your image |
| `"A red apple"` | Your description of what to create |

### What is a Prompt?

A "prompt" is your description of the image you want. The more detailed your prompt, the better the result.

**Simple prompt**: `"A cat"`
**Better prompt**: `"A fluffy orange tabby cat sitting on a windowsill, sunlight streaming in, cozy atmosphere"`

### What is an API Key?

An API key is like a password that lets Banana Brush CLI talk to Google's AI. You get one for free from Google, and it looks like a long string of letters and numbers:

```
AIzaSyB1234567890abcdefghijklmnop
```

---

## Installation Guide

Follow these steps exactly. Each step builds on the previous one.

### Step 1: Install UV (Package Manager)

UV is a tool that helps install and run Python programs. You need to install it once.

**On Windows:**

1. Open PowerShell (press `Win + X`, click "Windows PowerShell")
2. Copy and paste this command:
   ```powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
3. Press Enter
4. Wait for the installation to complete
5. Close and reopen PowerShell

**On Mac:**

1. Open Terminal (press `Cmd + Space`, type "Terminal")
2. Copy and paste this command:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
3. Press Enter
4. Wait for the installation to complete
5. Close and reopen Terminal

**On Linux:**

1. Open Terminal (`Ctrl + Alt + T`)
2. Copy and paste this command:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
3. Press Enter
4. Wait for the installation to complete
5. Close and reopen Terminal

**How to verify UV is installed:**
```bash
uv --version
```
You should see a version number like `uv 0.4.x`.

### Step 2: Get Your Google API Key

1. Open your web browser (Chrome, Firefox, Edge, Safari)
2. Go to: **https://aistudio.google.com/apikey**
3. Sign in with your Google account (or create one if needed)
4. Click the **"Create API Key"** button
5. A key will appear - it looks like: `AIzaSyB1234...`
6. Click the **copy button** next to the key
7. **Save this key somewhere safe** (like a password manager or a secure note)

> **Important**: Keep your API key secret! Don't share it publicly.

### Step 3: Set Your API Key

You need to tell your computer about your API key. This process differs by operating system.

**On Windows (Command Prompt):**

```cmd
set GOOGLE_API_KEY=paste-your-key-here
```

**On Windows (PowerShell):**

```powershell
$env:GOOGLE_API_KEY="paste-your-key-here"
```

**On Mac/Linux:**

```bash
export GOOGLE_API_KEY="paste-your-key-here"
```

> **Note**: This setting is temporary. When you close the terminal, you'll need to set it again. See "Making Your API Key Permanent" below.

### Step 4: Navigate to the Project Folder

In your terminal, you need to go to where Banana Brush CLI is located.

```bash
cd path/to/nano-banana
```

Replace `path/to/nano-banana` with the actual folder location.

**Example on Windows:**
```cmd
cd C:\Users\YourName\Downloads\nano-banana
```

**Example on Mac:**
```bash
cd ~/Downloads/nano-banana
```

### Step 5: Install Dependencies

Run this command to install everything Banana Brush CLI needs:

```bash
uv sync
```

You'll see output showing packages being installed. This only needs to be done once.

### Step 6: Test Your Installation

Run this test command:

```bash
uv run python main.py test.png "A happy sun with a smiling face"
```

**If successful**, you'll see:
```
Generating (1/1): A happy sun with a smiling face...
Saved: test.png
```

A file called `test.png` will appear in your folder!

---

## Making Your API Key Permanent

To avoid typing your API key every time:

**On Windows:**

1. Press `Win + R`
2. Type `sysdm.cpl` and press Enter
3. Click the **"Advanced"** tab
4. Click **"Environment Variables"**
5. Under "User variables", click **"New"**
6. Variable name: `GOOGLE_API_KEY`
7. Variable value: (paste your API key)
8. Click **OK** on all windows
9. Restart your terminal

**On Mac:**

1. Open Terminal
2. Type: `nano ~/.zshrc` (or `~/.bashrc` for older Macs)
3. Add this line at the bottom:
   ```
   export GOOGLE_API_KEY="your-api-key-here"
   ```
4. Press `Ctrl + X`, then `Y`, then Enter to save
5. Close and reopen Terminal

**On Linux:**

1. Open Terminal
2. Type: `nano ~/.bashrc`
3. Add this line at the bottom:
   ```
   export GOOGLE_API_KEY="your-api-key-here"
   ```
4. Press `Ctrl + X`, then `Y`, then Enter to save
5. Run: `source ~/.bashrc`

---

## How to Use Banana Brush CLI

### Basic Image Generation

The simplest command creates an image from a description:

```bash
uv run python main.py filename.png "Your description here"
```

**Examples:**

```bash
# A simple icon
uv run python main.py icon.png "A blue star icon"

# A landscape scene
uv run python main.py landscape.png "Mountains at sunset with orange sky"

# A product photo
uv run python main.py product.png "A coffee mug on a wooden table"
```

### Understanding the Command Structure

```
uv run python main.py [output] [prompts] [options]
```

| Part | Required? | Description |
|------|-----------|-------------|
| `uv run python main.py` | Yes | Runs the program |
| `[output]` | Yes | Filename for your image |
| `[prompts]` | Yes | One or more descriptions |
| `[options]` | No | Additional settings |

### Available Options

| Option | What It Does | Example |
|--------|-------------|---------|
| `--style` | Apply a style template | `--style styles/blue_glass_3d.md` |
| `--edit` | Edit an existing image | `--edit original.png` |
| `--ref` | Use a reference image | `--ref reference.png` |
| `--aspect` | Set image dimensions | `--aspect 16:9` |
| `--model` | Choose AI model | `--model gemini-2.0-flash-exp` |

### Aspect Ratios Explained

Aspect ratio is the width-to-height relationship of your image.

| Ratio | Shape | Best For |
|-------|-------|----------|
| `1:1` | Square | App icons, profile pictures |
| `16:9` | Wide landscape | YouTube thumbnails, desktop wallpapers |
| `9:16` | Tall portrait | Instagram stories, TikTok |
| `4:3` | Standard landscape | Presentations |
| `3:4` | Standard portrait | Instagram posts |
| `4:5` | Slightly tall | Instagram feed |
| `5:4` | Slightly wide | Photos |
| `3:2` | Classic photo | Photography |
| `2:3` | Classic portrait | Book covers |
| `21:9` | Ultra-wide | Banners, headers |

**Example:**
```bash
# YouTube thumbnail
uv run python main.py thumbnail.png "Epic gaming moment" --aspect 16:9

# Instagram story
uv run python main.py story.png "Morning coffee aesthetic" --aspect 9:16
```

---

## Working with Styles

Styles are pre-written descriptions that give your images a consistent look.

### What is a Style File?

A style file is a text document (ending in `.md`) that contains detailed instructions for how images should look. When you use a style, its contents are automatically added to your prompt.

### Using the Built-in Style

Banana Brush CLI comes with a "blue glass 3D" style:

```bash
uv run python main.py icon.png "A gear" --style styles/blue_glass_3d.md
```

This creates a gear icon that looks like polished blue glass.

### Creating Your Own Style

1. Open a text editor (Notepad, TextEdit, VS Code, etc.)
2. Write a description of your desired style
3. Save it as a `.md` file in the `styles` folder

**Example style file (`styles/neon_glow.md`):**

```markdown
# Neon Glow Style

Create an image with these characteristics:

## Colors
- Vibrant neon colors (pink, blue, purple, green)
- Glowing edges and outlines
- Dark/black background to make neon pop

## Effects
- Soft glow around all elements
- Light reflection on surfaces
- Slight blur on glow edges

## Mood
- Futuristic, cyberpunk aesthetic
- Night-time feel
- High contrast between dark and bright areas
```

**Use your new style:**
```bash
uv run python main.py neon_icon.png "A lightning bolt" --style styles/neon_glow.md
```

### Style Tips

- Be specific about colors, materials, and lighting
- Describe the mood or atmosphere you want
- Mention what you DON'T want (e.g., "no text", "no borders")
- Keep styles focused on visual characteristics, not subject matter

---

## Editing Images

You can modify existing images instead of creating new ones from scratch.

### How to Edit an Image

Use the `--edit` flag with an input image:

```bash
uv run python main.py output.png "Your changes" --edit input.png
```

### Edit Examples

**Change a color:**
```bash
uv run python main.py edited.png "Change the car from red to blue" --edit car.png
```

**Add an element:**
```bash
uv run python main.py edited.png "Add a sun in the top right corner" --edit landscape.png
```

**Remove an element:**
```bash
uv run python main.py edited.png "Remove the person from the background" --edit photo.png
```

**Replace an element:**
```bash
uv run python main.py edited.png "Replace the rocket with a star" --edit icon.png
```

### Edit Limitations

- Complex edits may not work perfectly
- Gradients can become distorted after editing
- Very detailed images may lose quality
- The AI interprets your instructions, so be specific

---

## Advanced Features

### Creating Multiple Images at Once

Generate several images with one command:

```bash
uv run python main.py icons.png "home" "search" "settings" "profile"
```

**Result:** Four files created:
- `icons_1.png` (home)
- `icons_2.png` (search)
- `icons_3.png` (settings)
- `icons_4.png` (profile)

### Using Reference Images

Make new images match the style of an existing image:

```bash
uv run python main.py new.png "A tree" --ref existing_icon.png
```

This tells the AI: "Create a tree that looks like it belongs with this other image."

### Combining Features

You can use multiple options together:

```bash
uv run python main.py icons.png "star" "heart" "moon" --style styles/blue_glass_3d.md --aspect 1:1
```

---

## Best Practices

### Writing Better Prompts

**Do:**
- Be specific: "A golden retriever puppy playing in autumn leaves"
- Describe style: "in the style of a watercolor painting"
- Mention lighting: "soft natural lighting", "dramatic shadows"
- Specify composition: "centered in frame", "close-up view"

**Don't:**
- Be too vague: "A dog" (what kind? doing what?)
- Contradict yourself: "A dark bright image"
- Request text: AI-generated text often looks bad

### Organizing Your Files

Create folders for different projects:

```
nano-banana/
├── output/
│   ├── app-icons/
│   ├── social-media/
│   └── marketing/
├── styles/
│   ├── blue_glass_3d.md
│   ├── neon_glow.md
│   └── minimalist.md
```

**Save to a subfolder:**
```bash
uv run python main.py output/app-icons/settings.png "A gear icon"
```

### Iterating on Results

1. Start with a basic prompt
2. Look at the result
3. Refine your prompt based on what's missing
4. Generate again
5. Repeat until satisfied

### Avoiding Gradient Issues

Gradients (smooth color transitions) can degrade when editing:

**Instead of:**
```bash
uv run python main.py icon.png "A gradient background from blue to purple"
```

**Do this:**
```bash
uv run python main.py icon.png "A solid dark blue background"
```

Then add gradients later in Canva, Photoshop, or another image editor.

---

## Frequently Asked Questions

### "I get an error about GOOGLE_API_KEY"

Your API key isn't set. Run this command (replace with your actual key):

```bash
# Windows
set GOOGLE_API_KEY=your-key-here

# Mac/Linux
export GOOGLE_API_KEY="your-key-here"
```

### "The image doesn't look like what I described"

Try being more specific in your prompt. Add details about:
- Style (realistic, cartoon, minimalist, etc.)
- Colors
- Lighting
- Background
- Composition

### "Can I generate text in images?"

AI-generated text often has errors. It's better to:
1. Generate the image without text
2. Add text using Canva, Photoshop, or another tool

### "The image quality seems low"

- Default resolution is optimized for speed
- For higher quality, use a different model:
  ```bash
  uv run python main.py output.png "prompt" --model gemini-2.0-flash-exp
  ```

### "How many images can I generate?"

Google provides free API credits. Typical limits:
- Several hundred images per day for free
- More with a paid plan

Check your usage at: https://aistudio.google.com/

### "Can I use these images commercially?"

Check Google's terms of service for the Gemini API. Generally:
- AI-generated images may have usage restrictions
- Always verify licensing for commercial use
- Images include an invisible watermark (SynthID)

### "The command isn't working at all"

1. Make sure you're in the correct folder: `cd path/to/nano-banana`
2. Make sure UV is installed: `uv --version`
3. Make sure dependencies are installed: `uv sync`
4. Check for typos in your command

---

## Getting Help

If you're stuck:

1. Check the [Troubleshooting Guide](TROUBLESHOOTING.md)
2. Re-read the [Quick Start Guide](QUICK_START.md)
3. Make sure all installation steps were completed

---

## Summary

You now know how to:

- ✅ Install and set up Banana Brush CLI
- ✅ Generate images from text descriptions
- ✅ Use style templates for consistency
- ✅ Edit existing images
- ✅ Create multiple images at once
- ✅ Use different aspect ratios
- ✅ Write effective prompts

Happy creating!
