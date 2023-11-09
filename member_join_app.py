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
        else:
            QMessageBox.warning(self, 'Fail', ' 사용 불가 \n아이디 중복')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()
    sys.exit(app.exec_())