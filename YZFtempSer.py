
from time import time
from starlette.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI, Response
from fastapi.params import Form
from fastapi.responses import JSONResponse
from GuangMinMysql import Light
import YZFtempMysql
from pydantic import BaseModel
import GuangMinMysql

# 导入第三方库来处理
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from YZFtempMysql import Temp


class Item(BaseModel):
    temperature: float = None
    Humidity: float = None
    lighting: float = None


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.post("/tempPOST")
async def mPost(request: Request, temperature: float, Humidity: float):
    """
    docstring
    """
    temp = Temp()
    temp.temperature = temperature
    temp.Humidity = Humidity
    YZFtempMysql.TEMPerature().insert(temp1=temp)
    return {'insert_result': 'it is ok!'}


@app.post("/tempPOSTjson")
async def qqq(request_data: Temp):
    """
    接收json格式的温湿度数据
    """
    print(request_data)
    YZFtempMysql.TEMPerature().insert(temp1=request_data)
    return {'insert_result': 'it is ok!'}


@app.get("/tempGET")
async def mGet(request: Request, response: Response):
    """
    docstring
    """
    result = YZFtempMysql.TEMPerature().select()

    print(result)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return result

if __name__ == '__main__':
    uvicorn.run(app=app,
                host="127.0.0.1",
                port=12345,
                workers=1)
