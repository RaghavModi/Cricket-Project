# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ofile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
player=sqlite3.connect('Final_project.db')
curplayer=player.cursor()

class Ui_Open(object):
    def __init__(self,a='',b=0):
        self.name=a
        self.value_team=b
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(369, 379)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.team_list = QtWidgets.QComboBox(Form)
        self.team_list.setObjectName("team_list")
        self.horizontalLayout.addWidget(self.team_list)
        self.select_team = QtWidgets.QPushButton(Form)
        self.select_team.setObjectName("select_team")
        self.select_team.setCheckable(True)
        self.select_team.toggle()
        self.select_team.clicked.connect(self.select_team1)
        
        self.horizontalLayout.addWidget(self.select_team)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.player = QtWidgets.QListWidget(Form)
        self.player.setObjectName("player")
        self.additem_player()
        self.verticalLayout.addWidget(self.player)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Value = QtWidgets.QLineEdit(Form)
        self.Value.setObjectName("Value")
        self.horizontalLayout_2.addWidget(self.Value)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def additem_player(self):
        sql_temp="select name from teams;"
        record_temp=curplayer.execute(sql_temp)
        temp=''
        result1=record_temp.fetchall()
        sql="select name from teams;"
        record=curplayer.execute(sql)
        for row in range(len(result1)):
            result=record.fetchone()
            temp=''.join(result)
            self.team_list.addItem(temp)


    def select_team1(self):
        self.name=self.team_list.currentText()
        sql_temp="select * from teams where name='"+self.name+"';"
        record_temp=curplayer.execute(sql_temp)
        temp=''
        result1=record_temp.fetchall()
        sql="select * from teams where name='"+self.name+"';"
        record=curplayer.execute(sql)
        for row in range(len(result1)):
            result=record.fetchone()
        list_result=list(result)
        team_players=''
        team_player=list_result[1]
        list_player=[]
        list_player=list(team_player.split(" "))
        self.player.clear()
        for i in range(len(list_player)):
            self.player.addItem(list_player[i])
        self.value_team=0
        self.value_team=list_result[2]
        self.Value.setText(str(self.value_team))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">TEAM NAME</span></p></body></html>"))
        self.select_team.setText(_translate("Form", "SELECT"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">TEAM VALUE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Open()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())

