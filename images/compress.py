import cv2
from glob import glob
import os
import os.path as osp

def _img_compress(in_path, out_path, ratio=85):
    img=cv2.imread(in_path, 1)
    cv2.imwrite(out_path, img, [cv2.IMWRITE_JPEG_QUALITY, ratio])


def img_compress(in_path, out_path, ratio=85):
    assert isinstance(in_path, out_path), "Image compresses failed, because \
        input and output are not the same type. They are either images or folders"
    if not (osp.exists(out_path) or osp.exists(in_path)):
        raise ValueError(f"No such file or directory {in_path} or {out_path}")
    if os.path.isfile(in_path):
        dir_name = osp.split(out_path)[0]
        os.makedirs(dir_name, exist_ok=True)
        