from helper import helper
from images import ImageBox
from files import FileBox
from box import Box

if __name__ == '__main__':
    args = helper()
    box = args.box(args)
    box.process()