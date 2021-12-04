import itertools
import random

from io import BytesIO
from PIL import Image


class ImageProcessor:

    def __init__(self, image_size: tuple, data_map: dict, debug_mode: bool):
        # size in pixels
        self.image_size = image_size
        self.data_map = data_map
        self.debug_mode = debug_mode

    def generate_image(self, image_layout: tuple) -> Image:
        images = []

        print(f"Generating images using layout {image_layout}:") if self.debug_mode else None
        for index, value in enumerate(image_layout):
            _key = list(self.data_map)[index]
            image = self.data_map[_key][value]["image"]
            print(f"Generated {BytesIO(image.tobytes()).getbuffer()} for value {value}.") if self.debug_mode else None
            images.append(image)

        empty_image = Image.new("RGBA", self.image_size)
        for img in images:
            empty_image.paste(img, mask=img)

        print(f"Exporting object {empty_image.__repr__()}\n") if self.debug_mode else None
        return empty_image

    def generate_images(self, amount_maximum: int) -> list:
        if self.data_map is None:
            raise ValueError("DATA_MAP object is null.")

        restraints = []
        for key in self.data_map:
            value = self.data_map[key]
            restraints.append(range(0, len(value)))

        images = []
        all_combinations = list(itertools.product(*restraints))
        for index, combination in enumerate(all_combinations):
            if index == amount_maximum:
                break
            image = self.generate_image(combination)
            images.append(image)

        return images

    def generate_random_images(self, amount_maximum: int) -> list:
        if self.data_map is None:
            raise ValueError("DATA_MAP object is null.")

        restraints = []
        for key in self.data_map:
            value = self.data_map[key]
            restraints.append(len(value))

        random_combinations = []
        for number in range(0, amount_maximum):
            random_combination = []
            for restraint in restraints:
                random_combination.append(random.randint(0, restraint - 1))
            random_combinations.append(tuple(random_combination))

        images = []
        for index, combination in enumerate(random_combinations):
            if index == amount_maximum:
                break
            image = self.generate_image(combination)
            images.append(image)

        return images