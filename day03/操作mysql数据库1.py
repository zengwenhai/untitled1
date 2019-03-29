import pymysql


class MySqlHelper(object):

    def conn(self):
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               passwd='',
                               db='test')
        return conn

    def get_one(self, sql, params):
        cur = self.conn().cursor()
        data = cur.execute(sql, params)
        result = cur.fetchone()
        return result


def checkValid(name, passwd):
    opera = MySqlHelper()
    sql = 'select * from user where name=%s and passwd=%s'
    parames = (name, passwd)
    result = opera.get_one(sql=sql, params=parames)
    return result


def info():
    name = input("请输入用户名:\n")
    passwd = input("请输入密码:\n")
    result = checkValid(name, passwd)
    if result:
        print("登录成功，%s" %(name))
    else:
        print("登录失败，请检查用户名或密码！")


if __name__ == "__main__":
    info()