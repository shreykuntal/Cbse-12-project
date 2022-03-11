import pymysql as pym
mycon=pym.connect(host="localhost",user="root",passwd="1234",database="sports")
cursor=mycon.cursor()
cursor.execute("select * from team")
data=cursor.fetchall()
for i in data:
    print(i)
mycon.close() 
