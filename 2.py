while True:
    notum=int(input("notunuzu giriniz"))

    if notum>=100 and notum>=90:
        print("AA")
    elif notum>=90 and notum>=80:
        print("BA")
    elif notum>=80 and notum>=70:
        print("BB")
    elif notum>=70 and notum>=60:
        print("BC")
    elif notum>=60 and notum>=50:
        print("CC")
    elif notum>=50 and notum>=40:
        print("CD")
    elif notum>=40 and notum>=0:
        print("DD")
    elif notum>100 or notum<0:
        print("bele bir not yok")

