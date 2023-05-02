from box import Box
from glob import glob
import os
import os.path as osp
from .compress import _img_compress
from .utils import _collect_images


class ImageBox(Box):
    def __init__(self, args):
        super(ImageBox, self).__init__()
        self.args = args
    
    def process(self):
        if self.args.function == 'compress':
            self.img_compress(self.args.i, self.args.o, self.args.ratio)
    
    def _img_compress(self, in_path, out_path, ratio):
        is_success = _img_compress(in_path, out_path)
        if is_success:
            self.logger.info(f"Compress {in_path} to {out_path} successfully!")
        else:
            self.logger.error(f"Compress {in_path} to {out_path} failed!")
        self.logger.info(f"Done!")
            
    
    def img_compress(self, in_path, out_path=None, ratio=85):
        if not (osp.exists(out_path) or osp.exists(in_path)):
            raise ValueError(f"No such file or directory {in_path} or {out_path}")
        dir_name, file_name = osp.split(in_path)
        if not out_path:
            out_path = osp.join('temp_compressed', file_name)
        if os.path.isfile(in_path):
            os.makedirs(dir_name, exist_ok=True)
            self._img_compress(in_path, out_path, ratio)
        else:
            images = _collect_images(in_path)
            for img_path in images:
                _, file_name = osp.split(img_path)
                out_img_path = osp.join(out_path, file_name)
                self._img_compress(img_path, out_img_path, ratio)
                
                
            
            