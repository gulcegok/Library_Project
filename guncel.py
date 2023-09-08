import sys
from PyQt5.QtWidgets import *
from guncel_ui import Ui_Guncel_Kitap
import veritabani_06 as baglanti
class GuncelPenceresi(Ui_Guncel_Kitap):
    def __init__(self,k_id):
        super().__init__()
        self.k_id = k_id
        self.setupUi(self)
        self.giris_button.clicked.connect(self.GuncelKontrol)

    def Guncel_Kitap(self):
            self.mesaj_label.setText("Giriş Butonu Tıklandı")
            guncel_id = self.guncel_id.text()
            self.k_id=guncel_id
            guncel_ad = self.guncel_ad.text()
            guncel_yazar = self.guncel_yazar.text()
            guncel_okunma = self.guncel_okunma.text() 
            guncel_begeni = self.guncel_begeni.text()
            sonuc = baglanti.guncelle(guncel_id,guncel_ad,guncel_yazar,guncel_okunma, guncel_begeni)
            # baglanti.guncelle(guncel_id)
            # self.gkitap = guncel_ad
            # self.gyazar = guncel_yazar
            # self.gokunma = guncel_okunma
            # self.gbegeni= guncel_begeni
            

            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GuncelPenceresi()
    pencere.show()
    sys.exit(app.exec_())
