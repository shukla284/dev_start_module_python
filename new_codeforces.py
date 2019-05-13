import re
import os
import fnmatch as fnm


def find_highest_number_file(path, pattern):
    file_list = fnm.filter(os.listdir(path), pattern)
    max_name = 0
    for file_name in file_list:
        num = re.findall("\d+", file_name)[0]
        max_name = max(int(num), max_name)
    return max_name


def create_file():
    path = "C:\\Users\\hp\\Desktop\\shukla\\cpp"
    pattern = "cf*.cpp"
    high_num = find_highest_number_file(path, pattern)+1
    print("Found the highest number file with "+str(high_num))
    print('Creating codeforces file with handle cf' + str(high_num) + ".cpp")
    return 'cf'+str(high_num)+'.cpp'

