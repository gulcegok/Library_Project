# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kitap_ekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KitapEkleForm(object):
    def setupUi(self, KitapEkleForm):
        KitapEkleForm.setObjectName("KitapEkleForm")
        KitapEkleForm.resize(400, 300)
        self.kitapKayitButton = QtWidgets.QPushButton(KitapEkleForm)
        self.kitapKayitButton.setGeometry(QtCore.QRect(232, 230, 101, 31))
        self.kitapKayitButton.setObjectName("kitapKayitButton")
        self.formLayoutWidget = QtWidgets.QWidget(KitapEkleForm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 19, 261, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.kitapAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kitapAdLabel.setObjectName("kitapAdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kitapAdLabel)
        self.KitapLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.KitapLineEdit.setObjectName("KitapLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.KitapLineEdit)
        self.kitapYazariLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kitapYazariLabel.setObjectName("kitapYazariLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kitapYazariLabel)
        self.kitapYazariLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kitapYazariLineEdit.setObjectName("kitapYazariLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kitapYazariLineEdit)
        self.okunmaDurumuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.okunmaDurumuLabel.setObjectName("okunmaDurumuLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.okunmaDurumuLabel)
        self.okunmaDurumuCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.okunmaDurumuCheckBox.setObjectName("okunmaDurumuCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.okunmaDurumuCheckBox)
        self.beEniDurumuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.beEniDurumuLabel.setObjectName("beEniDurumuLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.beEniDurumuLabel)
        self.beEniDurumuComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.beEniDurumuComboBox.setObjectName("beEniDurumuComboBox")
        self.beEniDurumuComboBox.addItem("")
        self.beEniDurumuComboBox.addItem("")
        self.beEniDurumuComboBox.addItem("")
        self.beEniDurumuComboBox.addItem("")
        self.beEniDurumuComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.beEniDurumuComboBox)
        self.kayitDurumLabel = QtWidgets.QLabel(KitapEkleForm)
        self.kayitDurumLabel.setGeometry(QtCore.QRect(60, 175, 221, 31))
        self.kayitDurumLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.kayitDurumLabel.setObjectName("kayitDurumLabel")

        self.retranslateUi(KitapEkleForm)
        QtCore.QMetaObject.connectSlotsByName(KitapEkleForm)

    def retranslateUi(self, KitapEkleForm):
        _translate = QtCore.QCoreApplication.translate
        KitapEkleForm.setWindowTitle(_translate("KitapEkleForm", "Kitap_Ekle"))
        self.kitapKayitButton.setText(_translate("KitapEkleForm", "Kaydet"))
        self.kitapAdLabel.setText(_translate("KitapEkleForm", "Kitap Adı"))
        self.kitapYazariLabel.setText(_translate("KitapEkleForm", "Yazar Adı"))
        self.okunmaDurumuLabel.setText(_translate("KitapEkleForm", "Okunma Durumu"))
        self.beEniDurumuLabel.setText(_translate("KitapEkleForm", "Beğeni Durumu"))
        self.beEniDurumuComboBox.setItemText(0, _translate("KitapEkleForm", "1"))
        self.beEniDurumuComboBox.setItemText(1, _translate("KitapEkleForm", "2"))
        self.beEniDurumuComboBox.setItemText(2, _translate("KitapEkleForm", "3"))
        self.beEniDurumuComboBox.setItemText(3, _translate("KitapEkleForm", "4"))
        self.beEniDurumuComboBox.setItemText(4, _translate("KitapEkleForm", "5"))
        self.kayitDurumLabel.setText(_translate("KitapEkleForm", "Kayıt Durumu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KitapEkleForm = QtWidgets.QWidget()
    ui = Ui_KitapEkleForm()
    ui.setupUi(KitapEkleForm)
    KitapEkleForm.show()
    sys.exit(app.exec_())