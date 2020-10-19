import pymysql
from pydantic import BaseModel


class User(BaseModel):
    '''
    User实体类，包括userid，username和password
    '''
    userid: int = None
    username: str = None
    password: str = None


class yzf_user:

    def select_All(self):
        '''
        获取数据库内所有信息
        无入参
        返回一个User类的集合
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
            db.execute("select * from yzf_user")
            # 将所有的查询结果放入结果集
            data_result = db.fetchall()
            # 实例化User类，并初始化集合
            user = User()
            list = []
            for row in data_result:
                user.userid = row[0]
                user.username = row[1]
                user.password = row[2]
                print("id=%s,username=%s,password=%s" %
                      (user.userid, user.username, user.password))
                list.append(user)
        except Exception:
            print("错误：无法获取数据")

        # 关闭数据库连接
        conn.close()
        return list

    # 增
    def insert_Database(self, username, hpassword):
        '''
        向数据库内增加用户
        输入为所要添加的用户的用户名和密码
        无返回值
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

        # sql中数据库后为password而不是hpassword，因为这里是字段名
        sql = "INSERT INTO yzf_user(username,password) VALUES (%s,%s)"
        try:
            # 执行sql语句
            db.execute(sql, (username, hpassword))
            # 提交到数据库执行
            conn.commit()
        except Exception:
            # 如果发生错误则回滚
            print("Insert error!")
            conn.rollback()

        # 关闭数据库连接
        conn.close()

    # 删
    def delete_Database(self, userid):
        '''
        从数据库中删除数据
        输入为用户id
        无返回值
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

        sql = "delete from yzf_user where ID=%s"
        try:
            # 执行sql语句
            db.execute(sql, userid)
            # 提交到数据库执行
            conn.commit()
        except Exception:
            # 如果发生错误则回滚
            print("Delete error!")
            conn.rollback()

        # 关闭数据库连接
        conn.close()

    # 改
    def update_Database(self, userid, username, password):
        '''
        改动用户数据
        输入用户的用户id，用户名和密码
        无返回值
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

        sql = "update yzf_user set username=%s,password=%s where ID=%s"
        try:
            # 执行sql语句
            db.execute(sql, username, password, userid)
            # 提交到数据库执行
            conn.commit()
        except Exception:
            # 如果发生错误则回滚
            print("Update error!")
            conn.rollback()

        # 关闭数据库连接
        conn.close()

    # 查
    def select_Database(self, username='', userid=''):
        '''
        查询用户信息
        输入为用户名或id
        返回为User类组成的集合
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
        # 实例化User类，并初始化集合
        user = User()
        list = []
        if userid == '':
            try:
                sql = "select * from yzf_user where username like %s"
                # 执行sql语句
                db.execute(sql, username)
                # 将所有的查询结果放入结果集
                data_result = db.fetchall()
                for row in data_result:
                    user.userid = row[0]
                    user.username = row[1]
                    user.password = row[2]
                    print("ID=%s,username=%s,password=%s" %
                          (user.userid, user.username, user.password))
                    list.append(user)
            except Exception:
                print("错误：无法由username获取数据")
                return 0

            # 关闭数据库连接
            conn.close()
            return list
        elif username == '':
            try:
                sql = "select * from yzf_user where ID = %s"
                # 执行sql语句
                db.execute(sql, userid)
                # 将所有的查询结果放入结果集
                data_result = db.fetchall()
                for row in data_result:
                    user.userid = row[0]
                    user.username = row[1]
                    user.password = row[2]
                    print("ID=%s,username=%s,password=%s" %
                          (user.userid, user.username, user.password))
                    list.append(user)
            except Exception:
                print("错误：无法由ID获取数据")
                return 0

            # 关闭数据库连接
            conn.close()
            return list
        elif userid != '' and username != '':
            try:
                sql = "select * from yzf_user where ID = %s and username = %s"
                # 执行sql语句
                db.execute(sql, userid, username)
                # 将所有的查询结果放入结果集
                data_result = db.fetchall()
                for row in data_result:
                    user.userid = row[0]
                    user.username = row[1]
                    user.password = row[2]
                    print("ID=%s,username=%s,password=%s" %
                          (user.userid, user.username, user.password))
                    list.append(user)
            except Exception:
                print("错误：无法由ID获取数据")
                return 0
            # 关闭数据库连接
            conn.close()
            return list
        else:
            print('error')
            # 关闭数据库连接
            conn.close()
            return 0





