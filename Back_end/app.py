from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL
import pymysql

DEBUG = True
UID = 0
PID = 0
OID = 0
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

#______________註冊______________

# 註冊
@app.route('/signUp', methods=['GET','POST'])
def signUp():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        data = request.get_json()
        cursor.execute('SELECT Account, Password FROM user WHERE (Account = %s)', data['Account'])
        user = cursor.fetchall()
        if (user == ()):
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
                'status': 'success',
                'values': '註冊成功'
            })
        else:
            return jsonify({
                'status': 'success',
                'values': '此帳號已被註冊'
            })
    finally:
        cursor.close() 
        conn.close()

#______________登入______________

# 登入
@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        data = request.get_json()
        sql = ("SELECT Account, Password FROM user WHERE (Account = %s)")
        val = (data['Account'])
        cursor.execute(sql, val)
        user = cursor.fetchall()
        if (user == ()):
            print('This account is not registerd.')
            return jsonify({
                'status': 'success',
                'values': '帳號未被註冊'
            })
        elif (data['Password'] != user[0]['Password']):
            print('Wrong password.')
            return jsonify({
                'status': 'success',
                'values': '錯誤的密碼'
            })
        elif (data['Password'] == user[0]['Password']):
            print('Success.')
            cursor.execute("SELECT UID FROM user WHERE (Account = %s)", val)
            global UID
            UID = cursor.fetchall()[0]['UID']
            print('SignIn UID = ' + str(UID))
            return jsonify({
                'status': 'success',
                'values': '登入成功',
                'UID': UID
            })
        else:
            return jsonify({
                'status': 'success',
                'values': '-1'
            })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close() 
        conn.close()

#______________使用者______________

# 查看會員
@app.route('/userList', methods=['GET'])
def userList():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM user")
        userslist = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'values': userslist
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close() 
        conn.close()

#取得使用者資料
@app.route('/user', methods=['GET'])
def getUser():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        global UID
        cursor.execute("SELECT * FROM user WHERE UID = %s", UID)
        user = cursor.fetchall()
        cursor.execute("SELECT Address FROM member WHERE Member_ID = %s", UID)
        Address = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'values': user,
            'Address': Address
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close() 
        conn.close()

#取得身分
@app.route('/getRole', methods=['GET'])
def getRole():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        global UID
        cursor.execute("SELECT Role FROM user WHERE UID = %s", UID)
        role = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'values': role
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close() 
        conn.close()

#修改使用者資料
@app.route('/modifyUser', methods=['GET', 'POST'])
def modifyUser():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        data = request.get_json()
        global UID
        val = (data['Email'], data['Phone'], UID)
        cursor.execute("UPDATE user SET Email= %s, Phone= %s  WHERE UID = %s", val)
        conn.commit()
        val = (data['Address'], UID)
        cursor.execute("UPDATE member SET Address= %s WHERE Member_ID = %s",val)
        conn.commit()
        Address = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'values': '修改成功'
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close() 
        conn.close()

#______________產品______________

