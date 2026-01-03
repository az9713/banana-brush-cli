# Quick Start Guide - Nano Banana

Welcome to Nano Banana! This guide will get you generating AI images in under 5 minutes, with 12 hands-on examples to help you master the tool quickly.

---

## Table of Contents

1. [One-Time Setup (5 minutes)](#one-time-setup-5-minutes)
2. [Your First Image (1 minute)](#your-first-image-1-minute)
3. [Video Tutorial Sequence (6 Steps)](#video-tutorial-sequence-6-steps)
4. [12 Educational Use Cases](#12-educational-use-cases)
5. [What's Next?](#whats-next)

---

## One-Time Setup (5 minutes)

### Step 1: Get Your Google API Key

1. Open your web browser
2. Go to: https://aistudio.google.com/apikey
3. Sign in with your Google account
4. Click **"Create API Key"**
5. Copy the key (it looks like: `AIzaSy...`)
6. Keep this key safe - you'll need it in the next step

### Step 2: Set Up Your API Key

**Recommended: Use a `.env` file**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your key
# GOOGLE_API_KEY=your-api-key-here
```

**Alternative: Set in terminal (temporary)**

*Windows (Command Prompt):*
```cmd
set GOOGLE_API_KEY=your-api-key-here
```

*Windows (PowerShell):*
```powershell
$env:GOOGLE_API_KEY="your-api-key-here"
```

*Mac/Linux:*
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

> **Tip**: Using `.env` is recommended - your key persists across terminal sessions and is automatically ignored by git.

### Step 3: Install Dependencies

Open your terminal, navigate to the project folder, and run:

```bash
uv sync
```

This installs all required packages. You only need to do this once.

**What if `uv` isn't installed?**
```bash
# On Mac/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows (PowerShell):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 4: Verify Setup

Run this test command:
```bash
uv run python main.py test.png "A red apple on white background"
```

If you see `Saved: test.png`, congratulations! You're ready to go.

---

## Your First Image (1 minute)

Let's generate your first AI image:

```bash
uv run python main.py my_first_image.png "A friendly robot waving hello"
```

**What happens:**
1. The tool sends your prompt to Google's Gemini AI
2. Gemini generates an image based on your description
3. The image is saved to `my_first_image.png`
4. You see: `Saved: my_first_image.png`

Open the file to see your creation!

---

## Video Tutorial Sequence (6 Steps)

This sequence mirrors the demonstration from [Zen van Riel's tutorial video](https://www.youtube.com/watch?v=NBibgD7I48w). Follow these steps in order to experience the full workflow.

### Step 1: Basic Generation
Generate a simple 3D object without any styling.

```bash
uv run python main.py images/1_cube_basic.png "A 3D cube on solid black background"
```

**What you'll see**: A basic 3D cube. Notice the default style applied by the AI.

---

### Step 2: Generate with Blue Glass Style
Apply the included style template for a polished look.

```bash
uv run python main.py images/2_cube_styled.png "A 3D cube" --style styles/blue_glass_3d.md
```

**What you'll see**: A beautiful translucent blue glass cube with professional lighting.

---

### Step 3: Generate Multiple Styled Objects
Create a batch of consistent icons in one command.

```bash
uv run python main.py images/3_shapes.png "cube" "sphere" "pyramid" --style styles/blue_glass_3d.md
```

**Output files**:
- `images/3_shapes_1.png` - Cube
- `images/3_shapes_2.png` - Sphere
- `images/3_shapes_3.png` - Pyramid

**What you'll see**: Three objects that all share the same blue glass aesthetic.

---

### Step 4: Create an Icon
Generate an emoji-style icon for editing practice.

```bash
uv run python main.py images/4_rocket.png "A rocket ship emoji style icon" --style styles/blue_glass_3d.md
```

**What you'll see**: A stylized rocket icon in the blue glass style.

---

### Step 5: Edit the Icon (Replace Element)
This is the **key feature** demonstrated in the video - editing specific parts of an image without destroying the rest.

```bash
uv run python main.py images/5_flag.png "Remove the rocket ship and replace it with a checkered racing flag emoji, keep everything else the same" --edit images/4_rocket.png
```

**What you'll see**: The rocket is replaced with a flag, but the style and background remain intact!

---

### Step 6: Use Reference for New Creation
Create a new icon that matches the style of an existing image.

```bash
uv run python main.py images/6_star.png "A star shape in the exact same style" --ref images/2_cube_styled.png
```

**What you'll see**: A star that looks like it belongs with the cube - same materials, lighting, and feel.

---

### Complete Sequence (Copy-Paste Ready)

```bash
# Create images folder
mkdir -p images

# Step 1: Basic cube
uv run python main.py images/1_cube_basic.png "A 3D cube on solid black background"

# Step 2: Styled cube
uv run python main.py images/2_cube_styled.png "A 3D cube" --style styles/blue_glass_3d.md

# Step 3: Multiple shapes
uv run python main.py images/3_shapes.png "cube" "sphere" "pyramid" --style styles/blue_glass_3d.md

# Step 4: Rocket icon
uv run python main.py images/4_rocket.png "A rocket ship emoji style icon" --style styles/blue_glass_3d.md

# Step 5: Edit - replace rocket with flag
uv run python main.py images/5_flag.png "Remove the rocket ship and replace it with a checkered racing flag emoji, keep everything else the same" --edit images/4_rocket.png

# Step 6: New icon using reference
uv run python main.py images/6_star.png "A star shape in the exact same style" --ref images/2_cube_styled.png
```

---

### What This Sequence Teaches

| Step | Feature | Key Takeaway |
|------|---------|--------------|
| 1 | Basic generation | AI creates images from text |
| 2 | Style templates | Consistent aesthetics with `--style` |
| 3 | Batch generation | Multiple images in one command |
| 4 | Icon creation | Detailed prompts = better results |
| 5 | Image editing | Modify parts with `--edit` |
| 6 | Reference images | Match existing styles with `--ref` |

---

## 12 Educational Use Cases

These examples progress from simple to advanced. Try each one to build your skills.

---

### Use Case 1: Simple Object Generation

**Goal**: Generate a basic object with minimal description.

```bash
uv run python main.py uc1_cube.png "A 3D cube"
```

**What you learn**: The AI can create simple 3D objects from short prompts.

**Try variations**:
- `"A 3D sphere"`
- `"A 3D pyramid"`
- `"A 3D cylinder"`

---

### Use Case 2: Adding Background Colors

**Goal**: Control the background of your image.

```bash
uv run python main.py uc2_cube_black.png "A 3D blue cube on a solid black background"
```

**What you learn**: Being specific about backgrounds gives you more control.

**Try variations**:
- `"A red ball on white background"`
- `"A golden trophy on dark gray background"`
- `"A green plant on pastel pink background"`

---

### Use Case 3: Specifying Materials

**Goal**: Define what the object is made of.

```bash
uv run python main.py uc3_glass_sphere.png "A translucent glass sphere with light refracting through it, on black background"
```

**What you learn**: Material descriptions dramatically change the look.

**Try variations**:
- `"A polished chrome sphere reflecting light"`
- `"A wooden cube with visible grain texture"`
- `"A marble statue of a hand"`

---

### Use Case 4: Using Style Templates

**Goal**: Apply consistent styling using a style file.

```bash
uv run python main.py uc4_styled_gear.png "A gear icon" --style styles/blue_glass_3d.md
```

**What you learn**: Style files ensure consistent aesthetics across multiple images.

**How it works**: The style file contains detailed instructions that are automatically added to your prompt.

---

### Use Case 5: Generating Multiple Images at Once

**Goal**: Create several related images in one command.

```bash
uv run python main.py uc5_shapes.png "cube" "sphere" "pyramid" "cylinder" --style styles/blue_glass_3d.md
```

**What you learn**: Batch generation saves time when creating icon sets or related assets.

**Output files created**:
- `uc5_shapes_1.png` (cube)
- `uc5_shapes_2.png` (sphere)
- `uc5_shapes_3.png` (pyramid)
- `uc5_shapes_4.png` (cylinder)

---

### Use Case 6: Changing Aspect Ratios

**Goal**: Generate images in different dimensions.

**Square (1:1) - Default, great for icons:**
```bash
uv run python main.py uc6_square.png "A minimalist logo design" --aspect 1:1
```

**Landscape (16:9) - YouTube thumbnails:**
```bash
uv run python main.py uc6_landscape.png "A dramatic mountain landscape" --aspect 16:9
```

**Portrait (9:16) - Instagram stories:**
```bash
uv run python main.py uc6_portrait.png "A tall skyscraper at night" --aspect 9:16
```

**What you learn**: Different platforms need different dimensions.

---

### Use Case 7: Editing Existing Images

**Goal**: Modify a previously generated image.

First, create an image:
```bash
uv run python main.py uc7_original.png "A rocket ship emoji style icon on black background"
```

Then edit it:
```bash
uv run python main.py uc7_edited.png "Replace the rocket with a checkered racing flag, keep everything else the same" --edit uc7_original.png
```

**What you learn**: You can modify specific parts of images without regenerating everything.

---

### Use Case 8: Using Reference Images for Consistency

**Goal**: Create new images that match an existing style.

First, create a reference:
```bash
uv run python main.py uc8_reference.png "A blue glass 3D star on black background"
```

Then create matching images:
```bash
uv run python main.py uc8_heart.png "A heart shape in the exact same style" --ref uc8_reference.png
```

```bash
uv run python main.py uc8_moon.png "A crescent moon in the exact same style" --ref uc8_reference.png
```

**What you learn**: Reference images help maintain visual consistency across a set.

---

### Use Case 9: Creating App Icons

**Goal**: Generate professional-looking app icons.

```bash
uv run python main.py uc9_app_icon.png "A modern, minimalist app icon for a music streaming service. Gradient from purple to blue, simple geometric shapes, clean design suitable for iOS and Android" --aspect 1:1
```

**What you learn**: Detailed prompts produce more professional results.

**Pro tip**: Avoid gradients if you plan to edit the image later (they degrade with edits).

---

### Use Case 10: Creating Social Media Graphics

**Goal**: Generate images sized for social media.

**Twitter/X Header (3:1):**
```bash
uv run python main.py uc10_twitter.png "Abstract colorful wave pattern, modern and dynamic" --aspect 21:9
```

**Instagram Post (1:1):**
```bash
uv run python main.py uc10_instagram.png "Aesthetic flat lay of coffee cup, notebook, and plant from above" --aspect 1:1
```

**Pinterest Pin (2:3):**
```bash
uv run python main.py uc10_pinterest.png "Inspiring quote background with soft pastel colors and geometric shapes" --aspect 4:5
```

---

### Use Case 11: Creating Product Mockups

**Goal**: Generate product visualization images.

```bash
uv run python main.py uc11_product.png "A sleek smartphone floating at an angle, showing a colorful app screen, soft shadows, gradient background from light gray to white, professional product photography style"
```

**What you learn**: AI can create realistic product mockups for presentations.

---

### Use Case 12: Creating a Complete Icon Set

**Goal**: Combine everything you've learned to create a professional icon set.

**Step 1**: Create a custom style file (or use the existing one):
```bash
uv run python main.py uc12_icons.png "settings gear" "user profile" "home house" "search magnifying glass" "notification bell" --style styles/blue_glass_3d.md --aspect 1:1
```

**Output**: Five consistent icons ready for your app!

- `uc12_icons_1.png` - Settings
- `uc12_icons_2.png` - Profile
- `uc12_icons_3.png` - Home
- `uc12_icons_4.png` - Search
- `uc12_icons_5.png` - Notifications

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Basic generation | `uv run python main.py out.png "prompt"` |
| With style | `uv run python main.py out.png "prompt" --style styles/file.md` |
| Edit image | `uv run python main.py out.png "changes" --edit input.png` |
| Reference style | `uv run python main.py out.png "prompt" --ref ref.png` |
| Multiple prompts | `uv run python main.py out.png "a" "b" "c"` |
| Landscape | `uv run python main.py out.png "prompt" --aspect 16:9` |
| Portrait | `uv run python main.py out.png "prompt" --aspect 9:16` |

---

## What's Next?

Now that you've mastered the basics:

1. **Read the [User Guide](USER_GUIDE.md)** for detailed explanations
2. **Create your own style files** - See `styles/blue_glass_3d.md` for the format
3. **Experiment with prompts** - More detail usually means better results
4. **Check [Troubleshooting](TROUBLESHOOTING.md)** if you run into issues

---

## Tips for Better Results

1. **Be descriptive**: "A red sports car" vs "A shiny red Ferrari 458 Italia, studio lighting, black background, high detail"

2. **Specify the style**: "cartoon", "photorealistic", "minimalist", "3D rendered", "flat design"

3. **Mention the background**: Always specify if you want a particular background color or style

4. **Use reference images**: For consistent sets, always use `--ref` with your best image

5. **Avoid gradients for editable images**: Solid colors work better for iterative editing

---

**Congratulations!** You now know how to use Nano Banana effectively. Happy creating!
