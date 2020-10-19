import os


class vedio:

    def vedio_list(self):
        '''
        返回json类型的视频目录，显示具体视频文件名称
        '''
        file_name = os.listdir('./static/vedio')
        return file_name
