from files import FileBox

def _collect_images(path):
    img_exts = ['jpeg', 'jpg', 'png']
    return FileBox(path, img_exts)