# library_manage_system
图书管理系统，该系统包含图书，读者信息以及借阅业务，包含数据表的设计、视图、存储过程，附带交互网页。

项目简介
本系统实现图书、读者信息维护，图书借阅归还业务，使用MySql完成底层数据存储，编写存储过程处理借阅业务逻辑；
基于Streamlit快速搭建Web交互页面，无需前端框架即可完成可视化管理操作。

🛠技术栈
- Python
- Streamlit（Web交互页面）
- MySQL（数据表、视图、存储过程）

✨核心功能
1. 图书信息管理：图书新增、修改、查询
2. 读者信息维护
3. 图书借阅、归还业务，调用MySQL存储过程完成业务处理
4. 借阅记录查询，逾期图书筛选
5. 基础数据统计展示
```
📂项目目录结构
├── main_api.py # FastAPI 后端 REST 接口
├── web.py # Streamlit 前端页面，requests 调用后端 API
├── connect.py # MySQL 数据库连接封装
├── test.py # 测试脚本
├── test_import.py # 测试脚本
├── sql/
│ └── init.sql # MySQL 建表、视图、存储过程初始化脚本
├── requirements.txt # 项目依赖清单
└── README.md # 项目说明文档
```
