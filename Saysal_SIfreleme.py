alf=[["A","B","C","Ç","D","E"],["F","G","Ğ","H","I","İ"],["J","K","L","M","N","O"],["Ö","P","R","S","Ş","T"],["U","Ü","V","Y","Z"," "],[".",",","?","!",":",";"]]
def Sifrele(metin):
    result=""
    for k in metin:
        for i in range(len(alf)):
            for j in range(len(alf[i])):
                if k.upper()==alf[i][j]:
                    result+=str(i+1)+str(j+1)
    return(result)
            
def Coz(metin):
    metin=str(metin)
    result=""
    for i in range(len(metin)):
        if i%2==0:
            result+=alf[int(metin[i])-1][int(metin[i+1])-1]
    return(result)
def main():
    while True:
        try:
            command=input("Şifrele/Çöz (S/C):").lower()
            if command=="s":
                girdi=input("Şifrelenecek Metin:")
                print(Sifrele(girdi))
            elif command=="c":
                girdi=input("Çözülecek Kombinasyon:")
                print(Coz(girdi))
            else:
                print("Şifrelemek için 'S' Çözmek için 'C' yazınız.")
        except:
            print("Şifrelemek için 'S' Çözmek için 'C' yazınız.")
    return 0
main()
print(Coz(Sifrele("merhaba")))
