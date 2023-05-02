from .spider_box import SpiderBox

def spider_helper(parser):
    spider_parser = parser.add_parser('spider')
    spider_parser.set_defaults(box=SpiderBox)
    spider_parser.add_argument('function', type=str)
    spider_parser.add_argument('-i', type=str)
    spider_parser.add_argument('-o', type=str)
    return parser