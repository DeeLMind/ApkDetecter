# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apkdetecter_ui.ui'
#
# Created: Sun Jan 18 22:26:54 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_APKDetecter(object):
    def setupUi(self, APKDetecter):
        APKDetecter.setObjectName(_fromUtf8("APKDetecter"))
        APKDetecter.setWindowModality(QtCore.Qt.WindowModal)
        APKDetecter.setEnabled(True)
        APKDetecter.resize(432, 237)
        APKDetecter.setMinimumSize(QtCore.QSize(432, 237))
        APKDetecter.setMaximumSize(QtCore.QSize(432, 237))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Andy/Desktop/20150117051304968_easyicon_net_512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        APKDetecter.setWindowIcon(icon)
        self.lab_file = QtGui.QLabel(APKDetecter)
        self.lab_file.setGeometry(QtCore.QRect(10, 10, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_file.setFont(font)
        self.lab_file.setObjectName(_fromUtf8("lab_file"))
        self.te_path = QtGui.QTextBrowser(APKDetecter)
        self.te_path.setGeometry(QtCore.QRect(50, 5, 291, 24))
        self.te_path.setObjectName(_fromUtf8("te_path"))
        self.file_open = QtGui.QPushButton(APKDetecter)
        self.file_open.setGeometry(QtCore.QRect(350, 5, 71, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.file_open.setFont(font)
        self.file_open.setObjectName(_fromUtf8("file_open"))
        self.groupBox = QtGui.QGroupBox(APKDetecter)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 411, 181))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arabic Typesetting"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lab_linksize = QtGui.QLabel(self.groupBox)
        self.lab_linksize.setGeometry(QtCore.QRect(210, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_linksize.setFont(font)
        self.lab_linksize.setObjectName(_fromUtf8("lab_linksize"))
        self.lab_dex_flag = QtGui.QLabel(self.groupBox)
        self.lab_dex_flag.setGeometry(QtCore.QRect(10, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_dex_flag.setFont(font)
        self.lab_dex_flag.setObjectName(_fromUtf8("lab_dex_flag"))
        self.lab_dexheader_size = QtGui.QLabel(self.groupBox)
        self.lab_dexheader_size.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_dexheader_size.setFont(font)
        self.lab_dexheader_size.setObjectName(_fromUtf8("lab_dexheader_size"))
        self.te_endiantag = QtGui.QTextBrowser(self.groupBox)
        self.te_endiantag.setEnabled(False)
        self.te_endiantag.setGeometry(QtCore.QRect(80, 104, 111, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.te_endiantag.setFont(font)
        self.te_endiantag.setFrameShape(QtGui.QFrame.Panel)
        self.te_endiantag.setObjectName(_fromUtf8("te_endiantag"))
        self.lab_linkoff = QtGui.QLabel(self.groupBox)
        self.lab_linkoff.setGeometry(QtCore.QRect(210, 111, 71, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_linkoff.setFont(font)
        self.lab_linkoff.setObjectName(_fromUtf8("lab_linkoff"))
        self.te_linkoff = QtGui.QTextBrowser(self.groupBox)
        self.te_linkoff.setEnabled(False)
        self.te_linkoff.setGeometry(QtCore.QRect(292, 103, 111, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.te_linkoff.setFont(font)
        self.te_linkoff.setFrameShape(QtGui.QFrame.Panel)
        self.te_linkoff.setObjectName(_fromUtf8("te_linkoff"))
        self.lab_file_size = QtGui.QLabel(self.groupBox)
        self.lab_file_size.setGeometry(QtCore.QRect(212, 32, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_file_size.setFont(font)
        self.lab_file_size.setObjectName(_fromUtf8("lab_file_size"))
        self.te_linksize = QtGui.QTextBrowser(self.groupBox)
        self.te_linksize.setEnabled(False)
        self.te_linksize.setGeometry(QtCore.QRect(292, 63, 111, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.te_linksize.setFont(font)
        self.te_linksize.setFrameShape(QtGui.QFrame.Panel)
        self.te_linksize.setObjectName(_fromUtf8("te_linksize"))
        self.te_dexheader_size = QtGui.QTextBrowser(self.groupBox)
        self.te_dexheader_size.setEnabled(False)
        self.te_dexheader_size.setGeometry(QtCore.QRect(80, 63, 111, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.te_dexheader_size.setFont(font)
        self.te_dexheader_size.setFrameShape(QtGui.QFrame.Panel)
        self.te_dexheader_size.setObjectName(_fromUtf8("te_dexheader_size"))
        self.te_file_size = QtGui.QTextBrowser(self.groupBox)
        self.te_file_size.setEnabled(False)
        self.te_file_size.setGeometry(QtCore.QRect(292, 22, 111, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.te_file_size.setFont(font)
        self.te_file_size.setFrameShape(QtGui.QFrame.Panel)
        self.te_file_size.setObjectName(_fromUtf8("te_file_size"))
        self.lab_endiantag = QtGui.QLabel(self.groupBox)
        self.lab_endiantag.setGeometry(QtCore.QRect(10, 113, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_endiantag.setFont(font)
        self.lab_endiantag.setObjectName(_fromUtf8("lab_endiantag"))
        self.te_protect = QtGui.QTextBrowser(self.groupBox)
        self.te_protect.setEnabled(False)
        self.te_protect.setGeometry(QtCore.QRect(12, 140, 391, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.te_protect.setFont(font)
        self.te_protect.setFrameShape(QtGui.QFrame.Panel)
        self.te_protect.setObjectName(_fromUtf8("te_protect"))
        self.te_dex_flag = QtGui.QTextEdit(self.groupBox)
        self.te_dex_flag.setEnabled(False)
        self.te_dex_flag.setGeometry(QtCore.QRect(80, 22, 111, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.te_dex_flag.setFont(font)
        self.te_dex_flag.setFrameShape(QtGui.QFrame.Panel)
        self.te_dex_flag.setObjectName(_fromUtf8("te_dex_flag"))
        self.progressBar = QtGui.QProgressBar(APKDetecter)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 217, 191, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.extend_info = QtGui.QPushButton(APKDetecter)
        self.extend_info.setGeometry(QtCore.QRect(275, 214, 71, 20))
        self.extend_info.setObjectName(_fromUtf8("extend_info"))
        self.about_info = QtGui.QPushButton(APKDetecter)
        self.about_info.setGeometry(QtCore.QRect(350, 214, 71, 20))
        self.about_info.setObjectName(_fromUtf8("about_info"))
        self.apk_info = QtGui.QPushButton(APKDetecter)
        self.apk_info.setGeometry(QtCore.QRect(200, 214, 71, 20))
        self.apk_info.setObjectName(_fromUtf8("apk_info"))

        self.retranslateUi(APKDetecter)
        QtCore.QMetaObject.connectSlotsByName(APKDetecter)

    def retranslateUi(self, APKDetecter):
        APKDetecter.setWindowTitle(_translate("APKDetecter", "APKDetecter", None))
        self.lab_file.setText(_translate("APKDetecter", "文 件", None))
        self.file_open.setText(_translate("APKDetecter", "打  开", None))
        self.groupBox.setTitle(_translate("APKDetecter", "DEX信息", None))
        self.lab_linksize.setText(_translate("APKDetecter", "连接段大小", None))
        self.lab_dex_flag.setText(_translate("APKDetecter", "DEX 标 识", None))
        self.lab_dexheader_size.setText(_translate("APKDetecter", "DEX头大小", None))
        self.lab_linkoff.setText(_translate("APKDetecter", "连接段偏移", None))
        self.lab_file_size.setText(_translate("APKDetecter", "文件大小", None))
        self.lab_endiantag.setText(_translate("APKDetecter", "字节序列", None))
        self.extend_info.setText(_translate("APKDetecter", "扩展信息", None))
        self.about_info.setText(_translate("APKDetecter", "About", None))
        self.apk_info.setText(_translate("APKDetecter", "ApkInfo", None))

