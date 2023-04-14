import numpy as np
np.set_printoptions(suppress=True)
# 作用是取消numpy默认的科学计数法，测试表明open3d点云读取函数没法读取科学计数法的表示
import open3d as o3d
# data = np.load('001056.npy')
# txt_data = np.savetxt('2.txt', data)
pcd = o3d.io.read_point_cloud('1.txt', format='xyz')

print(pcd)
o3d.visualization.draw_geometries([pcd], width=1200, height=600) # 可视化点云

