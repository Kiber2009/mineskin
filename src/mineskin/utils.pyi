from collections.abc import Iterable

from PIL.Image import Image

def is_region_fully_transparent_np(
    image: Image,
    box: tuple[float, float, float, float],
) -> bool: ...
def check_all_regions_transparency(
    image: Image,
    boxes: Iterable[tuple[float, float, float, float]],
) -> bool: ...
def check_any_regions_transparency(
    image: Image,
    boxes: Iterable[tuple[float, float, float, float]],
): ...
