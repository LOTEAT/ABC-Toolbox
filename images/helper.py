from .image_box import ImageBox

def image_helper(parser):
    img_parser = parser.add_parser('images')
    img_parser.set_defaults(box=ImageBox)
    img_parser.add_argument('function', type=str)
    img_parser.add_argument('-i', type=str)
    img_parser.add_argument('-o', type=str)
    img_parser.add_argument('--ratio', type=int, default=85)
    return parser