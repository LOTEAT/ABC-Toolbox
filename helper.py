import argparse
from images import image_helper
from files import file_helper

def helper():
    parser = argparse.ArgumentParser(
                    prog='ABCToolbox',
                    description='ABCToolbox')
    subparser = parser.add_subparsers(help='for different toolbox')
    
    image_helper(subparser)
    

    # parser = file_helper(parser)
    # parser = image_helper(parser)
    args = parser.parse_args()
    print(args)
    return args
    