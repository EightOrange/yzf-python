import pymysql
from pydantic import BaseModel
from timeD import timeDT


class Light(BaseModel):
    '''
    light实体类
    '''
    id: int = None
    lighting: float = None
    time1: str = None


class Lighting:
    def insert(self, light1: Light()):
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
        print(light1)
        sql = "INSERT INTO light(lighting,time) VALUES (%s,%s)"
        print(sql)
        try:
            # 执行sql语句
            db.execute(sql, (light1.lighting, dt))
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
            db.execute("select * from light")
            # 将所有的查询结果放入结果集
            data_result = db.fetchall()
            # 实例化User类，并初始化集合

            list1 = []
            for row in data_result:
                light = Light()
                light.id = row[0]
                light.lighting = row[1]
                light.time1 = row[2]
                print("id=%s,light=%s,datetime=%s" %
                      (light.id, light.lighting, light.time1))
                # json_data=json.dumps(light, default = lambda obj: obj.__dict__)
                list1.append(light)

        except Exception:
            print("错误：无法获取数据")

        # 关闭数据库连接
        conn.close()
        return list1
