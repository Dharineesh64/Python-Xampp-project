#!C:\Python\python.exe
import cgi
import mysql.connector
print("Content-Type:text\html\r\n\r\n")
print("<html>")
print("<body>")
#s="Python"
#print(s)
print("<h1>WELCOME TO DATABASE</h1>")
formDetails=cgi.FieldStorage()
Name=formDetails.getvalue("username")
Mobile=formDetails.getvalue("phone")
Password=formDetails.getvalue("pass")
print("<h1><mark>",Name,"<br>",Mobile,"<br>",Password,"</mark></h1>")

#2.backened to database python to sql

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sangeetha"
)
cursorData=DB.cursor()
#insert into tablename (column name datatype,col) values("","","")
sql="insert into database1 (Name,Mobile,Password) values(%s,%s,%s)"
values=(Name,Mobile,Password)
cursorData.execute(sql,values)
DB.commit()

print("</body>")
print("</html>")

