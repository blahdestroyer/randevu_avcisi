from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Randevu Avcısı Aktif"

if __name__ == "__main__":
    from scheduler import zamanlayici_baslat
    zamanlayici_baslat()
    app.run(host="0.0.0.0", port=10000)  # sahte port
