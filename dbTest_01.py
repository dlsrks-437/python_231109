# 1) DB가 설치된 컴퓨터의 IP 주소 (내 컴퓨터에 설치되어 잇으면 localhost)
# 2) DB의 계정 root
# 3) DB의 비밀번호 12345
# 4) DB(스키마)의 이름



import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')
# DB와 파이썬파일 사이에 연결통로 생성

sql = "SELECT * FROM member"
#sql문 생성하여 문자열로 저장

cur = conn.cursor()  # 커서 생성
cur.execute(sql)  # SQL문 실행

result = cur.fetchall()
print(result)
print(result[0])

for member in result:
    print(member[2])

cur.close()
conn.close()




