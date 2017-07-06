import pymysql

def connect():
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='lrm12350039',
        db='cmdb'
    )
    return con

def query():
    con=connect()
    cur = con.cursor()
    cur.execute('select * from cmdata')
    data = cur.fetchall()
    cur.close()
    return data