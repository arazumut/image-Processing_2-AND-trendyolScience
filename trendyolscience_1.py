import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.parse

URL = "https://www.trendyol.com/"

def fiyat_getir():
    urun_ismi = urun_entry.get()
    urun_ismi = urllib.parse.quote(urun_ismi)  # URL'ye ge�erli hale getir

    son_url = URL + urun_ismi

    request = Request(son_url, headers={"User-Agent": "Mozilla/5.0"})
    html_verisi = urlopen(request).read()

    soup = BeautifulSoup(html_verisi, "html.parser")
    try:
        fiyat = soup.find("span", {"class": "prc-slg"}).text.strip()
        fiyat_label.config(text="�r�n Fiyat�: " + fiyat)
    except Exception as e:
        hata_label.config(text="Hata: �r�n bulunamad� veya fiyat� al�namad�")

# Tkinter penceresi olu�turma
root = tk.Tk()
root.title("Trendyol �r�n Fiyat �ekici")

# �r�n ismi giri� alan�
urun_label = tk.Label(root, text="�r�n �smi:")
urun_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

urun_entry = tk.Entry(root)
urun_entry.grid(row=0, column=1, padx=10, pady=10)

# Fiyat �ek butonu
cek_button = tk.Button(root, text="Fiyat� �ek", command=fiyat_getir)
cek_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Sonu� etiketi
fiyat_label = tk.Label(root, text="")
fiyat_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

hata_label = tk.Label(root, text="")
hata_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

root.mainloop()

