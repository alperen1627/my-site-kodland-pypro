from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def alperen_sagdic():
    return render_template("index.html")

@app.route("/bilgiler")
def bilgi():
    bilgiler = [
        "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
        "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
        "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."
    ]

    return '<p>' + random.choice(bilgiler) + '</p>'

@app.route("/secret")
def secret():
    yazı_tura = ["Yazı", "Tura"]
    return '<p>' + random.choice(yazı_tura) + '</p>'

app.run(debug=True)