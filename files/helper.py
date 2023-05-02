from .file_box import FileBox

def file_helper(parser):
    file_parser = parser.add_parser('files')
    file_parser.set_defaults(box=FileBox)
    file_parser.add_argument('function', type=str)
    file_parser.add_argument('-i', type=str)
    file_parser.add_argument('-o', type=str)
    file_parser.add_argument('--in_ext', type=str, nargs='*')
    file_parser.add_argument('--out_ext', type=str, nargs='*')
    
    return parser