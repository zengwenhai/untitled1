import pymysql


class mySqlDb(object):
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db


    def connect_mysqldb(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.password,
                               db=self.db)
        except Exception as e:
            raise e
        else:
            return self.conn

    def getcursor(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def get_one(self, sql, parames):
        self.cursor.execute(sql, parames)
        result = self.cursor.fetchone()
        return result



if __name__ == "__main__":
    c = mySqlDb('127.0.0.1', 3306, 'root', '', 'test')
    print(c)
    sql = 'select * from user where name=%s and passwd=%s'
    parames = ('zengwenhai', 123)
    c.connect_mysqldb()
    c.getcursor()
    re = c.get_one(sql, parames)
    print(re)


# conn = pymysql.connect('127.0.0.1', 3306, 'root', '', 'test')
# cursor = conn.cursor()
# sql = 'select * from test'
# data = cursor.execute(sql)
# print(data)