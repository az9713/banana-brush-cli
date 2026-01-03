#!/usr/bin/env python3
"""
Nano Banana - Image Generation CLI for Claude Code

Generate and edit images using Google's Gemini API.

Usage:
    # Generate from prompt
    uv run python main.py output.png "A minimal 3D cube on solid black background"

    # Use a style template (reads prompt from .md file)
    uv run python main.py output.png "A gear icon" --style styles/blue_glass_3d.md

    # Generate multiple variations with style
    uv run python main.py output.png "cube" "sphere" "pyramid" --style styles/blue_glass_3d.md

    # Edit existing image
    uv run python main.py output.png "Change the background to blue" --edit input.png

    # Use reference images for style consistency
    uv run python main.py output.png "Same style but with a sphere" --ref style.png

    # Specify aspect ratio
    uv run python main.py output.png "Prompt" --aspect 16:9  # YouTube thumbnails

Aspect ratios: 1:1, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

# Load environment variables from .env file
load_dotenv()


def get_client() -> genai.Client:
    """Initialize Gemini client with API key from environment."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set", file=sys.stderr)
        print("Set it with: export GOOGLE_API_KEY='your-api-key'", file=sys.stderr)
        sys.exit(1)
    return genai.Client(api_key=api_key)


def load_style(style_path: str) -> str:
    """Load style description from markdown file."""
    path = Path(style_path)
    if not path.exists():
        print(f"Error: Style file not found: {style_path}", file=sys.stderr)
        sys.exit(1)
    return path.read_text(encoding="utf-8").strip()


def load_image(image_path: str) -> Image.Image:
    """Load image from file path."""
    path = Path(image_path)
    if not path.exists():
        print(f"Error: Image file not found: {image_path}", file=sys.stderr)
        sys.exit(1)
    return Image.open(path)


def build_prompt(user_prompt: str, style_content: str | None) -> str:
    """Build full prompt by combining style and user prompt."""
    if style_content:
        return f"{style_content}\n\nSubject: {user_prompt}"
    return user_prompt


def generate_image(
    client: genai.Client,
    prompt: str,
    model: str = "gemini-3-pro-image-preview",
    aspect_ratio: str = "1:1",
    edit_image: Image.Image | None = None,
    ref_image: Image.Image | None = None,
) -> Image.Image | None:
    """Generate or edit an image using Gemini API."""
    # Build contents list
    contents = []

    # Add reference/edit image if provided
    if edit_image:
        contents.append(edit_image)
        # Modify prompt to indicate editing
        prompt = f"Edit this image: {prompt}"
    elif ref_image:
        contents.append(ref_image)
        # Modify prompt to indicate reference
        prompt = f"Using this image as a style reference, create: {prompt}"

    # Add the text prompt
    contents.append(prompt)

    # Configure the request
    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
    )

    # Make the API call
    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=config,
        )
    except Exception as e:
        print(f"API Error: {e}", file=sys.stderr)
        return None

    # Extract image from response
    for part in response.parts:
        if part.inline_data is not None:
            return part.as_image()

    # Check if there's text response (might indicate why no image)
    for part in response.parts:
        if part.text:
            print(f"Model response: {part.text}")

    return None


def get_output_path(base_path: str, index: int, total: int) -> str:
    """Generate output path for multi-prompt generation."""
    if total == 1:
        return base_path

    path = Path(base_path)
    return str(path.parent / f"{path.stem}_{index}{path.suffix}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using Gemini API (Nano Banana)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("output", help="Output file path (e.g., output.png)")
    parser.add_argument("prompts", nargs="+", help="Image prompt(s)")
    parser.add_argument("--style", help="Style markdown file path")
    parser.add_argument("--edit", help="Input image to edit")
    parser.add_argument("--ref", help="Reference image for style consistency")
    parser.add_argument(
        "--aspect",
        default="1:1",
        choices=["1:1", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
        help="Aspect ratio (default: 1:1)",
    )
    parser.add_argument(
        "--model",
        default="gemini-3-pro-image-preview",
        choices=[
            "gemini-3-pro-image-preview",
            "gemini-2.5-flash-image",
            "imagen-4.0-generate-001",
        ],
        help="Image model to use (default: gemini-3-pro-image-preview)",
    )

    args = parser.parse_args()

    # Load style if provided
    style_content = None
    if args.style:
        style_content = load_style(args.style)
        print(f"Using style: {args.style}")

    # Load images if provided
    edit_image = None
    ref_image = None
    if args.edit:
        edit_image = load_image(args.edit)
        print(f"Editing image: {args.edit}")
    elif args.ref:
        ref_image = load_image(args.ref)
        print(f"Using reference: {args.ref}")

    # Initialize client
    client = get_client()

    # Generate images for each prompt
    total = len(args.prompts)
    for i, prompt in enumerate(args.prompts, 1):
        full_prompt = build_prompt(prompt, style_content)
        output_path = get_output_path(args.output, i, total)

        print(f"Generating ({i}/{total}): {prompt[:50]}...")

        image = generate_image(
            client=client,
            prompt=full_prompt,
            model=args.model,
            aspect_ratio=args.aspect,
            edit_image=edit_image,
            ref_image=ref_image,
        )

        if image:
            # Ensure output directory exists
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            image.save(output_path)
            print(f"Saved: {output_path}")
        else:
            print(f"Failed to generate image for: {prompt}", file=sys.stderr)


if __name__ == "__main__":
    main()
