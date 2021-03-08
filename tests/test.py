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
    # OPERATING SYSTEM DETECTION #
except Exception:
    print("Kritik Hata Oluştu Lütfen Log Dosyanızı Kontrol Edin.| "+os.path.dirname(os.path.abspath(__file__))+"\logs\error.log")
    logit("Kütüphaneler Yüklenemedi... Hata Kodu: 0000x1 ")
    sys.exit()
def main():
    start = time.time()
    f = open('settings/config.json','r',encoding='utf-8')
    data = json.loads(f.read())
    # 4 LOOP
    markalar = ["N11","Trendyol","HepsiBurada","GittiGidiyor"]
    
    for marka in markalar:
        print(f"-----------------------{marka.upper()}-----------------------")
        ürün_tag = data["PAZAR_YERI"][marka]["ürün_tag"]
        ürün_adi = data["PAZAR_YERI"][marka]["ürün_adi"]
        fiyat = data["PAZAR_YERI"][marka]["fiyat"]
        fiyat_tag = data["PAZAR_YERI"][marka]["fiyat_tag"]
        sayfa = data["PAZAR_YERI"][marka]["sayfa"]
        link = data["PAZAR_YERI"][marka]["link"]
        a = 0
        with open("data.json", "r",encoding='utf-8') as file:
            data = json.load(file)
            # 2 LOOP
        for query in data["PAZAR_YERI"]["URUN_GRUBU"][0]["URUNLER"]:
            abc = query.upper()
            # 5 LOOP
            for x in range(5): 
                s = requests.Session()
                print(f"{x+1}.Sayfada - {abc} Aranıyor...")
                r = s.get(f"{link}{abc}{sayfa}{x}").text
                soup = BeautifulSoup(r, 'html.parser')
                c = soup.find_all(f"{ürün_tag}",class_=f"{ürün_adi}")
                n = soup.find_all(f"{fiyat_tag}",class_=f"{fiyat}")
                print(f"-----------------------{marka.upper()}-----------------------")
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
            s.close()
    ques(kill,main)
        
main()
# --  N11 SCRAPER -- #