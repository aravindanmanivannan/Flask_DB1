import pymysql
from app import app
from config import  mysql
from flask import jsonify
from flask import flash, request

@app.route('/query_example', methods = ['GET'])
def students_detail():
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        name = request.args.get('name')
        age = request.args.get('age')
        print(f"name : {name} , age = {age}")
        idd= "student_name"

        try: 
            if bool(name) == True and bool(age) == True:
                cursor.execute (f"select * from students where student_name = {name}and age=  {age}")
                print("if")
            elif bool(name) == True:
                cursor.execute (f"select * from students where student_name =  {name}")
                print("elif1")
            elif bool(age) == True:
                cursor.execute (f"select * from students where age = {age} ")
                print("elif2")
            
            print(f"name : {name} , age = {age}")
            detail = cursor.fetchall()
            print(f"students details : {detail}")
        except :
            return "There is a Error"

        return  detail   
    
@app.route('/update_example', methods = ['PUT'])
def update_students_detail():
    if request.method == 'PUT':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
         
        id = request.json['id']
        name = str(request.json['name'])
        age = request.json['age']
        phone = str(request.json['phone'])

        #name = request.args.get('name')
        #age = request.args.get('age')
        #phone = request.args.get('phone')
        #id = request.args.get('id')
        

        print(f"name : {name}, age : {age}, phone : {phone} ,id : {id}")
        print(f"Query update students set student_name = {name}, age={age},phone={phone} where student_id = {id}")
        cursor.execute(f"update students set student_name = {name}, age={age},phone={phone} where student_id = {id}")
        conn.commit()
        #response = 'Students updated successfully!'
        return jsonify('Students updated successfully!') 
    
@app.route('/delete_example', methods = ['DELETE'])
def delete_students_detail():
    if request.method == 'DELETE':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        id = request.args.get('id')

        cursor.execute(f" delete from students where student_id = {id}")
        conn.commit()
        return jsonify('Deleted successfully!')
    
if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))