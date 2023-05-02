from glob import glob
import os.path as osp
import requests

def download_video(url, save_path):
    res = requests.get(url, stream=True)
    with open(save_path, 'wb') as f:
        for chunk in res.iter_content(chunk_size=10240):
            f.write(chunk)
