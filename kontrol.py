import requests
from email_alert import send_email

def randevu_kontrol():
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url, timeout=10)
        data = response.json()

        if "id" in data:
            send_email("Randevu Bulundu!", "MHRS üzerinden randevu bulundu! Hemen giriş yap!")
        else:
            print("Randevu bulunamadı.")
    except Exception as e:
        print(f"[HATA] Kontrol sırasında hata: {e}")