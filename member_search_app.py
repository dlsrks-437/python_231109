import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class = uic.loadUiType("UI/member_ui.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원조회프로그램")

        self.search_btn.clicked.connect(self.db_search)
        self.modify_btn.clicked.connect(self.db_modify)

    def db_search(self):
        memberid = self.memberid_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid = '{memberid}' "

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        result = cur.fetchone()
        if result != None:
            self.password_edit.setText(result[1])
            self.name_edit.setText(result[2])
            self.phone_edit.setText(result[3])
            self.address_edit.setText(result[4])
            self.age_edit.setText(str(result[5]))
        else:
            self.password_edit.setText('------------------')
            self.name_edit.setText('------------------')
            self.phone_edit.setText('------------------')
            self.address_edit.setText('------------------')
            self.age_edit.setText('------------------')


    def db_modify(self):
        memberid = self.memberid_edit.text()
        memberpw = self.password_edit.text()
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        address = self.address_edit.text()
        age = self.age_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = (f"UPDATE member SET memberpw = '{memberpw}', name = '{name}', phone = '{phone}', address = '{address}, age = '{age}' ")

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        cur.close()
        conn.commit()  # insert, delite, update sql문을 사용했을 경우 필수
        conn.close()

        self.db_search()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()
    sys.exit(app.exec_())







