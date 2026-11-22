from typing import Any

from PIL import ImageDraw, Image

from mineskin.skin_types.abc import MinecraftSkin, MinecraftSkinFormat
from mineskin.utils import check_all_regions_transparency


class MinecraftSkinV1_8(MinecraftSkin):  # type: ignore[pep8-naming]
    def __init__(self, img: Image.Image) -> None:
        self._img = img

    @property
    def image(self) -> Image.Image:
        return self._img

    @property
    def format(self) -> MinecraftSkinFormat:
        return MinecraftSkinFormat.V1_8

    @property
    def slim(self) -> bool:
        return check_all_regions_transparency(
            self._img,
            (
                # Right arm
                (50, 16, 52, 20),
                (54, 20, 56, 32),
                # Left arm
                (42, 48, 44, 52),
                (46, 52, 48, 64),
            ),
        )

    @property
    def has_overlay(self) -> bool:
        return not check_all_regions_transparency(
            self._img,
            (
                # Head
                (40, 0, 56, 8),
                (32, 8, 64, 16),
                # Right leg top
                (4, 32, 12, 36),
                # Body top
                (20, 32, 36, 36),
                # Right arm top
                (44, 32, 52, 36),
                # Other parts of (Right leg + Body + Rigth arm)
                (0, 36, 56, 48),
                # Left leg
                (4, 48, 12, 52),
                (0, 52, 16, 64),
                # Left arm
                (52, 48, 60, 52),
                (48, 52, 64, 64),
            ),
        )

    def optimize(self, keep_ears: bool = False) -> None:
        draw = ImageDraw.Draw(self._img)
        draw.rectangle((0, 0, 7, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle((56, 0, 63, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle((0, 16, 3, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle(
            (12, 16, 19, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (36, 16, 43, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (52, 16, 55, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle((0, 32, 3, 35), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle(
            (12, 32, 19, 35), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (36, 32, 43, 35), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (52, 32, 55, 35), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle((0, 48, 3, 51), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle(
            (12, 48, 19, 51), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (28, 48, 35, 51), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (44, 48, 51, 51), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (60, 48, 63, 51), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (56, 16, 63, 47), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        if keep_ears:
            draw.rectangle(
                (24, 0, 24, 0), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
            draw.rectangle(
                (37, 0, 37, 0), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
            draw.rectangle(
                (24, 7, 37, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
            draw.rectangle(
                (38, 0, 39, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
        else:
            draw.rectangle(
                (24, 0, 39, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )

    def convert(
        self,
        fmt: MinecraftSkinFormat,
        use_left_arm: bool = False,
        use_left_leg: bool = False,
        **kwargs: Any,
    ) -> MinecraftSkin:
        from mineskin.skin_types.legacy import LegacyMinecraftSkin

        match fmt:
            case MinecraftSkinFormat.V1_8:
                return MinecraftSkinV1_8(self._img.copy())
            case MinecraftSkinFormat.LEGACY:
                if not (use_left_leg or use_left_arm):
                    return LegacyMinecraftSkin(self._img.crop((0, 0, 64, 32)))
                img = Image.new("RGBA", (64, 32), (0, 0, 0, 0))
                img.paste(self._img.crop((0, 0, 64, 16)), box=(0, 0))
                img.paste(self._img.crop((16, 16, 40, 32)), box=(16, 16))
                if use_left_arm:
                    img.paste(self._img.crop((16, 48, 32, 64)), box=(0, 16))
                else:
                    img.paste(self._img.crop((0, 16, 16, 32)), box=(0, 16))
                if use_left_leg:
                    img.paste(self._img.crop((32, 48, 48, 64)), box=(40, 16))
                else:
                    img.paste(self._img.crop((40, 16, 56, 32)), box=(40, 16))
                return LegacyMinecraftSkin(img)
            case _:
                raise NotImplementedError(f"Unsupported skin format: {fmt}")


__all__ = ("MinecraftSkinV1_8",)
