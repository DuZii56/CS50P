from PIL import Image, ImageOps
import sys

def main():
    if sys.argv[2][-3] != sys.argv[1][-3]:
        sys.exit(1)
    with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt:
        img = ImageOps.fit(img, shirt.size)
        img.paste(shirt, (0,0), mask=shirt)
        img.save(sys.argv[2])

main()
