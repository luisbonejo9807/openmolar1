# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar/qt-designer/confirmDentist.ui'
#
# Created: Mon Aug 10 22:30:46 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 189)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dents_comboBox = QtGui.QComboBox(Dialog)
        self.dents_comboBox.setObjectName("dents_comboBox")
        self.gridLayout.addWidget(self.dents_comboBox, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.previousCourse_radioButton = QtGui.QRadioButton(Dialog)
        self.previousCourse_radioButton.setObjectName("previousCourse_radioButton")
        self.gridLayout.addWidget(self.previousCourse_radioButton, 1, 0, 1, 2)
        self.newCourse_radioButton = QtGui.QRadioButton(Dialog)
        self.newCourse_radioButton.setChecked(True)
        self.newCourse_radioButton.setObjectName("newCourse_radioButton")
        self.gridLayout.addWidget(self.newCourse_radioButton, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Which Dentist", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Print a GP17 form using this dentist\'s contract no? ", None, QtGui.QApplication.UnicodeUTF8))
        self.previousCourse_radioButton.setText(QtGui.QApplication.translate("Dialog", "Previous Course (00/00/0000 - 00/00/0000)", None, QtGui.QApplication.UnicodeUTF8))
        self.newCourse_radioButton.setText(QtGui.QApplication.translate("Dialog", "New Course ( no dates)", None, QtGui.QApplication.UnicodeUTF8))

