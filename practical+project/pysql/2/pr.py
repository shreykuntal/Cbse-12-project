import mysql.connector as sqltor
conn=sqltor.connect(host="localhost",user="root",passwd="1234",database="sports")
if conn.is_connected():
    print("Successfully connected")
    cursor = conn.cursor()
    cursor.execute("select * from match_details")
    data = cursor.fetchmany(3)
    count = cursor.rowcount
    print("Total no of records fetched from database :",count)
    for row in data:
        print(row)
    conn.close()
else:
    print("MYSqL connection problem")
