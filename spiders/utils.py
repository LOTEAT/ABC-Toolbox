from glob import glob
import os.path as osp

def collect_images(path):
    images = []
    images.extend(glob(osp.join(path, "**", "*.{}".format('jpeg')), recursive=True))
    images.extend(glob(osp.join(path, "**", "*.{}".format('png')), recursive=True))
    images.extend(glob(osp.join(path, "**", "*.{}".format('jpg')), recursive=True))
    return images