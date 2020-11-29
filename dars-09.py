"""
19/11/2020

Dasturlash asoslari

#09-dars: FOR LOOP

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print("Salom", mehmon)     
#      print("Hayr,", mehmon)
    
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")
    
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
    
#     print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi

# sonlar = list(range(1,11))
# for son in sonlar:
#       print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#      sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

# print(sonlar)
# print(sonlar_kvadrati)


dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)









