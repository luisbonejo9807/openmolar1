# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar/src/openmolar/qt-designer/newSetup.ui'
#
# Created: Mon May 24 22:45:21 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 405)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtGui.QLabel(self.page)
        self.label_7.setMinimumSize(QtCore.QSize(0, 100))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.sysAdvice_label = QtGui.QLabel(self.page)
        self.sysAdvice_label.setWordWrap(True)
        self.sysAdvice_label.setObjectName("sysAdvice_label")
        self.verticalLayout_3.addWidget(self.sysAdvice_label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtGui.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        self.mainPassword_label = QtGui.QLabel(self.page_2)
        self.mainPassword_label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.mainPassword_label.setFont(font)
        self.mainPassword_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainPassword_label.setWordWrap(True)
        self.mainPassword_label.setObjectName("mainPassword_label")
        self.gridLayout.addWidget(self.mainPassword_label, 0, 0, 1, 3)
        self.label_5 = QtGui.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.main_password_lineEdit = QtGui.QLineEdit(self.page_2)
        self.main_password_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.main_password_lineEdit.setText("")
        self.main_password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.main_password_lineEdit.setObjectName("main_password_lineEdit")
        self.gridLayout.addWidget(self.main_password_lineEdit, 1, 1, 1, 1)
        self.mainpassword_checkBox = QtGui.QCheckBox(self.page_2)
        self.mainpassword_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainpassword_checkBox.setObjectName("mainpassword_checkBox")
        self.gridLayout.addWidget(self.mainpassword_checkBox, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.repeat_password_lineEdit = QtGui.QLineEdit(self.page_2)
        self.repeat_password_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.repeat_password_lineEdit.setText("")
        self.repeat_password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.repeat_password_lineEdit.setObjectName("repeat_password_lineEdit")
        self.gridLayout.addWidget(self.repeat_password_lineEdit, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtGui.QLabel(self.page_3)
        self.label_13.setEnabled(True)
        self.label_13.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 3)
        self.label_12 = QtGui.QLabel(self.page_3)
        self.label_12.setEnabled(True)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.host_lineEdit = QtGui.QLineEdit(self.page_3)
        self.host_lineEdit.setEnabled(True)
        self.host_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.host_lineEdit.setText("localhost")
        self.host_lineEdit.setObjectName("host_lineEdit")
        self.gridLayout_2.addWidget(self.host_lineEdit, 1, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.page_3)
        self.label_14.setEnabled(True)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.port_lineEdit = QtGui.QLineEdit(self.page_3)
        self.port_lineEdit.setEnabled(True)
        self.port_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.port_lineEdit.setText("3306")
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.gridLayout_2.addWidget(self.port_lineEdit, 2, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.page_3)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtGui.QGridLayout(self.page_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtGui.QGroupBox(self.page_4)
        self.groupBox.setEnabled(True)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setEnabled(True)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.user_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.user_lineEdit.setEnabled(True)
        self.user_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.user_lineEdit.setText("OMuser")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.gridLayout_5.addWidget(self.user_lineEdit, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setEnabled(True)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)
        self.password_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.password_lineEdit.setEnabled(True)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.password_lineEdit.setText("password")
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout_5.addWidget(self.password_lineEdit, 3, 2, 1, 1)
        self.dbpassword_checkBox = QtGui.QCheckBox(self.groupBox)
        self.dbpassword_checkBox.setEnabled(True)
        self.dbpassword_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dbpassword_checkBox.setObjectName("dbpassword_checkBox")
        self.gridLayout_5.addWidget(self.dbpassword_checkBox, 3, 3, 1, 1)
        self.database_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.database_lineEdit.setEnabled(True)
        self.database_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.database_lineEdit.setText("openmolar_demo")
        self.database_lineEdit.setObjectName("database_lineEdit")
        self.gridLayout_5.addWidget(self.database_lineEdit, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.testDB_pushButton = QtGui.QPushButton(self.groupBox)
        self.testDB_pushButton.setEnabled(True)
        self.testDB_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.testDB_pushButton.setObjectName("testDB_pushButton")
        self.gridLayout_5.addWidget(self.testDB_pushButton, 4, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 5, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 4, 0, 2, 2)
        self.createDemo_radioButton = QtGui.QRadioButton(self.page_4)
        self.createDemo_radioButton.setChecked(True)
        self.createDemo_radioButton.setObjectName("createDemo_radioButton")
        self.gridLayout_3.addWidget(self.createDemo_radioButton, 0, 0, 1, 1)
        self.existingDB_radioButton = QtGui.QRadioButton(self.page_4)
        self.existingDB_radioButton.setObjectName("existingDB_radioButton")
        self.gridLayout_3.addWidget(self.existingDB_radioButton, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.checkBox = QtGui.QCheckBox(self.page_5)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono")
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_4 = QtGui.QGridLayout(self.page_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mainPassword_label_2 = QtGui.QLabel(self.page_6)
        self.mainPassword_label_2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.mainPassword_label_2.setFont(font)
        self.mainPassword_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mainPassword_label_2.setWordWrap(True)
        self.mainPassword_label_2.setObjectName("mainPassword_label_2")
        self.gridLayout_4.addWidget(self.mainPassword_label_2, 0, 0, 1, 3)
        self.label_6 = QtGui.QLabel(self.page_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 4, 1, 1, 1)
        self.rootPassword_lineEdit = QtGui.QLineEdit(self.page_6)
        self.rootPassword_lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.rootPassword_lineEdit.setText("")
        self.rootPassword_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.rootPassword_lineEdit.setObjectName("rootPassword_lineEdit")
        self.gridLayout_4.addWidget(self.rootPassword_lineEdit, 3, 0, 1, 1)
        self.rootPassword_checkBox = QtGui.QCheckBox(self.page_6)
        self.rootPassword_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rootPassword_checkBox.setObjectName("rootPassword_checkBox")
        self.gridLayout_4.addWidget(self.rootPassword_checkBox, 3, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.label_10 = QtGui.QLabel(self.page_7)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.progressBar = QtGui.QProgressBar(self.page_7)
        self.progressBar.setProperty("value", QtCore.QVariant(0))
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_pushButton = QtGui.QPushButton(self.frame)
        self.back_pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.back_pushButton.setObjectName("back_pushButton")
        self.horizontalLayout_3.addWidget(self.back_pushButton)
        self.go_pushButton = QtGui.QPushButton(self.frame)
        self.go_pushButton.setObjectName("go_pushButton")
        self.horizontalLayout_3.addWidget(self.go_pushButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_( u"OpenMolar - First Run"))
        self.title_label.setText(_( u"Welcome to the openMolar settings wizard."))
        self.label_7.setText(_( u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This first run application will </p>\n"
"<ul style=\"-qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">set your system password</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">make this client aware of your mysql server settings</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">install a small (4 patient) demo database if required.</li></ul></body></html>"))
        self.sysAdvice_label.setText(_( u"TextLabel"))
        self.mainPassword_label.setText(_( u"Please enter a password to prevent unauthorised running of this application."))
        self.label_5.setText(_( u"Password"))
        self.mainpassword_checkBox.setText(_( u"show"))
        self.label_8.setText(_( u"Repeat Password"))
        self.label_13.setText(_( u"Where is your mysql server located?  **"))
        self.label_12.setText(_( u"Host"))
        self.label_14.setText(_( u"Port"))
        self.label_9.setText(_( u"** If you do not have a mysql server on your network, please quit this setup, and install mysql server now.\n"
"\n"
"If you are a debian or ubuntu user, \"sudo apt-get install mysql-server\"\n"
"and make a note of the root password you create during set up. "))
        self.groupBox.setTitle(_( u"Database Details"))
        self.label_2.setText(_( u"User"))
        self.label_3.setText(_( u"(mysql)Password"))
        self.dbpassword_checkBox.setText(_( u"show"))
        self.label_4.setText(_( u"Database Name"))
        self.testDB_pushButton.setText(_( u"Test this Connection"))
        self.createDemo_radioButton.setText(_( u"Create A Demo Database"))
        self.existingDB_radioButton.setText(_( u"Use with an existing database"))
        self.label.setText(_( u"OK.... you are all set to go.\n"
"\n"
"When running openMolar, you are presented a login screen.\n"
"\n"
"Password = the one you specified earlier\n"
"User1 = any registered user (demo database has one user \"user\")\n"
"User2 = any registered user (can be left blank)\n"
""))
        self.checkBox.setText(_( u"Launch OpenMolar Now"))
        self.mainPassword_label_2.setText(_( u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To create a database, and set the privileges for user, requires logging into mysql as the root mysql user.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OpenMolar does NOT store this password.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />Please enter the password of the ROOT mysql user.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(note - on most mysql setups, root access is disabled unless the server is on localhost)</p></body></html>"))
        self.label_6.setText(_( u"Root mysql password"))
        self.rootPassword_checkBox.setText(_( u"show"))
        self.label_10.setText(_( u"Creating Database.... please wait"))
        self.back_pushButton.setText(_( u"Back"))
        self.go_pushButton.setText(_( u"Proceed"))

