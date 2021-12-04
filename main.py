import uuid

from argparse import ArgumentParser

from data import collector
from data import processor

# default paths
JSON_FILE_PATH = "./data/data.json"
OUTPUT_DIRECTORY_PATH = "./data/output"


def parse_data():
    data_collector = collector.DataCollector()

    data_collector.parse_json(JSON_FILE_PATH)
    data_collector.get_images()
    data_collector.map_data()

    return data_collector.mapped_data


def main():
    parser = ArgumentParser(description="Generate a batch of images with set rules.")

    parser.add_argument("amount", type=int, default=1000, help="the amount of images to be created")
    parser.add_argument("--debug", "-d", dest="debug", action="store_true", default=False,
                        help="show some extra debug information")
    parser.add_argument("--random", "-r", dest="random", action="store_true", default=False,
                        help="randomizes the creation of images")
    parser.add_argument("--counter", "-c", dest="counter", action="store_true", default=False,
                        help="names the images by order of generation")
    parser.add_argument("--size", "-s", dest="size", type=int, default=(500, 500), nargs="+",
                        help="set the width and height of the images")

    args = parser.parse_args()

    if args.amount <= 0:
        raise ValueError("Positional argument amount can not be negative or 0")

    if len(args.size) != 2:
        raise ValueError("Optional argument size must be a tuple of length 2")

    data = parse_data()
    image_processor = processor.ImageProcessor(args.size, data, args.debug)

    if args.random:
        images = image_processor.generate_random_images(args.amount)
    else:
        images = image_processor.generate_images(args.amount)

    image_counter = 0
    for image in images:
        try:
            image.save(f"{OUTPUT_DIRECTORY_PATH}/{image_counter if args.counter else uuid.uuid4()}.png")
            image_counter += 1
        except ValueError:
            print("Output format could not be determined.")
            raise ValueError
        except OSError:
            print("File could not be written.")
            raise OSError

    print(f"{image_counter} images have been generated.")


if __name__ == "__main__":
    main()