import argparse
import time
from pathlib import Path

import cv2
import pymysql
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized
import data_operations as db
import detect as dt
import data_operations as db

if __name__=='__main__':
    path='D:\\ships_vision\\imgs\\100001047.bmp'
    if dt.already_exist(path):
        print("hello")
    else:
        opt = dt.parse_args(path)
        print(opt)
        check_requirements(exclude=('pycocotools', 'thop'))

        with torch.no_grad():
            if opt.update:  # update all models (to fix SourceChangeWarning)
                for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                    dt.detect(opt)
                    strip_optimizer(opt.weights)
            else:
                dt.detect(opt)