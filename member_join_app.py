import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class = uic.loadUiType("UI/join_ui.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원가입프로그램")

        self.check_btn.clicked.connect(self.idCheck)
        self.join_btn.clicked.connect(self.join)
        self.clear_btn.clicked.connect(self.reset)

    def idCheck(self):
        memberid = self.memberid_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid = '{memberid}' "

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        result = cur.fetchone()
        print(result)

        if result == None:
            QMessageBox.warning(self, 'pass', '사용 가능')
            self.check_btn.setStyleSheet("color:blue;")
        else:
            QMessageBox.warning(self, 'Fail', ' 사용 불가 \n아이디 중복')
            self.check_btn.setStyleSheet("color:red;")

        cur.close()
        conn.commit()
        conn.close()


    def join(self):
        # if check_btn.StyleSheet.color == 'black':
        #     QMessageBox.warning(self, 'warning', '아이디 중복확인 필요')
        memberid = self.memberid_edit.text()
        memberpw = self.password_edit.text()
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        address = self.address_edit.text()
        age = self.age_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"INSERT INTO member VALUES('{memberid}', '{memberpw}', '{name}', '{phone}', '{address}', {age})"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        cur.close()
        conn.commit()
        conn.close()

        QMessageBox.warning(self, 'success', '가입 완료')
        self.check_btn.setStyleSheet("color:black;")
        self.reset()

    def reset(self):
        self.memberid_edit.clear()
        self.password_edit.clear()
        self.name_edit.clear()
        self.phone_edit.clear()
        self.address_edit.clear()
        self.age_edit.clear()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()
    sys.exit(app.exec_())