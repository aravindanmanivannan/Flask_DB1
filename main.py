import pymysql
from app import app
from config import  mysql
from flask import jsonify
from flask import flash, request

@app.route('/query_example', methods = ['GET'])
def students_detail():
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
     
            name = request.args.get('name')
            age = request.args.get('age')

            #name = request.json['name']
            #age = request.json['age']
            print(f"name : {name} , age = {age}")
            
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

            if bool(detail) == True:
                return  detail
            else:
                return"No such details available"
          
    except Exception as e :
        print("Details are not in the database")
        return f"There is an Error {e}"
    
@app.route('/update_example', methods = ['PUT'])
def update_students_detail():
    try:
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

            cursor.execute("select student_id from students;")
            data = cursor.fetchall()
            print(f"data : {data}")

            for i in range(len(data)):
                if id == (data[i]['student_id']):
                    return jsonify ("Update Successfully")
            else:
                return jsonify ("ID not available")

            #return jsonify('Students updated successfully!')
    except Exception as e:
         print("Details are not updated in the database")
         return f"There is an Error {e}"
    
@app.route('/delete_example', methods = ['DELETE'])
def delete_students_detail():
    try:
        if request.method == 'DELETE':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            id = request.args.get('id')

            cursor.execute("select student_id from students;")
            data = cursor.fetchall()
            print(f"data : {data}")

            for i in range(len(data)):
                if int(id) == (data[i]['student_id']):
                    print(f"data inside if {data[i]['student_id']}")
                    print(f" delete from students where student_id = {id}")
                    cursor.execute(f" delete from students where student_id = {id}")
                    conn.commit()
                    break                 
            else:
                print(f"data inside else {data[i]['student_id']}")
                return jsonify(f"{id} ID not available")
            return jsonify('Deleted successfully!')
    except Exception as e:
        print("Details are not Deleted from the database")
        return f"There is an Error {e}"

if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))