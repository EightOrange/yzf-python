# from GuangMinMysql import Light
import pymysql
from pydantic import BaseModel
import timeD
from timeD import timeDT
import json
# import GuangMinMysql


class Temp(BaseModel):
    '''
    temp实体类
    '''
    id: int = None
    temperature: float = None
    Humidity: float = None
    # light: float = None
    time1: str = None


class TEMPerature:
    def insert(self, temp1: Temp()):
        '''
        向数据库内增加记录
        '''
        # 打开数据库连接
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="yuzhuofan",
            database="for_python",
            charset="utf8",
        )
        # 获取连接下的游标
        db = conn.cursor()

        dt = timeDT()
        print(temp1)
        sql = "INSERT INTO temp(temperature,Humidity,time) VALUES (%s,%s,%s)"
        print(sql)
        try:
            # 执行sql语句
            db.execute(sql, (temp1.temperature, temp1.Humidity, dt))
            # 提交到数据库执行
            conn.commit()
        except Exception:
            # 如果发生错误则回滚
            print("Insert error!")
            conn.rollback()

        # 关闭数据库连接
        conn.close()

    def select(self):
        '''
        获取数据库内所有信息
        '''
        # 打开数据库连接
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="yuzhuofan",
            database="for_python",
            charset="utf8",
        )
        # 获取连接下的游标
        db = conn.cursor()
        try:
            # 执行sql语句
            db.execute("select * from temp")
            # 将所有的查询结果放入结果集
            data_result = db.fetchall()
            # 实例化User类，并初始化集合
            # lights = GuangMinMysql.Lighting().select()
            list1 = []
            # i = 0
            for row in data_result:
                temp = Temp()
                temp.id = row[0]
                temp.temperature = row[1]
                temp.Humidity = row[2]
                temp.time1 = row[3]
                # lit = lights[i]

                print("id=%s,temp=%s,Hum=%s,datetime=%s" %
                      (temp.id, temp.temperature, temp.Humidity, temp.time1))
                # else:
                #     temp.light = None
                #     print("id=%s,temp=%s,Hum=%s,datetime=%s" %
                #           (temp.id, temp.temperature, temp.Humidity, temp.time1))
                # i = i+1

                list1.append(temp)

        except Exception:
            print("错误：无法获取数据")

        # 关闭数据库连接
        conn.close()
        return list1
