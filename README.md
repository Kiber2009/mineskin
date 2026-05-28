# mineskin

Simple Python library for working with Minecraft skins

# Installation

Install `mineskin` from PyPI using your favorite package manager

- `pip install mineskin`
- `uv add mineskin`
- `poetry add mineskin`

# Usage

```python
# Import library
import mineskin

# Read skin from file
with mineskin.MinecraftSkin.open("path/to/skin.png") as skin:
    skin.load()

# Check skin information
print(skin.format)
print(skin.is_slim())
print(skin.has_overlay)

# Optimize skin
skin.optimize()

# Convert skin to old (before 1.8) format
old_skin = skin.convert(mineskin.MinecraftSkinFormat.OLD)

# Save the result
old_skin.save("path/to/result.png")
```

# Building from source

> [!WARNING]
> Make sure uv installed on your system

- Clone the repo:
  ```shell
  git clone https://github.com/Kiber2009/mineskin.git
  cd mineskin
  ```
- Build using uv
  ```shell
  uv build
  ```
- Distribution will be available in `dist` directory