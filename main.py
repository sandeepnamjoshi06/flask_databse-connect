from flask import Flask,request,render_template,jsonify
import mysql.connector
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/data",methods=["POST"])
def get_data():
    s_name=request.form["student_name"]
    roll_no=request.form["roll_no"]
    sub1=request.form["sub1"]
    sub2=request.form["sub2"]
    conn=mysql.connector.connect(host="localhost",database="student",user="root",password="123456")
    cursor=conn.cursor()
    query="INSERT INTO info(name,roll_no,sub1,sub2) VALUES(%s,%s,%s,%s)"
    data=(s_name,roll_no,sub1,sub2)
    cursor.execute(query,data)
    conn.commit()
    conn.close()

    return jsonify(s_name,roll_no,sub1,sub2)
if __name__=="__main__":
    app.run(debug=True)