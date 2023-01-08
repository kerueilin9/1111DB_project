from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL
import pymysql

DEBUG = True
UID = ''
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
                'userStatus': 'This account is not registerd.'
            })
        elif (data['Password'] != user[0]['Password']):
            print('Wrong password.')
            return jsonify({
                'status': 'success',
                'userStatus': 'Wrong password.'
            })
        elif (data['Password'] == user[0]['Password']):
            print('Success.')

            cursor.execute("SELECT UID from user WHERE (Account = %s)", val)
            UID = cursor.fetchall()
            print(UID[0]['UID'])
            return jsonify({
                'status': 'success',
                'userStatus': 'Success.'
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
@app.route('/user', methods=['GET'])
def userget():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT Phone,Email,Address from user , member where UID = 1 or Member_ID = 1")
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

if __name__ == '__main__':
    app.run()