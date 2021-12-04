import json
import copy

from PIL import Image


class DataCollector:

    def __init__(self):
        self.parsed_json = None
        self.images_list = []
        self.mapped_data = None

    def parse_json(self, file_name: str) -> None:
        try:
            with open(file_name, "r") as json_file:
                self.parsed_json = json.load(json_file)
        except IOError:
            print(f"OS error occurred with {file_name}.")
            raise IOError
        except json.JSONDecodeError:
            print(f"Failed to decode {file_name}, not valid JSON.")
            raise json.JSONDecodeError

    def get_images(self) -> None:
        if self.parsed_json is None:
            raise ValueError("PARSED_JSON object is null.")

        image_locations = []
        for key in self.parsed_json:
            values = self.parsed_json[key]
            for value in values:
                image_location = value["location"]
                image_locations.append(image_location)

        for location in image_locations:
            # lazy loading, image data is not read
            self.images_list.append(Image.open(location, "r").convert("RGBA"))

    def map_data(self) -> None:
        if self.parsed_json is None:
            raise ValueError("PARSED_JSON object is null.")

        if not self.images_list:
            raise ValueError("IMAGE_LIST object is empty.")

        index_counter = 0
        # shallow copies are not useful here
        self.mapped_data = copy.deepcopy(self.parsed_json)

        for key in self.mapped_data:
            values = self.mapped_data[key]
            for value in values:
                image = self.images_list[index_counter]
                value["image"] = image
                index_counter += 1
