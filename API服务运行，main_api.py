from fastapi import FastAPI
#导入工具
from test_import import add_book,get_all_books,add_reader,get_all_readers,borrow_book,return_book,get_borrow_list

app = FastAPI(title="图书借阅管理接口")

# 获取全部图书
@app.get("/books")
def api_get_books():
    return {"data":get_all_books()}

# 获取全部读者
@app.get("/readers")
def api_get_readers():
    return {"data":get_all_readers()}

# 借书接口，传图书id、读者id
@app.post("/borrow")
def api_borrow(book_id:int,reader_id:int):
    res = borrow_book(book_id,reader_id)
    if res:
        return {"msg":"借书成功"}
    else:
        return {"msg":"借书失败，库存不足"}

# 还书接口，传借阅记录record_id
@app.post("/return_book")
def api_return(record_id:int):
    return_book(record_id)
    return {"msg":"还书成功"}

# 查询所有借阅记录
@app.get("/borrow_list")
def api_borrow_list():
    return {"data":get_borrow_list()}
