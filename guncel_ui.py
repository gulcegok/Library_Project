# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guncel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Guncel_Kitap(object):
    def setupUi(self, Guncel_Kitap):
        Guncel_Kitap.setObjectName("Guncel_Kitap")
        Guncel_Kitap.resize(400, 300)
        self.guncelid_label = QtWidgets.QLabel(Guncel_Kitap)
        self.guncelid_label.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.guncelid_label.setObjectName("guncelid_label")
        self.guncel_id = QtWidgets.QLineEdit(Guncel_Kitap)
        self.guncel_id.setGeometry(QtCore.QRect(270, 20, 113, 22))
        self.guncel_id.setObjectName("guncel_id")
        self.giris_button = QtWidgets.QPushButton(Guncel_Kitap)
        self.giris_button.setGeometry(QtCore.QRect(270, 240, 93, 28))
        self.giris_button.setObjectName("giris_button")
        self.mesaj_label = QtWidgets.QLabel(Guncel_Kitap)
        self.mesaj_label.setGeometry(QtCore.QRect(70, 250, 55, 16))
        self.mesaj_label.setObjectName("mesaj_label")
        self.guncelad_label = QtWidgets.QLabel(Guncel_Kitap)
        self.guncelad_label.setGeometry(QtCore.QRect(10, 60, 241, 16))
        self.guncelad_label.setObjectName("guncelad_label")
        self.guncelyazar_label = QtWidgets.QLabel(Guncel_Kitap)
        self.guncelyazar_label.setGeometry(QtCore.QRect(10, 100, 211, 16))
        self.guncelyazar_label.setObjectName("guncelyazar_label")
        self.guncelokunma_label = QtWidgets.QLabel(Guncel_Kitap)
        self.guncelokunma_label.setGeometry(QtCore.QRect(10, 140, 241, 16))
        self.guncelokunma_label.setObjectName("guncelokunma_label")
        self.guncelbegeni_label = QtWidgets.QLabel(Guncel_Kitap)
        self.guncelbegeni_label.setGeometry(QtCore.QRect(10, 180, 221, 16))
        self.guncelbegeni_label.setObjectName("guncelbegeni_label")
        self.guncel_ad = QtWidgets.QLineEdit(Guncel_Kitap)
        self.guncel_ad.setGeometry(QtCore.QRect(270, 60, 113, 22))
        self.guncel_ad.setObjectName("guncel_ad")
        self.guncel_yazar = QtWidgets.QLineEdit(Guncel_Kitap)
        self.guncel_yazar.setGeometry(QtCore.QRect(270, 100, 113, 22))
        self.guncel_yazar.setObjectName("guncel_yazar")
        self.guncel_okunma = QtWidgets.QLineEdit(Guncel_Kitap)
        self.guncel_okunma.setGeometry(QtCore.QRect(270, 140, 113, 22))
        self.guncel_okunma.setObjectName("guncel_okunma")
        self.guncel_begeni = QtWidgets.QLineEdit(Guncel_Kitap)
        self.guncel_begeni.setGeometry(QtCore.QRect(270, 180, 113, 22))
        self.guncel_begeni.setObjectName("guncel_begeni")

        self.retranslateUi(Guncel_Kitap)
        QtCore.QMetaObject.connectSlotsByName(Guncel_Kitap)

    def retranslateUi(self, Guncel_Kitap):
        _translate = QtCore.QCoreApplication.translate
        Guncel_Kitap.setWindowTitle(_translate("Guncel_Kitap", "Form"))
        self.guncelid_label.setText(_translate("Guncel_Kitap", "Güncellenecek kitabın id numarasını girin:"))
        self.giris_button.setText(_translate("Guncel_Kitap", "Giriş"))
        self.mesaj_label.setText(_translate("Guncel_Kitap", "Mesaj"))
        self.guncelad_label.setText(_translate("Guncel_Kitap", "Güncellenecek kitabın adını girin:"))
        self.guncelyazar_label.setText(_translate("Guncel_Kitap", "Güncellenecek kitabın yazarını girin:"))
        self.guncelokunma_label.setText(_translate("Guncel_Kitap", "Güncel okunma durumunu girin:"))
        self.guncelbegeni_label.setText(_translate("Guncel_Kitap", "Güncel beğeni durumunu girin:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Guncel_Kitap = QtWidgets.QWidget()
    ui = Ui_Guncel_Kitap()
    ui.setupUi(Guncel_Kitap)
    Guncel_Kitap.show()
    sys.exit(app.exec_())
