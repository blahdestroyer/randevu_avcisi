import requests
from email_alert import send_email

def randevu_kontrol():
    try:
        # Bu sadece örnek endpoint, gerçek MHRS API yerine sabit veriyle simülasyon yapılır
        url = "https://jsonplaceholder.typicode.com/posts/1"  # Temsili
        response = requests.get(url, timeout=10)

        # Burada normalde MHRS yanıtı parse edilir, örneğin:
        data = response.json()
        if "id" in data:
            send_email("Randevu Bulundu!", "MHRS üzerinden randevu bulundu! Hemen giriş yap!")
        else:
            print("Randevu bulunamadı.")
    except Exception as e:
        print(f"[HATA] Kontrol sırasında hata: {e}")