
import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_product_info(product_name):
    # Trendyol'dan veri �ekme
    url = f"https://www.trendyol.com/sr?q={product_name.replace(' ', '+')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    
# -----------------------------------------------------------------------------------------------------------------------------------------------------
                        #  By Kamil Umut Araz �nstagram: K.umutarazz   linkedin: Kamil Umut Araz
# -----------------------------------------------------------------------------------------------------------------------------------------------------
    


    # �r�n bilgilerini alma
    product_infos = []
    products = soup.find_all("div", class_="p-card-wrppr")
    for product in products:
        name = product.find("span", class_="prdct-desc-cntnr-name").text.strip()
        price_element = product.find("div", class_="prc-box-sllng")
        if price_element:
            price = price_element.text.strip()
        else:
            price = "Fiyat bilgisi bulunamad�"
        product_infos.append(f"�r�n Ad�: {name}\nFiyat: {price}\n")

    return product_infos

def display_product_info():
    product_name = entry.get()
    product_infos = get_product_info(product_name)
    result_text = "\n".join(product_infos)
    result_label.config(text=result_text)

# Tkinter ile aray�z olu�turma
root = tk.Tk()
root.title("Trendyol �r�n Bilgisi �ekici")

label = tk.Label(root, text="�r�n �smi:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

search_button = tk.Button(root, text="Ara", command=display_product_info)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
