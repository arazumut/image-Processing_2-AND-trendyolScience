import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.trendyol.com/erkek-spor-ayakkabi-x-g2-c109").content

soup = BeautifulSoup(html,'html.parser')

g = 1
x = soup.find_all('div',{"class":"p-card-wrppr with-campaign-view"})
for a in x:
    eski_�cret = a.find("div", {"class": "prc-box-orgnl"})


    yeni_�cret =  a.find("div",{"class":"prc-box-dscntd"})
    yeni_�cret = str(yeni_�cret).split('>')[1]
    yeni_�cret = yeni_�cret.replace('</div','')

    marka_isim = a.find("span",{"class":"prdct-desc-cntnr-ttl"})
    marka_isim = str(marka_isim).split('"')[3]

    isim = a.find("span", {"class": "prdct-desc-cntnr-name hasRatings"})
    isim = str(isim).split('"')[3]
    if eski_�cret == None:
        print(
            str(g) + '. �r�n : ' + marka_isim + ' ' + isim + ' ' + '\n' + 'Yeni �creti : ' + yeni_�cret)
    else:
        eski_�cret = str(eski_�cret).split('>')[1]
        eski_�cret = eski_�cret.replace('</div', '')
        print(str(g)+'. �r�n : ' + marka_isim +' ' + isim +' ' + '\n'+'Eski fiyat� : ' +  eski_�cret + '\n' + 'Yeni �creti : ' + yeni_�cret )
    g = g +1
