# Python Image Generator
Create images using a layered approach. An easy way to generate a batch of images.

**Dependencies**
```
Pillow
```

**Notes**

Keep in mind when processing a large amount of images it can take a while before your images are saved. It is advised to use debug mode when generating large batches. Place the images you want to use in the __images__ directory and the structure of your layering in the __data.json__ file. Output is done in the __output__ directory but can be changed in __main.py__ just like the path to the data file.

**Usage**
```
usage: main.py [-h] [--debug] [--random] [--counter] [--size SIZE [SIZE ...]]
               amount

Generate a batch of images with set rules.

positional arguments:
  amount                the amount of images to be created

optional arguments:
  -h, --help            show this help message and exit
  --debug, -d           show some extra debug information
  --random, -r          randomizes the creation of images
  --counter, -c         names the images by order of generation
  --size SIZE [SIZE ...], -s SIZE [SIZE ...]
                        set the width and height of the images
```
