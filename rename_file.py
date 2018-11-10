import os
import string
def rename_files():
    #(1)get file names from a folder
    file_list = os.listdir(r"/Users/lihangen/PycharmProjects/untitled2/prank")
    #(2) for each file , rename filename
    saved_path = os.getcwd()
    os.chdir(r'/Users/lihangen/PycharmProjects/untitled2/prank')
    for file_name in file_list:
        os.rename(file_name,file_name.strip('0123456789'))
    os.chdir(saved_path)


rename_files()