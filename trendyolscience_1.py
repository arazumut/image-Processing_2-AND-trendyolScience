import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.parse

URL = "https://www.trendyol.com/"

def fiyat_getir():
    urun_ismi = urun_entry.get()
    urun_ismi = urllib.parse.quote(urun_ismi)  # URL'ye geçerli hale getir

    son_url = URL + urun_ismi

    request = Request(son_url, headers={"User-Agent": "Mozilla/5.0"})
    html_verisi = urlopen(request).read()

    soup = BeautifulSoup(html_verisi, "html.parser")
    try:
        fiyat = soup.find("span", {"class": "prc-slg"}).text.strip()
        fiyat_label.config(text="Ürün Fiyatý: " + fiyat)
    except Exception as e:
        hata_label.config(text="Hata: Ürün bulunamadý veya fiyatý alýnamadý")

# Tkinter penceresi oluþturma
root = tk.Tk()
root.title("Trendyol Ürün Fiyat Çekici")

# Ürün ismi giriþ alaný
urun_label = tk.Label(root, text="Ürün Ýsmi:")
urun_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

urun_entry = tk.Entry(root)
urun_entry.grid(row=0, column=1, padx=10, pady=10)

# Fiyat çek butonu
cek_button = tk.Button(root, text="Fiyatý Çek", command=fiyat_getir)
cek_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Sonuç etiketi
fiyat_label = tk.Label(root, text="")
fiyat_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

hata_label = tk.Label(root, text="")
hata_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

root.mainloop()

