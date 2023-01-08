from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL
import pymysql

DEBUG = True
UID = 0
PID = 0
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
     
mysql = MySQL()
    
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'shopDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
CORS(app, resources={r'/*': {'origins': '*'}})

# 註冊
@app.route('/signUp', methods=['POST'])
def signUp():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        data = request.get_json()
        sql = ("INSERT INTO user (Name, Email, Account, Password, Role, Phone, Gender) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        val = (data['Name'], data['Email'], data['Account'], data['Password'], 'member', data['Phone'], data['Gender'])
        cursor.execute(sql, val)
        conn.commit()
        cursor.execute("SELECT UID FROM user WHERE Account = %s", data['Account'])
        userID = cursor.fetchall()
        sql = ("INSERT INTO member (Member_ID, Address) VALUES (%s, %s)")
        val = (userID, data['Address'])
        cursor.execute(sql, val)
        conn.commit()
        return jsonify({
            'status': 'success'
        })
    finally:
        cursor.close() 
        conn.close()

# 登入
@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        data = request.get_json()
        sql = ("SELECT Account, Password from user WHERE (Account = %s)")
        val = (data['Account'])
        cursor.execute(sql, val)
        user = cursor.fetchall()
        if (user == ()):
            print('This account is not registerd.')
            return jsonify({
                'status': 'success',
                'userStatus': '帳號未被註冊'
            })
        elif (data['Password'] != user[0]['Password']):
            print('Wrong password.')
            return jsonify({
                'status': 'success',
                'userStatus': '錯誤的密碼'
            })
        elif (data['Password'] == user[0]['Password']):
            print('Success.')
            cursor.execute("SELECT UID from user WHERE (Account = %s)", val)
            global UID
            UID = cursor.fetchall()[0]['UID']
            print('SignIn UID' + str(UID))
            return jsonify({
                'status': 'success',
                'userStatus': '登入成功',
                'UID': UID
            })
        else:
            return jsonify({
                'status': 'success',
                'userStatus': '-1'
            })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close() 
        conn.close()

# 查看會員
@app.route('/userList', methods=['GET'])
def home():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM user")
        userslist = cursor.fetchall()
        print(userslist)
        return jsonify({
            'status': 'success',
            'members': userslist
        })
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

#取得使用者資料
@app.route('/user', methods=['GET'])
def userget():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * from user where UID = 1")
        user = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'members': user
        })
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
 
        
# 產品
@app.route('/getProduct', methods=['GET'])
def product():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * from product")
        productList = cursor.fetchall()
        return jsonify({
            'status' : 'success',
            'members' : productList
        })
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# 取得UID
@app.route('/UID', methods=['GET'])
def getUID():
    try:
        return jsonify({
            'status': 'success',
            'UID': UID
        })
    except Exception as e:
        print(e)
    finally:
        print('GET UID = ' + str(UID))

# 登出
@app.route('/signOut', methods=['POST'])
def signOut():
    global UID
    UID = 0
    print('SignOut UID' + str(UID))
    return jsonify({
        'status': 'success',
        'userStatus': '登出成功',
        'UID': UID
    })

if __name__ == '__main__':
    app.run()