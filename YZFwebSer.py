# -*- coding: utf-8 -*-
#  @Author: yuzhuofan
#  @Date: 2020-09-26 22:08:25
#  @Last Modified by:   yuzhuofan
#  @Last Modified time: 2020-09-26 22:08:25


from typing import List
from fastapi.params import Form
from fastapi.responses import StreamingResponse
from starlette.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI, UploadFile, File

import YZF_mysql_pyserver
import YZF_vedio


# 导入第三方库来处理
from starlette.requests import Request
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')

# 主页


@app.get("/")
async def root1(request: Request):
    return templates.TemplateResponse('/index.html',
                                      {'request': request})


@app.get("/yuzhuofan/")
async def root(request: Request):
    return templates.TemplateResponse('/index.html',
                                      {'request': request})

# 获取视频


@app.get("/vedio/{vedio_name}")
async def vedio(vedio_name: str):
    some_file_path = "./static/vedio/"+str(vedio_name)
    file_like = open(some_file_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")


@app.get('/yuzhuofan/shipin.html')
async def shipin1(request: Request, vedio_list: str):
    """
    docstring
    """
    return templates.TemplateResponse('/shipin.html',
                                      {'request': request,
                                       'vedio_list': vedio_list})


# 上传视频


@app.get("uploadFile.html")
async def upload(request: Request, username: str):
    """
    docstring
    """
    return templates.TemplateResponse('/uploadFile.html',
                                      {'request': request,
                                       'username': username, })


@app.get("/yuzhuofan/uploadFile")
async def uploadyzf(request: Request,
                    username: str = Form(...),):
    return templates.TemplateResponse('/uploadFile.html',
                                      {'request': request,
                                       'username': username, })


@app.post("/uploadfile/")
async def create_upload_file(request: Request,
                             files: List[UploadFile] = File(...),
                             username: str = Form(...),):
    '''
    返回成功上传的文件名列表
    '''
    vedio_list = YZF_vedio.vedio().vedio_list()
    for item in files:
        contents = await item.read()
        # 检测文件类型是否为MP4格式
        if item.content_type == "video/mp4":
            file_link = "./static/vedio/" + str(item.filename)
            with open(file_link, 'wb') as f:
                f.write(contents)
        else:
            # 返回0表示错误
            return templates.TemplateResponse("/main.html",
                                              {'request': request,
                                               'username': username,
                                               'filenames': '上传文件类型并非MP4文件！',
                                               'vedio_list': vedio_list})

    return templates.TemplateResponse("/main.html",
                                      {'request': request,
                                       "filenames": [file.filename for file in files],
                                       'username': username,
                                       "content_type": [file.content_type for file in files],
                                       'vedio_list': vedio_list})


# 登录部分


@app.post('/yuzhuofan/login')
def login(request: Request,
          username: str = Form(...),
          password: str = Form(...)):
    print('用户的输入为：')
    print('username', username)
    print("password", password)

    res = YZF_mysql_pyserver.yzf_user().select_Database(username=username)

    if res != 0:
        for Item in res:
            if Item.password == password:
                vedio_list = YZF_vedio.vedio().vedio_list()
                return templates.TemplateResponse("/main.html",
                                                  {'request': request,
                                                   'username': username,
                                                   'vedio_list': vedio_list})
        print("登录错误！")
        return templates.TemplateResponse("/index.html",
                                          {'request': request,
                                           'error': '用户名或密码错误'})
    else:
        print("登录错误！")
        return templates.TemplateResponse("/index.html",
                                          {'request': request,
                                           'error': '用户名或密码错误'})


if __name__ == '__main__':
    uvicorn.run(app=app,
                host="127.0.0.1",
                port=12345,
                workers=1)
