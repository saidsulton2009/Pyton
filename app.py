# # for yosh in range(5):
# yosh = input("Yoshingizni kiriting ")
# try:
#     yosh = int(yosh)
    
# except ValueError:
    
#     print("Siz faqat butun son kirirta olasiz ")
# else:
#     print(f"siz {2025-yosh} yilda tugulgan ekansiz ")

# try:
#     x = int(input("Son kiriting "))
#     print(10//x)
# except ZeroDivisionError:
#     print("NaN")
# except ValueError:
#     print("Bu yerda faqat son yozish kerek")
# yosh = int(input("Yoshingizni kiriting"))



try:
    malumot = {
        'ism': "ali"
    }
    print(malumot('yosh'))
except:
    print("BU kalit soz mavju emas")