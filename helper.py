import argparse
from images import image_helper

def helper():
    parser = argparse.ArgumentParser(
                    prog='ABCToolbox',
                    description='ABCToolbox')
    parser.add_argument('boxname', type=str)
    parser = image_helper(parser)
    args = parser.parse_args()
    return args
    