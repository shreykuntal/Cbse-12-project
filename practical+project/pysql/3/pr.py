import mysql.connector as sqltor
conn=sqltor.connect(host="localhost",user="root",passwd="1234",database="sports")
if conn.is_connected():
    print("Successfully connected")
    cursor = conn.cursor()
    cursor.execute("delete from match_details where FirstTeamID=1")
    data = cursor.fetchmany(10)
    count = cursor.rowcount
    print("Total no of records deleted from database :",count)
    conn.commit()
    conn.close()
else:
    print("MYSqL connection problem")
