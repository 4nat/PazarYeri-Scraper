
def ques(kill,main):
    print("Tarama Tamamlandı.")
    print("Çıkış yapmak istiyor musunuz?")
    print("1 = Yeniden ara\n2 = Çıkış")
    sel = input(">>> ")
    if sel == "1":
        main()
    else:
        print(kill())