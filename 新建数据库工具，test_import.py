#这个文件分装数据库连接
import pymysql

# 数据库配置
DB_CONFIG = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"Yu@20233198",
    "database":"book_borrow",
    "charset":"utf8mb4"
}

def get_conn():
    """获取数据库连接"""
    return pymysql.connect(**DB_CONFIG)

# ----------图书相关操作----------
def add_book(book_name, author, stock, publish_time):
    """新增图书"""
    conn = get_conn()
    cursor = conn.cursor()
    sql = """INSERT INTO book(book_name,author,stock,publish_time) VALUES(%s,%s,%s,%s)"""
    cursor.execute(sql,(book_name,author,stock,publish_time))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_books():
    """查询全部图书"""
    conn = get_conn()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM book")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

# ----------读者相关操作----------
def add_reader(name, phone, class_name):
    """新增读者"""
    conn = get_conn()
    cursor = conn.cursor()
    sql = """INSERT INTO reader(name,phone,class_name) VALUES(%s,%s,%s)"""
    cursor.execute(sql,(name,phone,class_name))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_readers():
    conn = get_conn()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM reader")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

# ----------借书、还书业务----------
def borrow_book(book_id, reader_id):
    """借书：库存-1，新增借阅记录"""
    conn = get_conn()
    cursor = conn.cursor()
    # 判断库存
    cursor.execute("SELECT stock FROM book WHERE book_id=%s",(book_id,))
    stock = cursor.fetchone()[0]
    if stock <= 0:
        conn.rollback()
        cursor.close()
        conn.close()
        return False
    # 新增借阅记录
    cursor.execute("INSERT INTO borrow_record(book_id,reader_id) VALUES(%s,%s)",(book_id,reader_id))
    # 库存减1
    cursor.execute("UPDATE book SET stock=stock-1 WHERE book_id=%s",(book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def return_book(record_id):
    """还书：填写还书时间，库存+1"""
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("UPDATE borrow_record SET return_time=NOW() WHERE record_id=%s",(record_id,))
    cursor.execute("UPDATE book SET stock=stock+1 WHERE book_id=(SELECT book_id FROM borrow_record WHERE record_id=%s)",(record_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def get_borrow_list():
    """查询全部借阅记录，关联图书、读者名字"""
    conn = get_conn()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = """
    SELECT br.record_id,b.book_name,r.name,br.borrow_time,br.return_time
    FROM borrow_record br
    LEFT JOIN book b ON br.book_id = b.book_id
    LEFT JOIN reader r ON br.reader_id = r.reader_id
    """
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res
