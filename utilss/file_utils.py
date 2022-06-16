"""
author :rain
Date : 2020/07/20
Description :文件操作
"""
import os

from constant import BASE_DIR


class FileUtils:

    @staticmethod
    def clear_file(file_path):
        """清空文件夹"""
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        fileList = os.listdir(file_path)
        # print(fileList)
        for i in range(len(fileList)):
            if fileList[i].endswith('.html'):
                os.remove(file_path + os.sep + fileList[i])

    @staticmethod
    def get_files():
        file_name = os.listdir(BASE_DIR + os.sep + "file")
        file_path = []
        for i in range(len(file_name)):
            file_path.append(BASE_DIR + os.sep + 'file' + os.sep + file_name[i])
        print(file_path)

        # with open(file_list[i], 'rb') as f:
        #     file = {'file': f}
        #     r = requests.post(url, headers=header1, files=file, timeout=50000)
        #     LogUtils.print_response(r, isformart=True)
        return file_path


if __name__ == '__main__':
    FileUtils.get_files()
