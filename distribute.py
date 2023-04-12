from images import ImageBox

def distribute_tasks(args):
    if args.toolbox == 'image':
        box = ImageBox(args)
    
    box.process()