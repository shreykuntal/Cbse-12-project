import mysql.connector as ms
db=ms.connect(host="localhost",user="root",passwd="1234",database='school')
cn=db.cursor()
cn.execute("create table students ( rno int(3) not null unique, name char(30), marks int(3), grade char(1) )")
db.commit()
def insert_rec():
    while True:
        rn=int(input("Enter roll number:"))
        sname=input("Enter name:")
        marks=float(input("Enter marks:"))
        gr=input("Enter grade:")
        cn.execute("insert into students values({},'{}',{},'{}')".format(rn,sname,marks,gr))
        db.commit()
        ch=input("Want more records? Press (N/n) to stop entry:")
        if ch in 'Nn':
            break

def update_rec():
    rn=int(input("Enter rollno to update:"))
    marks=float(input("Enter new marks:"))
    gr=input("Enter Grade:")
    cn.execute("update students set marks={},grade='{}' where rno={}".format(marks,gr,rn))
    db.commit()

def delete_rec():
    rn=int(input("Enter rollno to delete:"))
    cn.execute("delete from students where rno={}".format(rn))
    db.commit()

def view_rec():
    cn.execute("select * from students;")
    data = cn.fetchall()
    for row in data:
        print(row)
while True:
  print("MENU\n1. Insert Record\n2. Update Record \n3. Delete Record\n4. Display Record \n5. Exit")
  ch=int(input("Enter your choice: "))
  if ch==1:
    insert_rec()
  elif ch==2:
    update_rec()
  elif ch==3:
    delete_rec()
  elif ch==4:
    view_rec()
  elif ch==5:
    break
  else:
    print("Invalid Option")
