import os

'''rename your data's name as pcdet frame'''

folder_path = "/home/liuyang/uuv_ws/bag_files/pcd/" # please change it to you root path
file_names = os.listdir(folder_path)

for i, file_name in enumerate(file_names):
    new_file_name = '{:06d}.pcd'.format(i)

    if new_file_name == file_name:
        continue
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))