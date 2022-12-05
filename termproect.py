import pymysql
import datetime

conn = pymysql.connect(host='192.168.187.3', port=4567, user='root', db='GYM', password='eoaks14', charset='utf8')
cursor = conn.cursor()

cursor.execute('USE GYM;') #GYM database 사용함

p = int(input("회원은 1 관리자는 0번입니다. :"))


if p == 1:
    mem_id = int(input('회원번호(휴대전화 뒤자리)를 입력하세요 :'))
    sql = f"SELECT * FROM Member WHERE mem_id = {mem_id}"
    cursor.execute(sql)
    pr = cursor.fetchall()
    print(pr)
    
conn.commit()
conn.close()