# 主頁產品
@app.route('/getAllProduct', methods=['GET'])
def getAllProduct():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM product")
        productList = cursor.fetchall()
        return jsonify({
            'status' : 'success',
            'values' : productList
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()
# 進入產品
@app.route('/getProduct', methods=['GET'])
def getProduct():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        global PID
        cursor.execute("SELECT * FROM product WHERE PID = %s", PID)
        product = cursor.fetchall()
        return jsonify({
            'status' : 'success',
            'values' : product
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()

#______________購物車______________

#加入購物車
@app.route('/addToShoppingCart', methods=['POST'])
def addToShoppingCart():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        data = request.get_json()
        global PID
        global UID
        val = (PID, data['Quantity'], data['Customize'], UID)
        cursor.execute("INSERT INTO shoppingcart (PID, Quantity, Customize, UID) VALUES (%s, %s, %s, %s)", val)
        conn.commit()
        shoppingCart = cursor.fetchall()
        return jsonify({
            'status' : 'success',
            'values' : '已加入購物車'
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()

#進入購物車
@app.route('/getShoppingCart', methods=['GET'])
def getShoppingCart():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        global UID
        cursor.execute("SELECT * FROM shoppingCart AS S, product AS P WHERE S.UID = %s AND P.PID = S.PID", UID)
        shoppingCart = cursor.fetchall()
        return jsonify({
            'status' : 'success',
            'values' : shoppingCart
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()

#刪除購物車
@app.route('/deleteShoppingCart', methods=['POST'])
def deleteShoppingCart():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        data = request.get_json()
        global UID
        val = (UID, data['CID'])
        cursor.execute("DELETE FROM shoppingCart AS S WHERE S.UID = %s AND S.CID = %s", val)
        conn.commit()
        return jsonify({
            'status' : 'success',
            'values' : '成功刪除'
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/shoppingCartAddOrder', methods=['POST'])
def shoppingCartAddOrder():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        data = request.get_json()
        global UID
        val = (data['PID'], 9, UID, data['Order_date'], data['Quantity'], '剛剛成立', '貨到付款', '貨到付款', data['Fee'], data['Other_request'])
        cursor.execute("INSERT INTO `order` (PID, Manager_ID, Member_ID, Order_date, Quantity, Status, Payment_method, Delivery_method, Fee, Other_request) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", val)
        conn.commit()
        cursor.execute("DELETE FROM `shoppingCart`")
        conn.commit()
        return jsonify({
            'status' : 'success',
            'values' : '訂單成立'
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()

#______________訂單(order SQL)______________
@app.route('/getAllOrderByUser', methods=['GET'])
def getOrderByUser():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT OID, Member_ID AS UID, product.Image AS Image, productName AS `Name`, Other_request AS Other, Price, `order`.Quantity AS Quantity FROM `order` INNER JOIN product USING(PID) WHERE Member_ID = %s;", UID)
    order = cursor.fetchall()
    return jsonify({
            'status' : 'success',
            'values' : order
        })

@app.route('/getAllOrder', methods=['GET'])
def getAllOrder():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT OID, Member_ID AS UID, product.Image AS Image, productName AS `Name`, Other_request AS Other, Price, `order`.Quantity AS Quantity FROM `order` INNER JOIN product USING(PID);")
    order = cursor.fetchall()
    return jsonify({
            'status' : 'success',
            'values' : order
        })

@app.route('/getOrderStatusByOID', methods=['GET'])
def getOrderByOID():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    global OID
    cursor.execute("SELECT OID, Member_ID AS UID, `Status` FROM `order` WHERE OID = %s;", OID)
    order = cursor.fetchall()
    return jsonify({
            'status' : 'success',
            'values' : order
        })

@app.route('/modifyOrderStatus', methods=['POST'])
def modifyOrderStatus():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        data = request.get_json()
        global OID
        val = (data['Status'], OID)
        cursor.execute("UPDATE `order` SET `Status`= %s WHERE OID = %s", val)
        conn.commit()
        Address = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'values': '修改成功'
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close() 
        conn.close()

#______________換頁傳遞資訊______________
# PID POST
@app.route('/PID/<int:pid>', methods=['POST'])
def Update(pid):
    global PID
    PID = pid
    return jsonify({
        'status' : 'success',
        'values' : pid
    })

# 取得UID
@app.route('/UID', methods=['GET'])
def getUID():
    global UID
    print('GET UID = ' + str(UID))
    return jsonify({
        'status': 'success',
        'UID': UID
    })

@app.route('/OID', methods=['POST'])
def setOID():
    data = request.get_json()
    global OID
    OID = data['OID']
    print('OID is' + str(OID))
    return jsonify({
        'status': 'success'
    })
@app.route('/getOID', methods=['POST'])
def getOID():
    data = request.get_json()
    global OID
    OID = data['OID']
    print('OID is' + str(OID))
    return jsonify({
        'status': 'success'
    })
#______________登出______________

# 登出
@app.route('/signOut', methods=['POST'])
def signOut():
    global UID
    UID = 0
    print('SignOut UID = ' + str(UID))
    return jsonify({
        'status': 'success',
        'values': '登出成功',
        'UID': UID
    })

# ____________編輯商品____________

# 編輯商品

@app.route('/editProduct', methods=['POST'])
def editProduct():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        data = request.get_json()
        global PID
        val = (data['name'], data['image'], data['price'],
               data['discount'], data['describe'], PID)
        cursor.execute(
            "UPDATE product SET productName= %s, Image= %s, Price= %s, Discount= %s, `Describe`= %s WHERE PID = %s", val)
        
        conn.commit()
        return jsonify({
            'status': 'success',
            'values': '編輯成功'
        })
    finally:
        cursor.close()
        conn.close()

#取得商品
@app.route('/getTargetProduct/<int:pid>', methods=['get'])
def getTargetProduct(pid):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM product WHERE PID = %s", pid)
        product = cursor.fetchall()
        return jsonify({
            'status' : 'success',
            'values' : product
        })
    # except Exception as e:
    #     print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run()