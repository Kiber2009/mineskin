import numpy as np


def is_region_fully_transparent_np(image, box):
    if image.mode not in ("RGBA", "LA", "PA"):
        return False

    region = image.crop(box)
    arr = np.array(region)

    if region.mode == "RGBA":
        alpha_channel = arr[:, :, 3]
    else:
        alpha_channel = arr[:, :, 1]

    return np.all(alpha_channel == 0)


def check_regions_transparency(image, boxes):
    return all(is_region_fully_transparent_np(image, box) for box in boxes)
