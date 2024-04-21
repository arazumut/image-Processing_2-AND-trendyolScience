
import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_product_info(product_name):
    # Trendyol'dan veri çekme
    url = f"https://www.trendyol.com/sr?q={product_name.replace(' ', '+')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ürün bilgilerini alma
    product_infos = []
    products = soup.find_all("div", class_="p-card-wrppr")
    for product in products:
        name = product.find("span", class_="prdct-desc-cntnr-name").text.strip()
        price = product.find("div", class_="prc-box-sllng").text.strip()
        product_infos.append(f"Ürün Adý: {name}\nFiyat: {price}\n")

    return product_infos

    
# -----------------------------------------------------------------------------------------------------------------------------------------------------
                        #  By Kamil Umut Araz Ýnstagram: K.umutarazz   linkedin: Kamil Umut Araz
# -----------------------------------------------------------------------------------------------------------------------------------------------------
    

def display_product_info():
    product_name = entry.get()
    product_infos = get_product_info(product_name)
    result_text = "\n".join(product_infos)
    result_label.config(text=result_text)

# Tkinter ile arayüz oluþturma
root = tk.Tk()
root.title("Trendyol Ürün Bilgisi Çekici")

label = tk.Label(root, text="Ürün Ýsmi:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

search_button = tk.Button(root, text="Ara", command=display_product_info)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
