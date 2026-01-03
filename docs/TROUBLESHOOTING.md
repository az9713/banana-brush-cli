# Troubleshooting Guide

Solutions for common problems when using Nano Banana. Find your error message or symptom below.

---

## Table of Contents

1. [Installation Problems](#installation-problems)
2. [API Key Issues](#api-key-issues)
3. [Generation Errors](#generation-errors)
4. [Image Quality Issues](#image-quality-issues)
5. [File and Path Problems](#file-and-path-problems)
6. [Performance Issues](#performance-issues)
7. [Platform-Specific Issues](#platform-specific-issues)
8. [Error Message Reference](#error-message-reference)

---

## Installation Problems

### "uv: command not found" or "'uv' is not recognized"

**Problem**: UV package manager is not installed or not in your PATH.

**Solution**:

1. Install UV:
   ```bash
   # Mac/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Restart your terminal (close and reopen)

3. Verify installation:
   ```bash
   uv --version
   ```

**If still not working**:
- On Windows: The installer might have added UV to a different PATH. Search for "uv.exe" and add its folder to your system PATH
- On Mac/Linux: Add `source $HOME/.cargo/env` to your shell profile

---

### "python: command not found" or Python version too old

**Problem**: Python 3.10+ is not installed or not in PATH.

**Solution**:

1. Check if Python is installed:
   ```bash
   python --version
   # or
   python3 --version
   ```

2. If not installed, download from https://www.python.org/downloads/

3. **Windows users**: During installation, CHECK "Add Python to PATH"

4. If installed but wrong version, install a newer version alongside

---

### "uv sync" fails with dependency errors

**Problem**: Dependencies can't be resolved.

**Solutions**:

1. **Clear UV cache**:
   ```bash
   uv cache clean
   uv sync
   ```

2. **Update UV**:
   ```bash
   # Reinstall UV
   curl -LsSf https://astral.sh/uv/install.sh | sh
   uv sync
   ```

3. **Check Python version**:
   ```bash
   python --version
   # Must be 3.10 or higher
   ```

4. **Delete and recreate environment**:
   ```bash
   rm -rf .venv
   uv sync
   ```

---

### "ModuleNotFoundError: No module named 'google'"

**Problem**: Dependencies weren't installed properly.

**Solution**:

1. Make sure you're in the project directory:
   ```bash
   cd path/to/nano-banana
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run with `uv run`:
   ```bash
   uv run python main.py ...
   ```

   **Important**: Don't just run `python main.py` — use `uv run python main.py`

---

## API Key Issues

### "Error: GOOGLE_API_KEY environment variable not set"

**Problem**: The API key isn't configured in your environment.

**Solutions**:

**Temporary (current session only)**:
```bash
# Windows Command Prompt
set GOOGLE_API_KEY=your-api-key-here

# Windows PowerShell
$env:GOOGLE_API_KEY="your-api-key-here"

# Mac/Linux
export GOOGLE_API_KEY="your-api-key-here"
```

**Permanent**:

*Windows*:
1. Press `Win + R`, type `sysdm.cpl`, press Enter
2. Click "Advanced" → "Environment Variables"
3. Under "User variables", click "New"
4. Name: `GOOGLE_API_KEY`, Value: your key
5. Click OK, restart terminal

*Mac/Linux*:
1. Open `~/.bashrc` or `~/.zshrc` in a text editor
2. Add: `export GOOGLE_API_KEY="your-api-key-here"`
3. Save and run `source ~/.bashrc` (or restart terminal)

---

### "API Error: 401 Unauthorized" or "Invalid API key"

**Problem**: Your API key is incorrect or expired.

**Solutions**:

1. **Verify your key**:
   - Go to https://aistudio.google.com/apikey
   - Check if your key is listed and active
   - If not, create a new one

2. **Check for typos**:
   - API keys are case-sensitive
   - No extra spaces before/after
   - No quotation marks in the value itself

3. **Verify it's set correctly**:
   ```bash
   # Windows
   echo %GOOGLE_API_KEY%

   # Mac/Linux
   echo $GOOGLE_API_KEY
   ```

4. **Try a fresh key**:
   - Delete the old key in Google AI Studio
   - Create a new one
   - Update your environment variable

---

### "API Error: 403 Forbidden" or "Quota exceeded"

**Problem**: You've hit your API usage limit.

**Solutions**:

1. **Wait**: Free tier limits reset periodically (usually daily)

2. **Check your quota**:
   - Go to https://aistudio.google.com/
   - Check your usage statistics

3. **Reduce usage**:
   - Generate fewer images
   - Use simpler prompts
   - Avoid rapid repeated requests

4. **Upgrade**: Consider a paid plan for higher limits

---

## Generation Errors

### "API Error: 400 Bad Request"

**Problem**: The API rejected your request.

**Possible causes and solutions**:

1. **Prompt too long**:
   - Shorten your prompt
   - Reduce style file content

2. **Invalid aspect ratio**:
   - Use only supported ratios: 1:1, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

3. **Invalid model name**:
   ```bash
   # Use a valid model
   --model gemini-2.5-flash-preview-native-audio-dialog
   ```

4. **Problematic content**:
   - The prompt may contain content the API refuses to generate
   - Rephrase your prompt

---

### "Failed to generate image for: [prompt]"

**Problem**: The API returned a response but no image.

**Solutions**:

1. **Check your prompt**:
   - Is it too vague? Add more detail
   - Is it requesting something problematic? Rephrase
   - Does it contradict itself?

2. **Try a simpler prompt**:
   ```bash
   uv run python main.py test.png "A blue square"
   ```

3. **Check the console output**:
   - There may be a text message explaining why

4. **Try without style**:
   ```bash
   # Remove --style to see if that's the issue
   uv run python main.py test.png "Your prompt"
   ```

---

### "API Error: 429 Too Many Requests"

**Problem**: You're making requests too quickly.

**Solutions**:

1. **Wait and retry**: Wait 30-60 seconds between requests

2. **Slow down batch processing**: Don't run multiple instances simultaneously

3. **Check for loops**: Make sure your script isn't retrying infinitely

---

### Request times out or takes forever

**Problem**: Network issues or very complex requests.

**Solutions**:

1. **Check internet connection**

2. **Try a simpler prompt**

3. **Reduce image complexity**:
   - Avoid very detailed scenes
   - Use shorter prompts

4. **Try later**: API may be under heavy load

---

## Image Quality Issues

### Generated image looks different than expected

**Problem**: AI interpretation doesn't match your vision.

**Solutions**:

1. **Be more specific**:
   ```bash
   # Instead of:
   "A dog"

   # Try:
   "A golden retriever puppy sitting on green grass, sunny day, photorealistic style"
   ```

2. **Specify style explicitly**:
   - Add: "in cartoon style", "photorealistic", "minimalist", "3D rendered"

3. **Describe composition**:
   - "centered in frame"
   - "close-up view"
   - "wide angle shot"

4. **Iterate**: Generate multiple times with refined prompts

---

### Image has artifacts or is low quality

**Problem**: Generation produced imperfect results.

**Solutions**:

1. **Avoid gradients**: Solid colors work better
   ```bash
   # Instead of:
   "gradient background from blue to purple"

   # Try:
   "solid dark blue background"
   ```

2. **Simpler compositions**: Fewer elements = better quality

3. **Try a different model** (if available)

4. **Regenerate**: Sometimes running the same prompt again produces better results

---

### Edited images look worse than originals

**Problem**: Quality degrades with each edit.

**Solutions**:

1. **Start with simple images**: Avoid complex originals

2. **Make fewer edits**: Each edit can reduce quality

3. **Add post-processing later**: Use Photoshop/Canva for gradients and text

4. **Keep originals**: Save your best unedited versions

---

### Text in images is garbled or wrong

**Problem**: AI-generated text is often imperfect.

**Solution**: Don't rely on AI for text generation
1. Generate the image without text
2. Add text using:
   - Canva (free, easy)
   - Photoshop
   - GIMP (free)
   - Any image editor

---

## File and Path Problems

### "Error: Style file not found: [path]"

**Problem**: The style file doesn't exist at the specified path.

**Solutions**:

1. **Check the path**:
   ```bash
   # Correct
   --style styles/blue_glass_3d.md

   # Wrong
   --style style/blue_glass_3d.md  # missing 's'
   --style blue_glass_3d.md        # missing folder
   ```

2. **Use full path if needed**:
   ```bash
   --style /full/path/to/styles/blue_glass_3d.md
   ```

3. **List available styles**:
   ```bash
   ls styles/
   # or on Windows:
   dir styles
   ```

---

### "Error: Image file not found: [path]"

**Problem**: The input image for `--edit` or `--ref` doesn't exist.

**Solutions**:

1. **Verify the file exists**:
   ```bash
   ls -la input.png
   # or on Windows:
   dir input.png
   ```

2. **Check file extension**: Make sure it matches exactly (.png vs .PNG)

3. **Use full path**: Avoid relative path issues
   ```bash
   --edit /Users/you/Downloads/input.png
   ```

---

### Output file not created

**Problem**: Command completes but no file appears.

**Solutions**:

1. **Check for error messages**: Look at the console output carefully

2. **Check the directory**:
   - Where did you specify the output?
   - Are you looking in the right folder?

3. **Verify generation succeeded**: Should see "Saved: filename.png"

4. **Check disk space**: Ensure you have space to save images

---

### "Permission denied" when saving

**Problem**: Can't write to the output location.

**Solutions**:

1. **Choose a writable location**:
   ```bash
   # Write to current directory
   uv run python main.py output.png "prompt"

   # Write to home directory
   uv run python main.py ~/output.png "prompt"
   ```

2. **On Mac/Linux**: Check folder permissions
   ```bash
   ls -la /path/to/folder
   ```

3. **On Windows**: Don't save to protected folders (Program Files, etc.)

---

## Performance Issues

### Generation is very slow

**Problem**: Each image takes a long time.

**Understanding**: This is often normal!
- AI image generation typically takes 3-15 seconds
- Complex prompts take longer
- Network speed affects transfer time

**Optimizations**:

1. **Use a faster model** (if available)
2. **Simplify prompts**
3. **Check internet speed**
4. **Avoid peak hours**

---

### High memory usage

**Problem**: System becomes slow during generation.

**Solutions**:

1. **Close other applications**

2. **Process fewer images at once**:
   ```bash
   # Instead of 10 at once:
   uv run python main.py out.png "a" "b" "c" ... "j"

   # Do smaller batches:
   uv run python main.py out1.png "a" "b" "c"
   uv run python main.py out2.png "d" "e" "f"
   ```

3. **Restart between large batches**

---

## Platform-Specific Issues

### Windows: Path issues with backslashes

**Problem**: Paths with backslashes cause problems.

**Solution**: Use forward slashes or raw strings:
```bash
# These both work:
--style styles/blue_glass_3d.md
--style "styles\\blue_glass_3d.md"
```

### Windows: PowerShell encoding issues

**Problem**: Special characters in prompts cause errors.

**Solution**: Use simple ASCII characters, or use Command Prompt instead of PowerShell.

### Mac: "Operation not permitted"

**Problem**: macOS security blocks the operation.

**Solutions**:

1. **Allow terminal access**:
   - System Preferences → Security & Privacy → Privacy → Full Disk Access
   - Add Terminal (or your terminal app)

2. **Use a different output location**

### Linux: Missing libraries

**Problem**: PIL/Pillow fails to load images.

**Solution**: Install system libraries:
```bash
# Ubuntu/Debian
sudo apt install libjpeg-dev libpng-dev

# Fedora
sudo dnf install libjpeg-devel libpng-devel

# Then reinstall Pillow
uv sync --reinstall
```

---

## Error Message Reference

Quick reference for common error messages:

| Error | Likely Cause | Quick Fix |
|-------|--------------|-----------|
| `GOOGLE_API_KEY not set` | Missing API key | Set environment variable |
| `401 Unauthorized` | Invalid API key | Check/regenerate API key |
| `403 Forbidden` | Quota exceeded | Wait or upgrade plan |
| `400 Bad Request` | Invalid request | Check prompt/parameters |
| `429 Too Many Requests` | Rate limited | Wait 60 seconds |
| `Style file not found` | Wrong path | Verify file exists |
| `Image file not found` | Wrong path | Verify file exists |
| `ModuleNotFoundError` | Missing dependencies | Run `uv sync` |
| `command not found: uv` | UV not installed | Install UV |
| `Permission denied` | Can't write file | Change output location |

---

## Still Stuck?

If none of these solutions work:

1. **Double-check the basics**:
   - Are you in the right directory?
   - Did you run `uv sync`?
   - Is your API key set?

2. **Try the simplest possible command**:
   ```bash
   uv run python main.py test.png "A red circle"
   ```

3. **Check for typos**: Copy-paste commands from documentation

4. **Restart fresh**:
   - Close all terminals
   - Open a new terminal
   - Navigate to the project
   - Set your API key
   - Try again

5. **Review documentation**:
   - [Quick Start Guide](QUICK_START.md)
   - [User Guide](USER_GUIDE.md)
   - [Developer Guide](DEVELOPER_GUIDE.md)

---

## Reporting Issues

If you've found a bug or have a feature request:

1. Note down:
   - Your operating system
   - Python version (`python --version`)
   - UV version (`uv --version`)
   - The exact command you ran
   - The complete error message

2. Check if it's a known issue (above)

3. Try to create a minimal reproduction case

---

This troubleshooting guide covers the most common issues. For additional help, refer to the other documentation files or search for your specific error message online.
