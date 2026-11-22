# mineskin

Simple Python library to work with Minecraft skins

# Installation

Install `mineskin` from PyPI using your favorite package manager

- `pip install mineskin`
- `uv add mineskin`
- `poetry add mineskin`

# Usage

```python
from PIL import Image

# Import library
import mineskin
from mineskin.skin_types.abc import MinecraftSkinFormat

# Read skin from file
with Image.open("path/to/skin.png") as img:
    img.load()
    
    skin = mineskin.skin(img)
    
    # Check skin information
    print(f"{skin.format=}")
    print(f"{skin.slim=}")
    print(f"{skin.has_overlay=}")

    # Optimize skin (will mutate img object)
    skin.optimize(keep_ears=False)
    
    # Convert skin to old (before 1.8) format
    # This operation will create new Image object
    legacy_skin = skin.convert(MinecraftSkinFormat.LEGACY)

    # Save the result
    legacy_skin.image.save("path/to/result.png")
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