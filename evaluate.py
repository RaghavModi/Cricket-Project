# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
player=sqlite3.connect('Final_project.db')
curplayer=player.cursor()

class Ui_Form(object):
    def __init__(self,a='',b='',c=0,d=0):
        self.name_team1=a
        self.name_team2=b
        self.value_1=c
        self.value_2=d
        
    def setup_evaluate(self, Form):
        Form.setObjectName("Form")
        Form.resize(634, 589)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 1, 1, 3)
        self.select_team2 = QtWidgets.QPushButton(Form)
        self.select_team2.setObjectName("select_team2")
        self.select_team2.setCheckable(True)
        self.select_team2.toggle()
        self.select_team2.clicked.connect(self.select_btn2)
        
        self.gridLayout.addWidget(self.select_team2, 1, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 2, 5, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 5, 1, 1)
        self.value2 = QtWidgets.QLineEdit(Form)
        self.value2.setObjectName("value2")
        self.gridLayout.addWidget(self.value2, 3, 7, 1, 1)
        self.value1 = QtWidgets.QLineEdit(Form)
        self.value1.setObjectName("value1")
        self.gridLayout.addWidget(self.value1, 3, 3, 1, 1)
        self.answer = QtWidgets.QLineEdit(Form)
        self.answer.setObjectName("answer")
        self.gridLayout.addWidget(self.answer, 4, 3, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.team1 = QtWidgets.QComboBox(Form)
        self.team1.setObjectName("team1")
        self.additem_team1()
        
        self.gridLayout.addWidget(self.team1, 0, 1, 1, 3)
        self.team2 = QtWidgets.QComboBox(Form)
        self.team2.setObjectName("team2")
        self.additem_team2()
        
        self.gridLayout.addWidget(self.team2, 0, 5, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 8, 1, 1)
        self.select_team1 = QtWidgets.QPushButton(Form)
        self.select_team1.setObjectName("select_team1")
        self.select_team1.setCheckable(True)
        self.select_team1.toggle()
        self.select_team1.clicked.connect(self.select_btn1)
        
        self.gridLayout.addWidget(self.select_team1, 1, 2, 1, 1)
        self.select_team2.raise_()
        self.select_team1.raise_()
        self.team1.raise_()
        self.team2.raise_()
        self.listWidget.raise_()
        self.listWidget_2.raise_()
        self.value1.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.value2.raise_()
        self.answer.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def additem_team1(self):
        sql_temp="select name from teams;"
        record_temp=curplayer.execute(sql_temp)
        temp=''
        result1=record_temp.fetchall()
        sql="select name from teams;"
        record=curplayer.execute(sql)
        for row in range(len(result1)):
            result=record.fetchone()
            temp=''.join(result)
            self.team1.addItem(temp)

    def additem_team2(self):
        sql_temp="select name from teams;"
        record_temp=curplayer.execute(sql_temp)
        temp=''
        result1=record_temp.fetchall()
        sql="select name from teams;"
        record=curplayer.execute(sql)
        for row in range(len(result1)):
            result=record.fetchone()
            temp=''.join(result)
            self.team2.addItem(temp)

    def select_btn2(self):
        self.name_team2=self.team2.currentText()
        sql_temp="select * from teams where name='"+self.name_team2+"';"
        record_temp=curplayer.execute(sql_temp)
        temp=''
        result1=record_temp.fetchall()
        sql="select * from teams where name='"+self.name_team2+"';"
        record=curplayer.execute(sql)
        for row in range(len(result1)):
            result=record.fetchone()
        list_result=list(result)
        team_players=''
        team_player=list_result[1]
        list_player=[]
        list_player=list(team_player.split(" "))
        self.listWidget_2.clear()
        for i in range(len(list_player)):
            self.listWidget_2.addItem(list_player[i])
        self.value_2=0
        self.value_2=list_result[2]
        self.value2.setText(str(self.value_2))
        if self.value_2> self.value_1:
            self.answer.setText(self.name_team2+" WINS")
        elif self.value_2< self.value_1:
            self.answer.setText(self.name_team1+" WINS")
        else:
            self.answer.setText("TIE")
            

    def select_btn1(self):
        
        self.name_team1=self.team1.currentText()
        sql_temp="select * from teams where name='"+self.name_team1+"';"
        record_temp=curplayer.execute(sql_temp)
        temp=''
        result1=record_temp.fetchall()
        sql="select * from teams where name='"+self.name_team1+"';"
        record=curplayer.execute(sql)
        for row in range(len(result1)):
            result=record.fetchone()
        list_result=list(result)
        team_players=''
        team_player=list_result[1]
        list_player=[]
        list_player=list(team_player.split(" "))
        self.listWidget.clear()
        for i in range(len(list_player)):
            self.listWidget.addItem(list_player[i])
        self.value_1=0
        self.value_1=list_result[2]
        self.value1.setText(str(self.value_1))
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.select_team2.setText(_translate("Form", "TEAM 2"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">VALUE OF PLAYER A</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">VALUE OF PLAYER B</span></p></body></html>"))
        self.select_team1.setText(_translate("Form", "TEAM 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setup_evaluate(Form)
    Form.show()
    sys.exit(app.exec_())

