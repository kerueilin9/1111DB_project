# Team10 Database Project

我們使用MySQL當資料庫

打開MySQL WorkBench
設定Connection
帳號: root
密碼: admin

在script中輸入以下指令並執行
drop database if exists `shopDB`;
create database `shopDB`;

在MySQL WorkBench上方工具欄依序點擊
Server > Data Import
開啟的頁面中
Import from Dump Project Folder 欄位
選擇我們專案的\project\Database
找到同頁面中最下方的 Start Import 點擊並執行
資料庫就建好了 !


如遇到import問題時 需要安裝對應套件
> pip install flask
> pip install flask_cors
> pip install Flask-MySQL==1.5.2
> pip install pymysql
執行後端應用
> python .\Back_end\app.py