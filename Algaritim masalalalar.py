# # 1-masala
# # harorat = float(input("Haroratni kiriting: "))
# # if harorat < 50:
# #     if harorat > 30:
# #         print("Yengil kiyim kiying!")
# #     elif 15 < harorat < 30:
# #         print("Yengil kurtka kiying!")
# #     else:
# #         print("Issiq kiyim kiying!")
# # else:
# #     print("Bunday haroratda yashab bo'lmaydi.")
#
# # # 1-masala
# # ball = float(input("Ballni kiriting: "))
# # if 0 < ball < 100:
# #     if 90 <= ball < 100:
# #         print("A'lo baxo")
# #     elif 80 <= ball < 90:
# #         print("Yaxshi baxo!")
# #     elif 70 <= ball < 80:
# #         print("Qoniqarli baxo!")
# #     elif 60 <= ball < 70:
# #         print("Qoniqarsiz baxo!")
# #     else:
# #         print("Imtihondan yiqildingiz")
# # else:
# #     print("Qiymat xato kiritildi.\nMaksimal ball 100 ball")
# #-----------------------------------------------------------------------------------------
# # # 1-masala
# # s = input("Xarid summasini kiriting: ")
# # if s.isdigit():
# #     summa = int(s)
# #     if summa < 50000:
# #         print("Chegirma yo'q!")
# #     elif summa < 100000:
# #         print("5% chegirma!")
# #     elif summa < 200000:
# #         print("10% chegirma!")
# #     else:
# #         print("15% chegirma!")
# # else:
# #     print("Hurmatli foydalanuvchi, iltimos faqat raqam kiriting!")
# #
# # # 2-masala-----------------------------------------------
# # rang = input("Chiroq rangi kiriting (qizil, sariq, yashil): ")
# # if rang.isalpha():
# #     if rang == "qizil":
# #         print("To‘xtang")
# #     elif rang == "sariq":
# #         print("Tayyorlaning")
# #     elif rang == "yashil":
# #         print("Yuring")
# #     else:
# #         print("Noto‘g‘ri chiroq rangi kiritildi!")
# # else:
# #     print("Noto‘g‘ri chiroq rangi kiritildi!")
# #
# # # 3-masala-----------------------------------------------
# # soat = input("Soatni kiriting: ")
# # if soat.isdigit():
# #     sat = int(soat)
# #     if 6 < sat < 11:
# #         print("Ertalabki dori!")
# #     elif 12 < sat < 17:
# #         print("Kunduzgi dori!")
# #     elif 18 < sat < 23:
# #         print("Kechki dori!")
# #     else:
# #         print("Dori ichish vaqti emas!")
# # else:
# #     print("Soat noto‘g‘ri kiritildi!")
#
# # x# 4-masala-----------------------------------------------
# # harorat = float(input("Haroratni kiriting: "))
# # if harorat < 50:
# #     if harorat > 30:
# #         print("Yengil kiyim kiying!")
# #     elif 15 < harorat < 30:
# #         print("Yengil kurtka kiying!")
# #     else:
# #         print("Issiq kiyim kiying!")
# # else:
# #     print("Bunday haroratda yashab bo'lmaydi.")
#
# # 5-masala-----------------------------------------------
#
# # ogirlik = input("kilogrammni kiriting: ")
# #
# # if ogirlik.isdigit():
# #     sumka = int(ogirlik)
# #     if 1 > sumka > 4:
# #         print("Og'ir, kamaytiring!")
# #     elif 5 > sumka > 9:
# #         print("Og'ir kamaytiring!")
# #     else:
# #         print("Juda og'ir")
# # else:
# #     print("Qiymatni to'g'ri kiriting!")
#
# # 6-masala-----------------------------------------------
#
# # yosh = input("yoshni kiriting: ")
# # holat = input("Holatni kiriting: ")
# #
# # yoshi = int(yosh)
# #
# # if holat == "og'ir":
# #     print("zudlik bilan!")
# #     if 10 < yoshi > 70:
# #         print("1 soat ichida!")
# #     else:
# #         print("3 soat ichida!")
# # else:
# #     print("iymatni to'g'ri kiriting!")
#
# # 7-masala---------------------------------------------
#
# # kunlar = input("Bugun qanday kun (ish / dam olish): ").lower()
# # masofa = float(input("Masofani kiriting (km): "))
# #
# # if kunlar == "dam olish":
# #     km_narxi = 3600
# # else:
# #     print("3000 so'm")
# #
# # umumiy_narx = km_narxi * masofa
# #
# # if masofa > 10:
# #     print(f"umumiy_narxi = {umumiy_narx * 0.9}")
# #     print(umumiy_narxi)
#
# # 8-masala---------------------------------------------
#
# Ob_havo = float(input("Ob_havoni kiriting: "))
# yomgir_ehtimoli = float(input("Yomg‘ir yog'ish ehtimolini kiriting: "))
#
# if yomgir_ehtimoli >= 70:
#     print("Uyda qoling")
# elif harorat < 5:
#     print("Juda sovuq, sayr qilish tavsiya etilmaydi")
# else:
#     print("Ajoyib kun, sayrga boring!")
#
# # 9-masala---------------------------------------------
#
# daromad = float(input("Oylik daromadingizni kiriting: "))
# xarajat = float(input("Oylik xarajatlaringizni kiriting: "))
# if xarajat > daromad:
#     print("Xavfli! Xarajatlarni kamaytiring")
# elif xarajat == daromad:
#     print("Aynan yetarli")
# else:
#     print("Ajoyib! Tejamkorlik qilyapsiz")

