import os
def rename_files():
    #(1)get file names from a folder
    file_list = os.listdir('./prank')
    #(2) for each file , rename filename
    for file_name in file_list:
        dele_number = file_name.translate(None,"0123456789")

        os.rename(file_name,dele_number)



rename_files()