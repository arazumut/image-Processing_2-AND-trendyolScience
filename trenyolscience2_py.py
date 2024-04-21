import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.trendyol.com/erkek-spor-ayakkabi-x-g2-c109").content

soup = BeautifulSoup(html,'html.parser')

g = 1
x = soup.find_all('div',{"class":"p-card-wrppr with-campaign-view"})
for a in x:
    eski_ücret = a.find("div", {"class": "prc-box-orgnl"})


    yeni_ücret =  a.find("div",{"class":"prc-box-dscntd"})
    yeni_ücret = str(yeni_ücret).split('>')[1]
    yeni_ücret = yeni_ücret.replace('</div','')

    marka_isim = a.find("span",{"class":"prdct-desc-cntnr-ttl"})
    marka_isim = str(marka_isim).split('"')[3]

    isim = a.find("span", {"class": "prdct-desc-cntnr-name hasRatings"})
    isim = str(isim).split('"')[3]
    if eski_ücret == None:
        print(
            str(g) + '. Ürün : ' + marka_isim + ' ' + isim + ' ' + '\n' + 'Yeni ücreti : ' + yeni_ücret)
    else:
        eski_ücret = str(eski_ücret).split('>')[1]
        eski_ücret = eski_ücret.replace('</div', '')
        print(str(g)+'. Ürün : ' + marka_isim +' ' + isim +' ' + '\n'+'Eski fiyatı : ' +  eski_ücret + '\n' + 'Yeni ücreti : ' + yeni_ücret )
    g = g +1
