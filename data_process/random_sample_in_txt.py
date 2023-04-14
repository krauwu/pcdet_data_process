import os
import random

def imageset_gene():
    target_folder = "/home/liuyang/data_process/npy/"
    files = os.listdir(target_folder)
    random_files = random.sample(files, 4)
    unselected_files = list(set(files) - set(random_files))
    with open("val.txt", "w") as f:
        for file in random_files:
            name, ext = os.path.splitext(file)
            f.write(name + "\n")
    with open("train.txt", "w") as f:
        for file in unselected_files:
            name, ext = os.path.splitext(file)
            f.write(name + "\n")
