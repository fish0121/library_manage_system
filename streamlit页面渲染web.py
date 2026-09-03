import streamlit as st
import requests

# 后端 FastAPI 地址，保持后端一直开启
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="图书管理系统", layout="wide")
st.title("📚 图书管理系统 - 前端页面")

# -------- 查询图书 --------
st.subheader("图书列表")
if st.button("刷新图书"):
    try:
        res = requests.get(f"{BASE_URL}/books", timeout=10)
        if res.status_code == 200:
            book_data = res.json()["data"]
            st.table(book_data)
        else:
            st.error(f"请求失败，状态码：{res.status_code}")
    except Exception as e:
        st.error(f"无法连接后端，请检查uvicorn是否启动！{e}")

st.subheader("🔍 图书搜索")
search_keyword = st.text_input("输入图书名称搜索")

if st.button("搜索图书"):
    try:
        res = requests.get(f"{BASE_URL}/books", timeout=10)
        if res.status_code == 200:
            all_books = res.json()["data"]
            # 过滤：书名包含关键词
            result_list = [
                book for book in all_books
                if search_keyword.lower() in book["book_name"].lower()
            ]
            if len(result_list) > 0:
                st.table(result_list)
            else:
                st.info("没有找到匹配的图书")
        else:
            st.error("获取图书数据失败")
    except Exception as e:
        st.error(f"后端连接异常：{e}")



# -------- 查询读者 --------
st.subheader("读者列表")
if st.button("刷新读者"):
    try:
        res = requests.get(f"{BASE_URL}/readers", timeout=10)
        if res.status_code == 200:
            reader_data = res.json()["data"]
            st.table(reader_data)
        else:
            st.error(f"请求失败，状态码：{res.status_code}")
    except Exception as e:
        st.error(f"无法连接后端！{e}")


# -------- 借书表单 --------
st.subheader("借书操作")
borrow_book_id = st.number_input("输入图书ID", min_value=1, step=1)
borrow_reader_id = st.number_input("输入读者ID", min_value=1, step=1)

if st.button("确认借书"):
    payload = {
        "book_id": borrow_book_id,
        "reader_id": borrow_reader_id
    }
    try:
        res = requests.post(f"{BASE_URL}/borrow", json=payload, timeout=10)
        if res.status_code == 200:
            st.success("借书成功")
        else:
            st.warning(f" 借书失败，返回信息：{res.text}")
    except Exception as e:
        st.error(f"后端连接异常：{e}")


# -------- 还书表单 --------
st.subheader("还书操作")
return_book_id = st.number_input("归还图书ID", min_value=1, step=1)

if st.button("确认还书"):
    payload = {
        "book_id": return_book_id
    }
    try:
        res = requests.post(f"{BASE_URL}/return_book", json=payload, timeout=10)
        if res.status_code == 200:
            st.success("还书成功")
        else:
            st.warning(f"还书失败：{res.text}")
    except Exception as e:
        st.error(f"后端连接异常：{e}")

