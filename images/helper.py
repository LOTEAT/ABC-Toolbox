import argparse

def image_helper(parser):
    parser.add_argument('function', type=str)
    parser.add_argument('--ratio', type=int, default=85)
    return parser