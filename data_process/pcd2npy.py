import open3d as o3d
import numpy as np
import os

def pcd2npy():
    folder_path = "/home/liuyang/data_process/points/"   # please change it to you root path
    save_path = "/home/liuyang/data_process/npy/"
    file_names = os.listdir(folder_path)

    for i, file_name in enumerate(file_names):
        '''some lidar simu software only give xyz so we need to add other features to make the pcdet codes run'''
        pcd = o3d.io.read_point_cloud(f'{folder_path+file_name}')
        points = np.asarray(pcd.points)

        intense = np.zeros((points.shape[0], 1))

        np.save(f'{save_path+os.path.splitext(file_name)[0]}.npy', np.hstack((points, intense)))


