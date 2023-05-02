from box import Box
from glob import glob
import os.path as osp
import os
from files import convert

class FileBox(Box):
    def __init__(self, args):
        super(FileBox, self).__init__()
        self.args = args
    
    @staticmethod
    def get_ext(file):
        return osp.splitext(file)[-1][1:] 
    
    @staticmethod
    def get_pre(file):
        return osp.splitext(file)[0]
    
    @staticmethod
    def collect_files(path, file_exts):
        files = []
        for ext in file_exts:
            files.extend(glob(osp.join(path, "**", "*.{}".format(ext)), recursive=True))
        return files
        
     
    
    def process(self):
        if self.args.function == 'convert':
            self.convert(self.args.i, self.args.o, self.args.in_ext, self.args.out_ext)
            
            
    def _file_convert(self, in_paths, out_paths):
        for in_path, out_path in zip(in_paths, out_paths):
            in_ext, out_ext = self.get_ext(in_path), self.get_ext(out_path)
            func_name = f'_{in_ext}2{out_ext}'
            convert_func = getattr(convert, func_name)
            is_success = convert_func(in_path, out_path)
            if is_success:
                self.logger.info(f"Convert {in_path} to {out_path} successfully!")
            else:
                self.logger.error(f"Convert {in_path} to {out_path} failed!")
            self.logger.info(f"Done!")
        
    def convert(self, in_path, out_path, in_ext, out_ext):
        if not osp.exists(in_path):
            raise ValueError(f"No such file or directory {in_path}")
        
        if os.path.isdir(in_path) and (not in_ext or not out_ext):
            raise ValueError(f"You need to specify file extension.")
    
        if len(out_ext) > 1:
            raise ValueError("Out file extension must be one.")

        dir_name, file_name = osp.split(in_path)
        if not out_path:
            out_path = osp.join('temp_convert', file_name)
        
        if os.path.isfile(in_path):
            os.makedirs(dir_name, exist_ok=True)
            in_ext, out_ext = self.get_ext(in_path), self.get_ext(out_path)
            in_paths, out_paths = [in_path], [out_path]
        else:
            in_paths = self.collect_files(in_path, in_ext)
            out_paths = [path.replace(dir_name, out_path).replace('.' + self.get_ext(path), f'.{out_ext[0]}')  for path in in_paths]

        self._file_convert(in_paths, out_paths)