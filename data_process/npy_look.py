import open3d as o3d
import numpy as np
import os

folder_path = "/home/liuyang/SUSTechPOINTS/data/scene1/lidar"   # please change it to you root path
file_names = os.listdir(folder_path)

pcd = o3d.io.read_point_cloud('/home/liuyang/SUSTechPOINTS/data/scene1/lidar/000002.pcd')
points = np.asarray(pcd.points)
intense = np.ones((points.shape[0], 1))
print(np.hstack((points, intense)).shape)
