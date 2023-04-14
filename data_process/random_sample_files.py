import os
import random
import shutil

destination_dir = "/home/liuyang/SUSTechPOINTS/data/example/sample/"
path = "/home/liuyang/SUSTechPOINTS/data/example/lidar/"
files = os.listdir(path)
random_files = random.sample(files, 200)
for file in random_files:
    source_path = path + file
    destination_path = destination_dir + file
    shutil.move(source_path, destination_path)

