import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')
# DB와 파이썬파일 사이에 연결통로 생성

sql = "INSERT INTO member VALUES('cat', '28467', '강감찬', '101-4867-8719', '개성', 61)"

cur = conn.cursor()  # 커서 생성
cur.execute(sql)  # SQL문 실행



cur.close()
conn.commit()  # insert, delite, update sql문을 사용했을 경우 필수
conn.close()






