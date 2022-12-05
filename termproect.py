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
elif p == 0:
    k = int(input('원하는 행동의 숫자를 입력하세요. 1.조회, 2.추가, 3.수정, 4.삭제, 5.조건조회 :'))
# while(True):
    if k == 1: #조회
        entity = input('조회하려는 항목을 선택하세요 gym, member, trainer, program, inbody, manage : ')
        if entity == 'gym':
            Gym = int(input('지점번호를 입력하세요 :'))
            sql = f"SELECT * FROM Gym WHERE Gym_id = {Gym}"
            cursor.execute(sql)
            pr = cursor.fetchall()
            print(pr)

        elif entity == 'member':
            mem_id = int(input('회원번호(휴대전화 뒤자리)를 입력하세요 :'))
            sql = f"SELECT * FROM Member WHERE mem_id = {mem_id}"
            cursor.execute(sql)
            pr = cursor.fetchall()
            print(pr)

        elif entity == 'trainer':
            trainer_id = int(input('트레이너 아이디를 입력하세요 :'))
            sql = f"SELECT * FROM Trainer WHERE trainer_id = {trainer_id}"
            cursor.execute(sql)
            pr = cursor.fetchall()
            print(pr)
        
        elif entity == 'program':
            pid = int(input('프로그램 번호를 입력하세요 :'))
            sql = f"SELECT * FROM Program WHERE pid = {pid}"
            cursor.execute(sql)
            pr = cursor.fetchall()
            print(pr)
        
        elif entity == 'inbody':
            mem_id = int(input('회원번호(휴대전화 뒤자리)를 입력하세요 :'))
            sql = f"SELECT * FROM InBody WHERE mem_id = {mem_id}"
            cursor.execute(sql)
            pr = cursor.fetchall()
            print(pr)

        elif entity == 'manage':
            trainer_id = int(input('트레이너 아이디를 입력하세요 :'))
            sql = f"SELECT * FROM Manage WHERE trainer_id = {trainer_id}"
            cursor.execute(sql)
            pr = cursor.fetchall()
            print(pr)
        # break
conn.commit()
conn.close()
