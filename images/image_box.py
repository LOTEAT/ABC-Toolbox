class ImageBox:
    def __init__(self, args):
        self.args = args
    
    def process(self):
        if self.args.function == 'compress':
            