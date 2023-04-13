from helper import helper
from images import ImageBox
from box import Box

if __name__ == '__main__':
    args = helper()
    if args.boxname == 'images':
        box = ImageBox(args)
    box.process()