# --  N11 SCRAPER -- #
try:
    # IMPORTING LIB'S #
    import requests
    from bs4 import BeautifulSoup
    import csv
    import os
    import sys
    import time
    import json
    from src.assets.killer import kill
    from src.assets.exques import ques
    from src.assets.logger import logit,loget
    #from src.assets.logger import error_tester
    # OPERATING SYSTEM DETECTION #
except Exception:
    print("Kritik Hata Oluştu Lütfen Log Dosyanızı Kontrol Edin.| "+os.path.dirname(os.path.abspath(__file__))+"\logs\error.log")
    logit("Kütüphaneler Yüklenemedi... Hata Kodu: 0000x1 ")
    sys.exit()
def main():
    start = time.time()
    f = open('settings/config.json','r',encoding='utf-8')
    data1 = json.loads(f.read())
    i = open('settings/general.json','r',encoding='utf-8')
    data2 = json.loads(i.read())
    minfiyat = data2["Ayarlar"]["Genel"]["fiyat_min"]
    maxfiyat = data2["Ayarlar"]["Genel"]["fiyat_max"]
    # 4 LOOP
    markalar = ["N11","Trendyol","HepsiBurada","GittiGidiyor"]
    for marka in markalar:
        print(f"-----------------------{marka.upper()}-----------------------")
        if marka == "Trendyol" or marka == "HepsiBurada":
            ürün_tag = data1["PAZAR_YERI"][marka]["ürün_tag"]
            ürün_adi = data1["PAZAR_YERI"][marka]["ürün_adi"]
            fiyat = data1["PAZAR_YERI"][marka]["fiyat"]
            fiyat_tag = data1["PAZAR_YERI"][marka]["fiyat_tag"]
            sayfa = data1["PAZAR_YERI"][marka]["sayfa"]
            link = data1["PAZAR_YERI"][marka]["link"]
            aralik = data1["PAZAR_YERI"][marka]["aralik"]
        else:
            ürün_tag = data1["PAZAR_YERI"][marka]["ürün_tag"]
            ürün_adi = data1["PAZAR_YERI"][marka]["ürün_adi"]
            fiyat = data1["PAZAR_YERI"][marka]["fiyat"]
            fiyat_tag = data1["PAZAR_YERI"][marka]["fiyat_tag"]
            sayfa = data1["PAZAR_YERI"][marka]["sayfa"]
            link = data1["PAZAR_YERI"][marka]["link"]
            fmin = data1["PAZAR_YERI"][marka]["aralik_min"]
            fmax = data1["PAZAR_YERI"][marka]["aralik_max"]
        a = 0
        with open(data2["Ayarlar"]["Genel"]["ürün_dosyasi"], "r",encoding='utf-8') as file:
            data = json.load(file)
            # 2 LOOP
        for query in data["PAZAR_YERI"]["URUN_GRUBU"][0]["URUNLER"]:
            abc = query.upper()
            # 5 LOOP
            for x in range(data2["Ayarlar"]["Genel"]["sayfa_sayisi"]): 
                s = requests.Session()
                if marka == "Trendyol" or marka == "HepsiBurada":
                    print(f"{x+1}.Sayfada - {abc} Aranıyor...")
                    r = s.get(f"{link}{abc}{sayfa}{x}{aralik}{minfiyat}-{maxfiyat}").text
                    soup = BeautifulSoup(r, 'html.parser')
                    c = soup.find_all(f"{ürün_tag}",class_=f"{ürün_adi}")
                    n = soup.find_all(f"{fiyat_tag}",class_=f"{fiyat}")
                else:
                    print(f"{x+1}.Sayfada - {abc} Aranıyor...")
                    r = s.get(f"{link}{abc}{sayfa}{x}{fmin}{minfiyat}&{fmax}{maxfiyat}").text
                    soup = BeautifulSoup(r, 'html.parser')
                    c = soup.find_all(f"{ürün_tag}",class_=f"{ürün_adi}")
                    n = soup.find_all(f"{fiyat_tag}",class_=f"{fiyat}")
                #print(f"-----------------------{marka.upper()}-----------------------")
                for st,nt in zip(c,n):
                    a += 1
                    csvfile = open('output/ürünler.csv', 'a',encoding='utf-8')
                    ürünadi = st.text.strip()
                    ürünfiyati = nt.text.strip()
                    writer = csv.writer(csvfile, delimiter='\t', lineterminator='\n', )
                    writer.writerow(["PAZAR",'KOD','URUN', 'FIYAT'])
                    writer.writerow([marka,a,ürünadi,ürünfiyati])
    end = time.time()
    elapsed = end - start
    loget(f"İşlem Başarılı. Toplam Geçen Süre:{int(elapsed)} Saniye.")
        
main()
# --  N11 SCRAPER -- #