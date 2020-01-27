#============================================================
# Create Time:			2020-01-27 20:35:37
# Last modify:			2020-01-27 22:13:27
# Writer:			Wenhao	1795902848@qq.com
# File Name:			MysqlOperator.py
# File Type:			PY Source File
# Tool:				Mac -- vim & python
# Information:			
#============================================================
#coding=utf-8
import pymysql
class MysqlOperator:
    def __init__(this):
        with open('password.txt', 'r', encoding='utf-8') as f:
            password = f.read().strip()
        this.conn = pymysql.connect(
                host="localhost", user="root", 
                password=password, database="News")
        this.curr = this.conn.cursor()
        initOp = """create table if not exists news (
            datetime datetime,
            title varchar(100) primary key,
            editor varchar(15))"""
        this.curr.execute(initOp)
        this.cnt = 0
        return None

    def insertOneLine(this, date:str, title:str, editor:str):
        this.cnt += 1
        insertSql = 'insert into news values(\'%s\', \'%s\', \'%s\')'%(
                date, title, editor)
        try:
            this.curr.execute(insertSql)
            this.commit()
        except Exception as e:
            this.conn.rollback()

        #if(this.cnt == 10):
        #    this.commit()
        #    this.cnt = 0
        return None

    def commit(this):
        this.conn.commit()
        return None

    def lineExists(this, title:str):
        this.commit()
        this.curr.execute(
                'select title from news where title = "%s"'%(title))
        fetch = this.curr.fetchall()
        if(fetch != () and fetch[0][0] == title):
            return True
        return False

if __name__ == "__main__":
    m = MysqlOperator()
    #ans = m.lineExists("春晚举行第五次彩排")
    def test1():
        m.curr.execute('select title from news where datetime="2020-01-15"')
        fetch = m.curr.fetchall()
        print(fetch)
        return None

    test1()
