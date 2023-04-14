import open3d
import numpy as np
from visual_utils import open3d_vis_utils as V
import os

path = "/home/liuyang/pcdet/OpenPCDet/data/custom/gt_database/"
for filename in os.listdir(path):
    print(filename)
    points = np.fromfile(f'{path+filename}', dtype=np.float32).reshape(-1, 4)
    V.draw_scenes(points)

# path = "/home/liuyang/pcdet/OpenPCDet/data/custom/gt_database/001043_Car_0.bin"
# path = "/home/liuyang/pcdet/OpenPCDet/data/kitti/gt_database/000045_Car_3.bin"
#
# points = np.fromfile(f'{path}', dtype=np.float32).reshape(-1, 4)
# np.set_printoptions(threshold=np.inf)
# print(points.shape, points)
# V.draw_scenes(points)
