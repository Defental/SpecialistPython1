f = False
while(f!=True):
    s = input("NxM")
    try:
        n=0
        m=0
        n = s[:s.find("x")]
        m = s[s.find("x")+1:]
        print(int(n)/int(m))
        t = True
    except ValueError:
        print("Неправильный формат!")
