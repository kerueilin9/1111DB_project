# Team10 Database Project

我們使用MySQL當資料庫

打開MySQL WorkBench
設定Connection
帳號: root
密碼: admin

在Query script中輸入以下指令並執行
drop database if exists `shopDB`;
create database `shopDB`;

在MySQL WorkBench上方工具欄依序點擊
Server > Data Import
開啟的頁面中包含
Import from Dump Project Folder 欄位
選擇我們專案的\project\Database
找到同頁面中最下方的 Start Import 點擊並執行
資料庫就建好了 !

要執行網頁前 需先執行 \Back_end\app.py
> pip install flask
> pip install flask_cors
> pip install Flask-MySQL==1.5.2
> pip install pymysql
> python .\Back_end\app.py

最後開啟index.html即可開始使用系統

Manager 帳號與密碼
man01
man01

Employee 帳號與密碼
emp1
emp1

Member 帳號與密碼
mem1
mem1