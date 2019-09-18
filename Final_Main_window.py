# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import Calculate_value
from evaluate import Ui_Form
from ofile import Ui_Open
player=sqlite3.connect("Final_project.db")
curplayer=player.cursor()

class Ui_MainWindow(object):
    count=0
    def __init__(self, a=''):
        open_team=a
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.bat = QtWidgets.QRadioButton(self.centralwidget)
        self.bat.setObjectName("bat")
        self.horizontalLayout_15.addWidget(self.bat)
        self.bwl = QtWidgets.QRadioButton(self.centralwidget)
        self.bwl.setObjectName("bwl")
        self.horizontalLayout_15.addWidget(self.bwl)
        self.wk = QtWidgets.QRadioButton(self.centralwidget)
        self.wk.setObjectName("wk")
        self.horizontalLayout_15.addWidget(self.wk)
        self.ar = QtWidgets.QRadioButton(self.centralwidget)
        self.ar.setObjectName("ar")
        self.horizontalLayout_15.addWidget(self.ar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bat.toggled.connect(self.checkstate)
        self.bwl.toggled.connect(self.checkstate)
        self.wk.toggled.connect(self.checkstate)
        self.ar.toggled.connect(self.checkstate)

        self.horizontalLayout_15.addItem(spacerItem)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_15.addWidget(self.label_18)
        self.team_name = QtWidgets.QLineEdit(self.centralwidget)
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_15.addWidget(self.team_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.Avialable = QtWidgets.QListWidget(self.centralwidget)
        self.Avialable.setObjectName("Avialable")
        
        self.Avialable.itemDoubleClicked.connect(self.addplayer)
            
        self.horizontalLayout_16.addWidget(self.Avialable)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem1)
        self.Taken = QtWidgets.QListWidget(self.centralwidget)
        self.Taken.setObjectName("Taken")
        self.horizontalLayout_16.addWidget(self.Taken)

        self.Taken.itemDoubleClicked.connect(self.rmplayer)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Team.addAction(self.actionNew_Team)
        self.menuManage_Team.addAction(self.actionOpen_Team)
        self.menuManage_Team.addAction(self.actionSave_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Team.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuManage_Team.triggered[QtWidgets.QAction].connect(self.menufunction)

    def menufunction(self, action):
        txt= (action.text())
        if txt =='New Team':
            Ui_MainWindow.count=0
            self.Avialable.clear()
            self.Taken.clear()
            self.team_name.clear()
            
        if txt =='Save Team ':
            name=self.team_name.text()
            team=[]
            total=0
            temp=0
            for index in range(self.Taken.count()):
                team.append(self.Taken.item(index).text())
            for i in range(len(team)):
                temp=self.getvalue(team[i])
                total=total+temp
            temp=' '.join(team)
            curplayer.execute("INSERT INTO teams (name, players, value) VALUES (?,?,?);", (name,temp,total))
            player.commit()
        if txt =='Open Team':
            open_team=''
            self.window=QtWidgets.QWidget()
            self.ui=Ui_Open()
            self.ui.setup(self.window)
            self.window.show()
        if txt=='Evaluate Team':
            self.window=QtWidgets.QWidget()
            self.temp=Ui_Form()
            self.temp.setup_evaluate(self.window)
            self.window.show()


    def checkstate(self):
            state1='OFF'
            state2='OFF'
            state3='OFF'
            state4='OFF'
            if self.bat.isChecked()==True:
                state1='ON'
                curplayer.execute("select player from stats where category ='Bat';")
                record=curplayer.fetchall()
            elif self.bwl.isChecked()==True:
                state2='ON'
                curplayer.execute("select player from stats where category ='Bwl';")
                record=curplayer.fetchall()
            elif self.wk.isChecked()==True:
                state3='ON'
                curplayer.execute("select player from stats where category ='Wk';")
                record=curplayer.fetchall()
            elif self.ar.isChecked()==True:
                state4='ON'
                curplayer.execute("select player from stats where category ='Ar';")
                record=curplayer.fetchall()
            self.Avialable.clear()
            for i in record:
                record1=''.join(i)
                self.Avialable.addItem(record1)
            

    def addplayer(self, item):
        if Ui_MainWindow.count <11:
            self.Avialable.takeItem(self.Avialable.row(item))
            self.Taken.addItem(item.text())
            Ui_MainWindow.count=Ui_MainWindow.count+1
            
    def rmplayer(self, item):
            self.Taken.takeItem(self.Taken.row(item))
            self.Avialable.addItem(item.text())
            Ui_MainWindow.count=Ui_MainWindow.count-1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bat.setText(_translate("MainWindow", "BAT"))
        self.bwl.setText(_translate("MainWindow", "BWL"))
        self.wk.setText(_translate("MainWindow", "WK"))
        self.ar.setText(_translate("MainWindow", "AR"))
        self.label_18.setText(_translate("MainWindow", "Team Name"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team "))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))

    def getvalue(self,temp):
        total_value=0
        sql="select * from match where player ='"+ temp +"';"
        result=curplayer.execute(sql)
        column_name=[]
        return_name=[]
        for row in result.description:
            column_name.append(row[0])
        result=result.fetchall()
        temp_dict={}

        for res in range(len(result)):
            for col in range(len(column_name)):
                temp_dict.update({column_name[col]:result[res][col]})        
        total_value=Calculate_value.players(temp_dict)
        return total_value
        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

