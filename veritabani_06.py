import sqlite3 as sql
vt = sql.connect('kitaplik_db.sqlite')
imlec = vt.cursor()

def k_giris(eposta,sifre):
    imlec.execute("CREATE TABLE IF NOT EXISTS kullanici_db (kullanici_id INTEGER PRIMARY KEY  AUTOINCREMENT, eposta TEXT Unique,sifre)")
#    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kullanici_girisi = "INSERT INTO kullanici_db (eposta,sifre) VALUES ('"+eposta+"','"+str(sifre)+"')"
    imlec.execute(kullanici_girisi)
    vt.commit()
    try:
        imlec.execute("SELECT * FROM kullanici_db where eposta='{}' and sifre='{}'".format(eposta,sifre))
        kullanici_id = imlec.fetchall()[0][1]
        return kullanici_id
    except:
        print("böyle bir kullanıcı yok")
        return 0
    
# def kekle(eposta,sifre):
    



def ekle(k_id,kitap_adi="",kitap_yazari="",okunma_durumu="",begeni=""):
    imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik_db (k_id INTEGER, kitap_id INTEGER PRIMARY KEY  AUTOINCREMENT, kitap_adi,kitap_yazari,okunma_durumu,begeni)")
#    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kitap_girisi = "INSERT INTO kitaplik_db (k_id,kitap_adi,kitap_yazari,okunma_durumu,begeni) VALUES ('{}','{}','{}','{}','{}')".format(k_id,kitap_adi,kitap_yazari,okunma_durumu,begeni)
#    print(kitap_girisi)
    imlec.execute(kitap_girisi)
    vt.commit()
    return 1


def listele(k_id):
    imlec.execute("SELECT * FROM kitaplik_db where k_id='{}'".format(k_id))
    kitaplar = imlec.fetchall()
    print(kitaplar)
    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")
    return kitaplar

def guncelle(guncellenecek):
    gkitap = input("Güncel kitap adını giriniz")
    gyazar = input("Güncel kitap yazarını")
    gokunma = input("Güncel kitap okunma durumunu giriniz")
    gbegeni = input("Güncel kitap beğeni değerini giriniz")
    guncelleme_kodu = "UPDATE kitaplik_db SET kitap_adi='"+gkitap+"',kitap_yazari='"+gyazar+"',okunma_durumu='"+gokunma+"',begeni='"+gbegeni+"' WHERE kitap_id = '"+guncellenecek+"'"
    imlec.execute(guncelleme_kodu)
    vt.commit()
def sil(silinecek):
    silme_kodu="DELETE FROM kitaplik_db WHERE kitap_id='"+silinecek+"'"
    imlec.execute(silme_kodu)
    vt.commit()
def cikis():
    vt.close()
    print("Çıkış Yapıldı İyi Günler")