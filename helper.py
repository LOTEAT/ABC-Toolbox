import argparse
from images import image_helper
from files import file_helper
from spiders import spider_helper

def helper():
    parser = argparse.ArgumentParser(
                    prog='ABCToolbox',
                    description='ABCToolbox')
    subparser = parser.add_subparsers(help='for different toolbox')
    image_helper(subparser)
    file_helper(subparser)
    spider_helper(subparser)
    args = parser.parse_args()
    print(args)
    return args
    