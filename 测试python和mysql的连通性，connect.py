#为方便后续的实验，在开始时，需在python终端借助清华源进行安装  pip install pymysql fastapi streamlit -i https://pypi.tuna.tsinghua.edu.cn/simple
import pymysql

try:
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",        #你的mysql用户名
        password="你的密码", #你的mysql密码
        database="borrow_book",   
        charset="utf8mb4"
    )
    print(" Python 和 MySQL 连接成功！")
    conn.close()

except Exception as e:
    print("连接失败：", e)
