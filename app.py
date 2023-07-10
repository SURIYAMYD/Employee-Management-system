from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="surya@2003"
app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

#loading home page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    
    return render_template("home.html",datas=res)

#new users details add
@app.route("/addusers",methods=['GET','POST'])
def addusers():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        con=mysql.connection.cursor()
        sql="insert into users(NAME,AGE,CITY) value (%s,%s,%s)"
        con.execute(sql,[name,age,city])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    
        
    return render_template("addusers.html")
    
#udate users details
@app.route("/editusers/<string:id>",methods=['GET','POST'])
def editusers(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        con=mysql.connection.cursor()
        sql="update users set NAME=%s,AGE=%s,CITY=%s where ID=%s"
        con.execute(sql,[name,age,city,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
    
    
    sql="select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()

    return render_template("editusers.html")
    
#delete users details
@app.route("/deletetusers/<string:id>",methods=['GET','POST'])
def deleteuser(id): 
    con=mysql.connection.cursor()
    sql="delete from users where ID=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))
    


if (__name__=='__main__'):
    app.run(debug=True)