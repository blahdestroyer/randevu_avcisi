from kontrol import randevu_kontrol
import time

def zamanlayici_baslat():
    while True:
        print("[ZAMANLAYICI] Randevu kontrolü başlatıldı.")
        randevu_kontrol()
        print("[ZAMANLAYICI] 5 dakika bekleniyor...")
        time.sleep(300)