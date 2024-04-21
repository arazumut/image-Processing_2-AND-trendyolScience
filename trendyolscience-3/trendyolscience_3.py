import tkinter as tk
from bs4 import BeautifulSoup
import requests

def fiyat_getir():
    url = urun_url_entry.get()
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', {"class": "p-card-wrppr with-campaign-view"})

    for i, product in enumerate(products, start=1):
        eski_ücret = product.find("div", {"class": "prc-box-orgnl"})
        yeni_ücret = product.find("div", {"class": "prc-box-dscntd"}).text.strip() if product.find("div", {"class": "prc-box-dscntd"}) else "Belirtilmemiþ"
        marka_isim = product.find("span", {"class": "prdct-desc-cntnr-ttl"}).text.strip()
        isim = product.find("span", {"class": "prdct-desc-cntnr-name hasRatings"}).text.strip()

        if eski_ücret:
            eski_ücret = eski_ücret.text.strip()
            result_text = f"{i}. Ürün : {marka_isim} {isim}\nEski fiyatý : {eski_ücret}\nYeni ücreti : {yeni_ücret}\n"
        else:
            result_text = f"{i}. Ürün : {marka_isim} {isim}\nYeni ücreti : {yeni_ücret}\n"
        
        result_text += "-" * 50 + "\n"
        result_textbox.insert(tk.END, result_text)

# Tkinter penceresi oluþturma
root = tk.Tk()
root.title("Trendyol Ürün Fiyat Çekici")

# Ürün URL giriþ alaný
urun_url_label = tk.Label(root, text="Ürün URL'si:")
urun_url_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

urun_url_entry = tk.Entry(root)
urun_url_entry.grid(row=0, column=1, padx=10, pady=10)

# Fiyat çek butonu
cek_button = tk.Button(root, text="Fiyatlarý Çek", command=fiyat_getir)
cek_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Sonuç kutusu
result_textbox = tk.Text(root, height=20, width=50)
result_textbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

