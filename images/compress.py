import cv2

def img_compress(in_path, out_path, ratio=85):
    img=cv2.imread(in_path, 1)
    cv2.imwrite(out_path, img, [cv2.IMWRITE_JPEG_QUALITY, ratio])
