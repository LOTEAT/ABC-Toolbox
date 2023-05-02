from box import Box
import os.path as osp
import csv
import os
from .download import _download_video

class SpiderBox(Box):
    def __init__(self, args):
        super(SpiderBox, self).__init__()
        self.args = args
    
    def process(self):
        if self.args.function == 'download_video':
            self.download_video(self.args.i, self.args.o)
    
    def _download_video(self, resources, out_dir):
        for resource in resources:
            url, name = resource['url'], resource['name']
            save_path = osp.join(out_dir, name)
            is_success = _download_video(url, save_path)
            if is_success:
                self.logger.info(f"Download video {name} successfully!")
            else:
                self.logger.error(f"Download video {name} failed!")
            self.logger.info(f"Done!")
    
    def download_video(self, in_path, out_path=None):
        if not (osp.exists(out_path) or osp.exists(in_path)):
            raise ValueError(f"No such file or directory {in_path} or {out_path}")
        with open(in_path, "r", encoding = "utf-8") as f:
            reader = csv.DictReader(f)
            resources = [row for row in reader]
        if not out_path:
            out_path = 'temp_download'
        os.makedirs(out_path, exist_ok=True)
        self._download_video(resources, out_path)
        
                
                
            
            