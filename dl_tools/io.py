import glob
import os

import cv2
import numpy as np

IMAGES_EXTS = {".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG", ".webp", ".WEBP"}


def read_image_rgb_fp32(image_filename):
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype(np.float32) / 255.
    return image


def write_image_rgb(image, image_filename):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(image_filename, image)


def glob_images_filenames(root, images_exts=IMAGES_EXTS, recursive=True):
    filenames = []
    for ext in images_exts:
        filenames_ext = list(glob.glob(os.path.join(root, f"**/*{ext}"), recursive=recursive))
        filenames.extend(filenames_ext)
    return sorted(filenames)
