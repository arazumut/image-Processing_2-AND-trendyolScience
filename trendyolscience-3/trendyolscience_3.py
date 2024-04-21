import tkinter as tk
from bs4 import BeautifulSoup
import requests

def fiyat_getir():
    url = urun_url_entry.get()
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', {"class": "p-card-wrppr with-campaign-view"})

    for i, product in enumerate(products, start=1):
        eski_�cret = product.find("div", {"class": "prc-box-orgnl"})
        yeni_�cret = product.find("div", {"class": "prc-box-dscntd"}).text.strip() if product.find("div", {"class": "prc-box-dscntd"}) else "Belirtilmemi�"
        marka_isim = product.find("span", {"class": "prdct-desc-cntnr-ttl"}).text.strip()
        isim = product.find("span", {"class": "prdct-desc-cntnr-name hasRatings"}).text.strip()

        if eski_�cret:
            eski_�cret = eski_�cret.text.strip()
            result_text = f"{i}. �r�n : {marka_isim} {isim}\nEski fiyat� : {eski_�cret}\nYeni �creti : {yeni_�cret}\n"
        else:
            result_text = f"{i}. �r�n : {marka_isim} {isim}\nYeni �creti : {yeni_�cret}\n"
        
        result_text += "-" * 50 + "\n"
        result_textbox.insert(tk.END, result_text)

# Tkinter penceresi olu�turma
root = tk.Tk()
root.title("Trendyol �r�n Fiyat �ekici")

# �r�n URL giri� alan�
urun_url_label = tk.Label(root, text="�r�n URL'si:")
urun_url_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

urun_url_entry = tk.Entry(root)
urun_url_entry.grid(row=0, column=1, padx=10, pady=10)

# Fiyat �ek butonu
cek_button = tk.Button(root, text="Fiyatlar� �ek", command=fiyat_getir)
cek_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Sonu� kutusu
result_textbox = tk.Text(root, height=20, width=50)
result_textbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