# # 10-masala---------------------------------------------

# velosiped = input("velosiped turini kiriting (shahar yoki sport): ")
# vaqt = int(input("Necha soatGA IJARAGA OLDINGIZ: "))
# city = "shahar, ahaxar"
# if velosiped in city:
#     if vaqt >= 5:
#         print(f"sizga 20% chegirma berilai! umumiy summa {(vaqt * 10000) * 0,8} so'm")
#     elif vaqt >= 3:
#         print(f"sizga 10% chegirma berilai! umumiy summa {(vaqt * 10000) * 0,8} so'm")
#     else:
#         print(f"sizga chegirma berilmaydi! umumiy summa: {vaqt * 10000}")
# elif velosiped == "sport":
#     if vaqt >= 5:
#         print(f"sizga 20% chegirma berilai! umumiy summa {(vaqt * 15000) * 0.8} so'm")
#     elif vaqt >= 3:
#         print(f"sizga 10% chegirma berilai! umumiy summa {(vaqt * 15000) * 0.8} so'm")
#     else:
#         print(f"sizga chegirma berilmaydi! Umumiy summa: {vaqt * 15000}")
# else:
#     print("qiymatni to'g'ri kiriting: ")
#
# 10 - masala---------------------------------------------

#
# jins = input("jinsni kiriting: ")
# yosh = int(input("yoshingizni kiriting: "))
#
# if 0 < yosh>= 120:
#     if jins == "ayol" and yosh >= 55:
#         n_y = yosh - 55
#         if n_y == 0:
#             print("Buvi - siz nafaqa yoshidasiz!")
#         else:
#             print(f"Siz {n_y} yildan beri nafaqadasiz!")
#     elif jins == "erkak" and yosh >= 60:
#         n_y = yosh - 60
#         if n_y == 0:
#             print("Bobo - siz nafaqa yoshidasiz!")
#         else:
#             print(f"Siz {n_y} yildan beri nafaqadasiz!")
#     else:
#         print("jinsni to'g'ri kiriting!")
# else:
#     print("Yosh 0 dan 120 gacha bo'lishi kerak!")

# 11-masala---------------------------------------------

# ism = input("Ismingizni kiriting: ").strip()
#
# if ism == "":
#     print("Ism bo'sh bo'lmasligi kerak!")
#
# else:
#     try:
#         oy = int(input("Necha oy ishlagansiz: "))
#
#         if oy < 0 or oy > 120:
#             print("oy minimal 0 dan katta, 120 dan kichik yoki teng bolishi kerak!")
#
#         elif oy >= 12:
#             print(f"{ism} siz ta'tilga chiqishingiz mumkin 🎉")
#             print(f"sizga 30 kunlik ta'til berildi.")
#
#         else:
#             print(f"{ism} siz hali ta'tilga chiqa olmaysiz😁")
#             print(f"Ta'tilga yana {12 - oy} oy ishlashingiz kerak!")
#
#     except ValueError:
#         print("Qiymat xato kiritildi")
#
#     finally:
#         print("datur yakuniga yetdi!")

# yosh = int(input("yoshingizni kiriting: "))
# toifa = input("toifangizni kiriting (Masalan: o'quvchi, talab): ").lower()
#
# if yosh < 7:
#     print("sizga yo'l haqqi kerak emas!")
# elif toifa == "o'quvchi":
#     print("2000 so'm")
# elif toifa == "talab":
#     print("4000 so'm")
# else:
#     print("5000 so'm")
