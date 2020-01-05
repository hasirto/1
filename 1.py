#isim=input("isminiz nedir: ")
#print("isminiz: ",isim)
    notum=int(input("notunuzu giriniz: "))
    if notum>90 and notum<100:
        print("AA")
    elif notum>80 and notum<90:
        print("BA")
    elif notum>70 and notum<80:
        print("BB")
    elif notum> 60 and notum<70:
        print("BC")
    elif notum> 50 and notum<60:
        print("CC")
    elif notum> 40 and notum<50:
        print("CD")
    elif notum> 0 and notum<40:
        print("DD")
    elif notum> 100 or notum<0:
        print("Bele bir not yok")