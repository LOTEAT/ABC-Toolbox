import requests
from contextlib import closing
import requests, os

# def _download_video(url, save_path):
#     try:
#         res = requests.get(url, stream=True)
#         with open(save_path, 'wb') as f:
#             for chunk in res.iter_content(chunk_size=10240):
#                 f.write(chunk)
#         return True
#     except:
#         return False
    

def _download_video(url, save_path):
    try:
        video_name = os.path.basename(save_path)
        with closing(requests.get(url, timeout=10, verify=False, stream=True)) as response:
            chunk_size = 1024                                              
            content_size = int(response.headers['content-length'])         
            data_count = 0                                                
            with open(save_path, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    done_block = int((data_count / content_size) * 50)    
                    data_count = data_count + len(data)                  
                    now_jd = (data_count / content_size) * 100     
                    print("\r %s [%s%s] %d%% " % (video_name + "  ---->  ", done_block * '█', ' ' * (50 - 1 - done_block), now_jd), end=" ")
            print('\n')
        return True
    except:
        return False

