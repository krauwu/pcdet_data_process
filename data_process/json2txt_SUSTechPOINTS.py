import json
import os

'''if you use SUSTechPOINTS to tagging, this can change your label file's format'''
def json_to_txt():
    folder_path = "/home/liuyang/data_process/json2txt/"    # please change it to you root path
    file_names = os.listdir(folder_path)
    save_path = "/home/liuyang/data_process/labels/"

    for _, file_name in enumerate(file_names):
        with open(f'{folder_path+file_name}', 'r') as fcc_file:
            fcc_data = json.load(fcc_file)
            with open(f'{save_path + os.path.splitext(file_name)[0]}.txt', "w") as file_txt:
                for box_dict in fcc_data:
                    line = str(box_dict['psr']['position']['x']) + ' ' + str(box_dict['psr']['position']['y']) \
                           + ' ' + str(box_dict['psr']['position']['z']) + ' ' + str(box_dict['psr']['scale']['x']) \
                           + ' ' + str(box_dict['psr']['scale']['y']) + ' ' + str(box_dict['psr']['scale']['z']) \
                           + ' ' + str(box_dict['psr']['rotation']['z']) + ' ' + box_dict['obj_type']
                    file_txt.write(line + "\n")
