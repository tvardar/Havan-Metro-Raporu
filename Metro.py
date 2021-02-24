import time
from sys import exit

print("")
print("*************************************************")
print("***************** HAVATİS METRO *****************")
print("****** METB33 Metro Raporu Çözüm Programı *******")
print("* M29A1 [HE] 900 İlavesiz ve M557 İHTİRAKLI TAPA *")
print("*************************************************")
print("")
print("////////////// tarikvardar@gmail.com ////////////")
print("")
print("************** !!! YASAL UYARI !!! **************")
print("")
print("* Programın kullanımından doğabilecek tüm \n"
      "sorun ve problemler kullanıcıya aittir.\n"
      "* Bu şartı kabul etmiyorsanız programı kullanmayın.\n"
      "* Program verilerin doğru olduğunu beyan etmez.")
print("")
print("*************************************************")
print("")

while True:
   answer = input('Tamam mı? Devam mı? (e/E) (h/H) : ')
   if answer.lower().startswith("e"):
      print("")
      print("Hoşgeldiniz !! METB33 Çözümüne Başlayalım...")
      time.sleep(1)
      print("")
      hhia = int(input("Havan Hedef İA : "))
      hhm = int(input("Havan Hedef Mesafesi : "))
      mvz_rkm = int(input("Mevzi Rakımı : "))
      bh = input("Barut Hakkını girerken;\n 'Tam değerler için 19 yada 1900'\n "
                 "ve '4/8 değerler için 1948 yada 19 48 \nyada 19 4/8' şeklinde \n"
                 "giriş yapınız. BARUT HAKKINI GİRİNİZ : ")

      mht = input("Mühimmat Ağırlık Kare Miktarı :")

      raporbilgi1 = input("Başlık ikinci satır, sağdaki 6 rakam : ")
      raporbilgi2 = input("Metin Soldaki 6 rakam : ")
      raporbilgi3 = input("Metin Sağdaki 6 rakam : ")

      #time.sleep(1)
      bilgi1 = raporbilgi1.split()
      for i in bilgi1:
         a = i[0:3]
         b = i[3:6]

      rakim = int(a)*10
      basinc = int(b)/100
      # print("İstasyon Rakımı : ",rakim," metre")
      # print("Hava Basıncı : %",basinc)

      bilgi2 = raporbilgi2.split()
      for i in bilgi2:
         a = i[2:4]
         b = i[4:6]

      ruzgar_istikamet = int(a)*100
      ruzgar_hizi = int(b)
      # print("Rüzgar İstikameti : ",ruzgar_istikamet,"Milyem")
      # print("Rüzgar Hızı : ",ruzgar_hizi,"Nat")

      bilgi3 = raporbilgi3.split()
      for i in bilgi3:
         a = i[0:3]
         b = i[3:6]

      hava_isi_yuzdesi = int(a)/10
      hava_yogunluk_yuzdesi = int(b)/10+100
      # print("Hava Isısı : %",hava_isi_yuzdesi)
      # print("Hava Yoğunluğu : %",hava_yogunluk_yuzdesi)

      print("")
      print("Plan Esasları Hesaplanıyor ...")
      time.sleep(1)

      rakim_fark = (mvz_rkm) - (rakim)

      if rakim_fark >= 370:
         isi = (hava_isi_yuzdesi) - (0.9)
         print(isi)
      elif rakim_fark >= 330 <= 369:
         isi = (hava_isi_yuzdesi) - (0.8)
         print(isi)
      elif rakim_fark >= 270 <= 329:
         isi = (hava_isi_yuzdesi) - (0.7)
         print(isi)
      elif rakim_fark >= 230 <= 269:
         isi = (hava_isi_yuzdesi) - (0.6)
         print(isi)
      elif rakim_fark >= 200 <= 229:
         isi = (hava_isi_yuzdesi) - (0.5)
         print(isi)
      elif rakim_fark >= 170 <= 199:
         isi = (hava_isi_yuzdesi) - (0.4)
         print(isi)
      elif rakim_fark >= 130 <= 169:
         isi = (hava_isi_yuzdesi) - (0.3)
         print(isi)
      elif rakim_fark >= 70 <= 129:
         isi = (hava_isi_yuzdesi) - (0.2)
         print(isi)
      elif rakim_fark >= 30 <= 69:
         isi = (hava_isi_yuzdesi) - (0.1)
         print(isi)
      elif rakim_fark >= 0 <= 299:
         isi = (hava_isi_yuzdesi) - (0.0)
         print(isi)
      elif rakim_fark <= -370:
         isi = (hava_isi_yuzdesi) + (0.9)
         print(isi)
      elif rakim_fark <= -330 >= -369:
         isi = (hava_isi_yuzdesi) + (0.8)
         print(isi)
      elif rakim_fark <= -270 >= -329:
         isi = (hava_isi_yuzdesi) + (0.7)
         print(isi)
      elif rakim_fark <= -230 >= -269:
         isi = (hava_isi_yuzdesi) + (0.6)
         print(isi)
      elif rakim_fark <= -200 >= -229:
         isi = (hava_isi_yuzdesi) + (0.5)
         print(isi)
      elif rakim_fark <= -170 >= -199:
         isi = (hava_isi_yuzdesi) + (0.4)
         print(isi)
      elif rakim_fark <= -130 >= -169:
         isi = (hava_isi_yuzdesi) + (0.3)
         print(isi)
      elif rakim_fark <= -70 >= -129:
         isi = (hava_isi_yuzdesi) + (0.2)
         print(isi)
      elif rakim_fark <= -30 >= -69:
         isi = (hava_isi_yuzdesi) + (0.1)
         print(isi)
      elif rakim_fark < 0 >= -29:
         isi = (hava_isi_yuzdesi) + (0.0)
         print(isi)
      else:
         print("bitti")

      if rakim_fark >= 390:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.9)
         print(round(yogunluk, 2))
      elif rakim_fark >= 380 <= 389:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.8)
         print(round(yogunluk, 2))
      elif rakim_fark >= 370 <= 379:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.7)
         print(round(yogunluk, 2))
      elif rakim_fark >= 360 <= 369:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.6)
         print(round(yogunluk, 2))
      elif rakim_fark >= 350 <= 359:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.5)
         print(round(yogunluk, 2))
      elif rakim_fark >= 340 <= 349:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.4)
         print(round(yogunluk, 2))
      elif rakim_fark >= 330 <= 339:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.3)
         print(round(yogunluk, 2))
      elif rakim_fark >= 320 <= 329:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.2)
         print(round(yogunluk, 2))
      elif rakim_fark >= 310 <= 319:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.1)
         print(round(yogunluk, 2))
      elif rakim_fark >= 300 <= 309:
         yogunluk = (hava_yogunluk_yuzdesi) - (3.0)
         print(round(yogunluk, 2))
      elif rakim_fark >= 290 <= 299:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.9)
         print(round(yogunluk, 2))
      elif rakim_fark >= 280 <= 289:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.8)
         print(round(yogunluk, 2))
      elif rakim_fark >= 270 <= 279:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.7)
         print(round(yogunluk, 2))
      elif rakim_fark >= 260 <= 269:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.6)
         print(round(yogunluk, 2))
      elif rakim_fark >= 250 <= 259:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.5)
         print(round(yogunluk, 2))
      elif rakim_fark >= 240 <= 249:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.4)
         print(round(yogunluk, 2))
      elif rakim_fark >= 230 <= 239:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.3)
         print(round(yogunluk, 2))
      elif rakim_fark >= 220 <= 229:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.2)
         print(round(yogunluk, 2))
      elif rakim_fark >= 210 <= 219:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.1)
         print(round(yogunluk, 2))
      elif rakim_fark >= 200 <= 209:
         yogunluk = (hava_yogunluk_yuzdesi) - (2.0)
         print(round(yogunluk, 2))
      elif rakim_fark >= 190 <= 199:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.9)
         print(round(yogunluk, 2))
      elif rakim_fark >= 180 <= 189:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.8)
         print(round(yogunluk, 2))
      elif rakim_fark >= 170 <= 179:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.7)
         print(round(yogunluk, 2))
      elif rakim_fark >= 160 <= 169:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.6)
         print(round(yogunluk, 2))
      elif rakim_fark >= 150 <= 159:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.5)
         print(round(yogunluk, 2))
      elif rakim_fark >= 140 <= 149:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.4)
         print(round(yogunluk, 2))
      elif rakim_fark >= 130 <= 139:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.3)
         print(round(yogunluk, 2))
      elif rakim_fark >= 120 <= 129:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.2)
         print(round(yogunluk, 2))
      elif rakim_fark >= 110 <= 119:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.1)
         print(round(yogunluk, 2))
      elif rakim_fark >= 100 <= 109:
         yogunluk = (hava_yogunluk_yuzdesi) - (1.0)
         print(round(yogunluk, 2))
      elif rakim_fark >= 90 <= 99:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.9)
         print(round(yogunluk, 2))
      elif rakim_fark >= 80 <= 89:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.8)
         print(yogunluk)
      elif rakim_fark >= 70 <= 79:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.7)
         print(yogunluk)
      elif rakim_fark >= 60 <= 69:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.6)
         print(yogunluk)
      elif rakim_fark >= 50 <= 59:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.5)
         print(yogunluk)
      elif rakim_fark >= 40 <= 49:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.4)
         print(yogunluk)
      elif rakim_fark >= 30 <= 39:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.3)
         print(yogunluk)
      elif rakim_fark >= 20 <= 29:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.2)
         print(yogunluk)
      elif rakim_fark >= 10 <= 19:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.1)
         print(yogunluk)
      elif rakim_fark >= 0 <= 9:
         yogunluk = (hava_yogunluk_yuzdesi) - (0.0)
         print(yogunluk)
      elif rakim_fark <= -390:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.8)
         print(yogunluk)
      elif rakim_fark <= -380 >= -389:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.8)
         print(yogunluk)
      elif rakim_fark <= -370 >= -379:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.7)
         print(yogunluk)
      elif rakim_fark <= -360 >= -369:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.6)
         print(yogunluk)
      elif rakim_fark <= -350 >= -359:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.5)
         print(yogunluk)
      elif rakim_fark <= -340 >= -349:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.4)
         print(yogunluk)
      elif rakim_fark <= -330 >= -339:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.3)
         print(yogunluk)
      elif rakim_fark <= -320 >= -329:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.2)
         print(yogunluk)
      elif rakim_fark <= -310 >= -319:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.1)
         print(yogunluk)
      elif rakim_fark <= -300 >= -309:
         yogunluk = (hava_yogunluk_yuzdesi) + (3.0)
         print(yogunluk)
      elif rakim_fark <= -290 >= -299:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.9)
         print(yogunluk)
      elif rakim_fark <= -280 >= -289:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.8)
         print(yogunluk)
      elif rakim_fark <= -270 >= -279:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.7)
         print(yogunluk)
      elif rakim_fark <= -260 >= -269:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.6)
         print(yogunluk)
      elif rakim_fark <= -250 >= -259:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.5)
         print(yogunluk)
      elif rakim_fark <= -240 >= -249:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.4)
         print(yogunluk)
      elif rakim_fark <= -230 >= -239:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.3)
         print(yogunluk)
      elif rakim_fark <= -220 >= -229:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.2)
         print(yogunluk)
      elif rakim_fark <= -210 >= -219:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.1)
         print(yogunluk)
      elif rakim_fark <= -200 >= -209:
         yogunluk = (hava_yogunluk_yuzdesi) + (2.0)
         print(yogunluk)
      elif rakim_fark <= -190 >= -199:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.9)
         print(yogunluk)
      elif rakim_fark <= -180 >= -189:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.8)
         print(yogunluk)
      elif rakim_fark <= -170 >= -179:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.7)
         print(yogunluk)
      elif rakim_fark <= -160 >= -169:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.6)
         print(yogunluk)
      elif rakim_fark <= -150 >= -159:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.5)
         print(yogunluk)
      elif rakim_fark <= -140 >= -149:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.4)
         print(yogunluk)
      elif rakim_fark <= -130 >= -139:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.3)
         print(yogunluk)
      elif rakim_fark <= -120 >= -129:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.2)
         print(yogunluk)
      elif rakim_fark <= -110 >= -119:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.1)
         print(yogunluk)
      elif rakim_fark <= -100 >= -109:
         yogunluk = (hava_yogunluk_yuzdesi) + (1.0)
         print(yogunluk)
      elif rakim_fark <= -90 >= -99:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.9)
         print(yogunluk)
      elif rakim_fark <= -80 >= -89:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.8)
         print(yogunluk)
      elif rakim_fark <= -70 >= -79:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.7)
         print(yogunluk)
      elif rakim_fark <= -60 >= -69:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.6)
         print(yogunluk)
      elif rakim_fark <= -50 >= -59:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.5)
         print(yogunluk)
      elif rakim_fark <= -40 >= -49:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.4)
         print(yogunluk)
      elif rakim_fark <= -30 >= -39:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.3)
         print(yogunluk)
      elif rakim_fark <= -20 >= -29:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.2)
         print(yogunluk)
      elif rakim_fark <= -10 >= -19:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.1)
         print(yogunluk)
      elif rakim_fark <= 0 >= -9:
         yogunluk = (hava_yogunluk_yuzdesi) + (0.0)
         print(yogunluk)

      else:
         print("bitti")

      # print("Rakım Farkı : ",rakim_fark,"Metre. Mevzi, Metro İstasyonuna göre",rakim_fark,"metre'de")
      print("")
      print("*************************************************")
      print("METB33 Rapor Formunu Aşağıdaki Şekilde Doldurunuz")
      print("*************************************************")
      print("")
      time.sleep(1)
      print("")
      print("/////////////// PLAN ESASLARI ///////////////")
      print("---------------------------------------------")
      print("Barut Hakkı : ", bh)
      print("Plan Mesafesi : ", hhm)
      print("Yükseliş : 900")
      print("Mevzi Yüksekliği : ", mvz_rkm)
      print("Metro İstasyon Yüksekliği : ", rakim)
      print("Mevzi - Metro İst.Yük.Fark : ", rakim_fark)
      print("")
      #time.sleep(2)
      print("/////////////// METRO RAPORU ///////////////")
      print("--------------------------------------------")
      print("Rapor Tipi : METB33")
      print("Met.İst.Yük : ", rakim)
      print("Rüzgar İst. : ", ruzgar_istikamet)
      print("Rüzgar Hızı : ", ruzgar_hizi)
      print("Hava Isısı : ", hava_isi_yuzdesi)
      print("Hava Yoğunluğu : ", hava_yogunluk_yuzdesi)
      print(">>Yükseklik Farkı Düzeltmeleri", round(isi-hava_isi_yuzdesi,2)," | ", round(yogunluk-hava_yogunluk_yuzdesi,2))
      print("Düzeltilmiş Değer (Isı) : ", isi)
      print("Düzeltilmiş Değer (Yoğunluk) : ", round(yogunluk,2))
      print("")
      #time.sleep(2)
      print("/// RÜZGAR BİLEŞENLERİ VE YAN DÜZELTMELER ///")
      print("--------------------------------------------")

      print("Rüzgar İstikameti : ", ruzgar_istikamet)
      if ruzgar_istikamet < hhia:
         ruzgar_istikamet = ruzgar_istikamet + 6400
      else:
         ruzgar_istikamet = ruzgar_istikamet
      print("Toplam : ", ruzgar_istikamet)
      print("Atış İstikameti : ", hhia)
      print("Rüzgar Plan İstikameti : ", ruzgar_istikamet - hhia)

      Ruzgar_Istikameti = ruzgar_istikamet - hhia

      if Ruzgar_Istikameti == 0 or Ruzgar_Istikameti <= 99:
         bilesen_hiz = 0
         mesafe_yon = "H Baş"
         mesafe_hiz = 1.00
         print("Yan Rüzgar Bileşenleri : ", bilesen_hiz)

      elif Ruzgar_Istikameti <= 199 >= 100:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.10
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.99
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 299 >= 200:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.20
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.98
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 399 >= 300:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.29
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.96
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 499 >= 400:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.38
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.92
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 599 >= 500:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.47
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.88
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 699 >= 600:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.56
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.83
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 799 >= 700:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.63
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.77
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 899 >= 800:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.71
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.71
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 999 >= 900:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.77
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.63
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1099 >= 1000:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.83
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.56
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1199 >= 1100:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.88
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.47
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1299 >= 1200:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.92
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.38
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1399 >=1300:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.96
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.29
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1499 >= 1400:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.98
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.20
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1599 >= 1500:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.99
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.10
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1699 >= 1600:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 1.0
         mesafe_hiz = 0
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1799 >= 1700:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.99
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.10
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1899 >= 1800:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.98
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.20
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 1999 >= 1900:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.96
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.29
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2099 >= 2000:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.92
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.38
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2199 >= 2100:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.88
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.47
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2299 >= 2200:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.83
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.56
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2399 >= 2300:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.77
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.63
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2499 >= 2400:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.71
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.71
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2599 >= 2500:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.63
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.77
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2699 >= 2600:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.56
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.83
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2799 >= 2700:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.47
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.88
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2899 >= 2800:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.38
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.92
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 2999 >= 2900:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.29
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.96
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3099 >= 3000:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.20
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.98
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3199 >= 3100:
         bilesen_yon = "R Sağ"
         bilesen_hiz = 0.10
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.99
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3299 >= 3200:
         bilesen_hiz = 0
         mesafe_yon = "T Arka"
         mesafe_hiz = 1.0
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3399 >= 3300:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.10
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.99
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3499 >= 3400:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.20
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.98
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3599 >= 3500:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.29
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.96
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3699 >= 3600:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.38
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.92
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3799 >= 3700:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.47
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.88
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3899 >= 3800:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.56
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.83
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 3999 >= 3900:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.63
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.77
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4099 >= 4000:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.71
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.71
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4199 >= 4100:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.77
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.63
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4299 >= 4200:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.83
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.56
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4399 >= 4300:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.88
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.47
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4499 >= 4400:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.92
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.38
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4599 >= 4500:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.96
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.29
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4699 >= 4600:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.98
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.20
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4799 >= 4700:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.99
         mesafe_yon = "T Arka"
         mesafe_hiz = 0.10
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4899 >= 4800:
         bilesen_yon = "L Sol"
         bilesen_hiz = 1.0
         mesafe_hiz = 0
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 4999 >= 4900:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.99
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.10
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5099 >= 5000:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.98
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.20
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5199 >= 5100:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.96
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.29
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5299 >= 5200:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.92
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.38
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5399 >= 5300:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.88
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.47
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5499 >= 5400:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.83
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.56
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5599 >= 5500:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.77
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.63
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5699 >= 5600:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.71
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.71
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5799 >= 5700:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.63
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.77
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5899 >= 5800:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.56
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.83
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 5999 >= 5900:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.47
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.88
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 6099 >= 6000:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.38
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.92
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 6199 >= 6100:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.29
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.96
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 6299 >= 6200:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.20
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.98
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 6399 >= 6300:
         bilesen_yon = "L Sol"
         bilesen_hiz = 0.10
         mesafe_yon = "H Baş"
         mesafe_hiz = 0.99
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      elif Ruzgar_Istikameti <= 6499 >= 6400:
         bilesen_hiz = 0
         mesafe_yon = "H Baş"
         mesafe_hiz = 1.0
         print("Yan Rüzgar Bileşenleri : ", bilesen_yon, bilesen_hiz)

      Cetvel_D = hhm

      if Cetvel_D <= 1260 >= 1060:
         nat_ruzgar = 0.6
      elif Cetvel_D <= 1810 >= 1261:
         nat_ruzgar = 0.7
      elif Cetvel_D <= 2470 >= 1811:
         nat_ruzgar = 0.8
      elif Cetvel_D <= 3250 >= 2471:
         nat_ruzgar = 0.9
      elif Cetvel_D <=4220 >=3251:
         nat_ruzgar = 1.0
      else:
         print("Hata")

      if mesafe_yon == "H Baş":
         if hhm <= 2569 >= 2529:
            nat_duzeltme = 4.1
         elif hhm <= 2639 >= 2570:
            nat_duzeltme = 4.2
         elif hhm <= 2679 >= 2640:
            nat_duzeltme = 4.3
         elif hhm <= 2719 >= 2680:
            nat_duzeltme = 4.4
         elif hhm <= 2759 >= 2720:
            nat_duzeltme = 4.5
         elif hhm <= 2829 >= 2760:
            nat_duzeltme = 4.6
         elif hhm <= 2869 >= 2830:
            nat_duzeltme = 4.7
         elif hhm <= 2909 >= 2870:
            nat_duzeltme = 4.8
         elif hhm <= 2949 >= 2910:
            nat_duzeltme = 4.9
         elif hhm <= 2999 >= 2950:
            nat_duzeltme = 5.0
         elif hhm <= 3039 >= 3000:
            nat_duzeltme = 5.1
         elif hhm <= 3079 >= 3040:
            nat_duzeltme = 5.2
         elif hhm <= 3149 >= 3080:
            nat_duzeltme = 5.3
         elif hhm <= 3189 >= 3150:
            nat_duzeltme = 5.4
         elif hhm <= 3229 >= 3190:
            nat_duzeltme = 5.5
         elif hhm <= 3279 >= 3228:
            nat_duzeltme = 5.6
         elif hhm <= 3319 >= 3280:
            nat_duzeltme = 5.7
         elif hhm <= 3359 >= 3320:
            nat_duzeltme = 5.8
         elif hhm <= 3409 >= 3360:
            nat_duzeltme = 5.9
         elif hhm <= 3449 >= 3410:
            nat_duzeltme = 6.0
         elif hhm <= 3489 >= 3450:
            nat_duzeltme = 6.1
         elif hhm <= 3539 >= 3490:
            nat_duzeltme = 6.2
         else:
            pass

      if mesafe_yon == "T Arka":
         if hhm <= 2589 >= 2529:
            nat_duzeltme = -3.0
         elif hhm <= 2659 >= 2590:
            nat_duzeltme = -3.1
         elif hhm <= 2719 >= 2660:
            nat_duzeltme = -3.2
         elif hhm <= 2779 >= 2720:
            nat_duzeltme = -3.3
         elif hhm <= 2849 >= 2780:
            nat_duzeltme = -3.4
         elif hhm <= 2889 >= 2850:
            nat_duzeltme = -3.5
         elif hhm <= 2949 >= 2890:
            nat_duzeltme = -3.6
         elif hhm <= 3019 >= 2950:
            nat_duzeltme = -3.7
         elif hhm <= 3059 >= 3020:
            nat_duzeltme = -3.8
         elif hhm <= 3119 >= 3060:
            nat_duzeltme = -3.9
         elif hhm <= 3189 >= 3120:
            nat_duzeltme = -4.0
         elif hhm <= 3229 >= 3190:
            nat_duzeltme = -4.1
         elif hhm <= 3299 >= 3230:
            nat_duzeltme = -4.2
         elif hhm <= 3359 >= 3300:
            nat_duzeltme = -4.3
         elif hhm <= 3409 >= 3360:
            nat_duzeltme = -4.4
         elif hhm <= 3469 >= 3410:
            nat_duzeltme = -4.5
         elif hhm <= 3509 >= 3470:
            nat_duzeltme = -4.6
         elif hhm <= 3579 >= 3510:
            nat_duzeltme = -4.7
         elif hhm <= 3649 >= 3580:
            nat_duzeltme = -4.8
         else:
            pass
      print("Yan Rüzgar : ", ruzgar_hizi, "X", bilesen_hiz, "=", ruzgar_hizi*bilesen_hiz, "X", nat_ruzgar, "=",bilesen_yon, ruzgar_hizi*bilesen_hiz*nat_ruzgar)

      print("Mesafe Rüzgarı : ", ruzgar_hizi, "X", mesafe_hiz, "=",mesafe_yon, (round(ruzgar_hizi*mesafe_hiz,2)))

      # time.sleep(2)
      print("")
      print("/// METRO MESAFE DÜZELTMELERİ ///")
      print("--------------------------------------------")
      print(">>>>> Mesafe Rüzgarı <<<<<")
      print("Bilinen Değerler : ", mesafe_yon, round(ruzgar_hizi*mesafe_hiz,2))
      print("Standart Değerler : 0")
      print("Standartdan Farklar : ", mesafe_yon, round(ruzgar_hizi*mesafe_hiz,2))
      print("Birim Düzeltmeleri : ", nat_duzeltme)
      durumruzgar = round((ruzgar_hizi*mesafe_hiz)*nat_duzeltme,1)
      if durumruzgar >= 0:
        print("ARTI ", durumruzgar)
      else:
        print("EKSİ ", durumruzgar)

      print("")
      print(">>>>> Hava Isısı <<<<<")
      print("Bilinen Değerler : ", isi)
      print("Standart Değerler : 100")
      durumisi = round(isi-100,2)
      if durumisi <0:
        print("Standarttan Farklar : EKSİLME ", round(isi-100,2))
      else:
        print("Standartdan Farklar : ARTMA ", round(isi-100,2))
      print("Birim Düzeltme : 0")
      print("")

      print(">>>>> Hava Yoğunluğu <<<<<")
      print("Bilinen Değerler : ", round(yogunluk,2))
      print("Standar Değerler : 100")
      durumyogunluk = round(yogunluk-100,2)
      if durumyogunluk >=0:
        print("Standartdan Farklar : ARTMA ", durumyogunluk)
      else:
        print("Standartdan Farklar : EKSİLME ", durumyogunluk)

      yogunlukduzeltme = durumyogunluk

      if yogunlukduzeltme >=0:
          if hhm <=2529 >=2491:
              yogunlukduzeltme = 5.0
          elif hhm <=2569 >=2530:
              yogunlukduzeltme = 5.1
          elif hhm <=2589 >=2570:
              yogunlukduzeltme = 5.2
          elif hhm <=2619 >=2590:
              yogunlukduzeltme = 5.3
          elif hhm <=2659 >2620:
              yogunlukduzeltme = 5.4
          elif hhm <=2679 >=2660:
              yogunlukduzeltme = 5.5
          elif hhm <=2699 >=2680:
              yogunlukduzeltme = 5.6
          elif hhm <=2719 >=2700:
              yogunlukduzeltme = 5.7
          elif hhm <=2739 >=2720:
              yogunlukduzeltme = 5.8
          elif hhm <=2779 >=2740:
              yogunlukduzeltme = 5.9
          elif hhm <=2799 >=2780:
              yogunlukduzeltme = 6.0
          elif hhm <=2829 >=2800:
              yogunlukduzeltme = 6.1
          elif hhm <=2849 >=2830:
              yogunlukduzeltme = 6.2
          elif hhm <=2869 >=2850:
              yogunlukduzeltme = 6.3
          elif hhm <=2889 >=2870:
              yogunlukduzeltme = 6.4
          elif hhm <=2909 >=2890:
              yogunlukduzeltme = 6.5
          elif hhm <=2929 >=2910:
              yogunlukduzeltme = 6.6
          elif hhm <=2969 >=2930:
              yogunlukduzeltme = 6.7
          elif hhm <=2999 >=2970:
              yogunlukduzeltme = 6.8
          elif hhm <=3019 >=3000:
              yogunlukduzeltme = 6.9
          elif hhm <=3039 >=3020:
              yogunlukduzeltme = 7.0
          elif hhm <=3059 >=3040:
              yogunlukduzeltme = 7.1
          elif hhm <=3079 >=3060:
              yogunlukduzeltme = 7.2
          elif hhm <=3099 >=3080:
              yogunlukduzeltme = 7.3
          elif hhm <=3119 >=3100:
              yogunlukduzeltme = 7.4
          elif hhm <=3149 >=3120:
              yogunlukduzeltme = 7.5
          elif hhm <=3169 >=3150:
              yogunlukduzeltme = 7.6
          elif hhm <=3189 >=3170:
              yogunlukduzeltme = 7.7
          elif hhm <=3209 >=3190:
              yogunlukduzeltme = 7.8
          elif hhm <=3229 >=3210:
              yogunlukduzeltme = 7.9
          elif hhm <=3249 >=3230:
              yogunlukduzeltme = 8.0
          elif hhm <=3279 >=3250:
              yogunlukduzeltme = 8.1
          elif hhm <=3299 >=3280:
              yogunlukduzeltme = 8.2
          elif hhm <=3319 >=3300:
              yogunlukduzeltme = 8.3
          elif hhm <=3339 >=3320:
              yogunlukduzeltme = 8.4
          elif hhm <=3359 >=3340:
              yogunlukduzeltme = 8.5
          elif hhm <=3379 >=3360:
              yogunlukduzeltme = 8.6
          elif hhm <=3409 >=3380:
              yogunlukduzeltme = 8.7
          elif hhm <=3429 >=3410:
              yogunlukduzeltme = 8.8
          else:
              print("2529 ile 3429 arası mesafeler için hesaplama yapar")
      else:
          if hhm <= 2529 >= 2491:
              yogunlukduzeltme = -4.8
          elif hhm <= 2549 >= 2530:
              yogunlukduzeltme = -4.9
          elif hhm <= 2569 >= 2550:
              yogunlukduzeltme = -5.0
          elif hhm <= 2619 >= 2570:
              yogunlukduzeltme = -5.1
          elif hhm <= 2639 > 2620:
              yogunlukduzeltme = -5.2
          elif hhm <= 2659 >= 2640:
              yogunlukduzeltme = -5.3
          elif hhm <= 2679 >= 2660:
              yogunlukduzeltme = -5.4
          elif hhm <= 2719 >= 2780:
              yogunlukduzeltme = -5.5
          elif hhm <= 2739 >= 2720:
              yogunlukduzeltme = -5.6
          elif hhm <= 2759 >= 2740:
              yogunlukduzeltme = -5.7
          elif hhm <= 2779 >= 2760:
              yogunlukduzeltme = -5.8
          elif hhm <= 2829 >= 2780:
              yogunlukduzeltme = -5.9
          elif hhm <= 2849 >= 2830:
              yogunlukduzeltme = -6.0
          elif hhm <= 2869 >= 2850:
              yogunlukduzeltme = -6.1
          elif hhm <= 2889 >= 2870:
              yogunlukduzeltme = -6.2
          elif hhm <= 2909 >= 2890:
              yogunlukduzeltme = -6.3
          elif hhm <= 2949 >= 2910:
              yogunlukduzeltme = -6.4
          elif hhm <= 2969 >= 2950:
              yogunlukduzeltme = -6.5
          elif hhm <= 2999 >= 2970:
              yogunlukduzeltme = -6.6
          elif hhm <= 3019 >= 3000:
              yogunlukduzeltme = -6.7
          elif hhm <= 3039 >= 3020:
              yogunlukduzeltme = -6.8
          elif hhm <= 3059 >= 3040:
              yogunlukduzeltme = -6.9
          elif hhm <= 3079 >= 3060:
              yogunlukduzeltme = -7.0
          elif hhm <= 3099 >= 3080:
              yogunlukduzeltme = -7.1
          elif hhm <= 3149 >= 3100:
              yogunlukduzeltme = -7.2
          elif hhm <= 3169 >= 3150:
              yogunlukduzeltme = -7.3
          elif hhm <= 3189 >= 3170:
              yogunlukduzeltme = -7.4
          elif hhm <= 3209 >= 3190:
              yogunlukduzeltme = -7.5
          elif hhm <= 3229 >= 3210:
              yogunlukduzeltme = -7.6
          elif hhm <= 3249 >= 3230:
              yogunlukduzeltme = -7.7
          elif hhm <= 3279 >= 3250:
              yogunlukduzeltme = -7.8
          elif hhm <= 3299 >= 3280:
              yogunlukduzeltme = -7.9
          elif hhm <= 3319 >= 3300:
              yogunlukduzeltme = -8.0
          elif hhm <= 3339 >= 3320:
              yogunlukduzeltme = -8.1
          elif hhm <= 3359 >= 3340:
              yogunlukduzeltme = -8.2
          elif hhm <= 3379 >= 3360:
              yogunlukduzeltme = -8.3
          elif hhm <= 3409 >= 3380:
              yogunlukduzeltme = -8.4
          elif hhm <= 3429 >= 3410:
              yogunlukduzeltme = -8.5
          else:
              print("2529 ile 3429 arası mesafeler için hesaplama yapar")

      if yogunlukduzeltme >= 0:
          yogunlukduzeltmebirim = "ARTMA"
      else:
          yogunlukduzeltmebirim = "EKSİLME"
      print("Birim Düzeltmeleri : ", yogunlukduzeltmebirim, yogunlukduzeltme)
      durumyogunlukduzeltme = yogunlukduzeltme
      if durumyogunlukduzeltme > 0:
          yogunlukduzeltmebirim = "ARTI"
      else:
          yogunlukduzeltmebirim = "EKSİ"

      print(yogunlukduzeltmebirim, round(durumyogunluk*yogunlukduzeltme,2))
      print("")

      print(">>>>> Mühimmat Ağırlığı <<<<<")
      print("Bilinen Değerler : ", mht, "SQ")
      print("Standart Değerler : 2 SQ")

      if int(mht) > 2:
         muhtfark = int(mht)-2
         muhtartis = "ARTMA"
      elif int(mht) < 2:
         muhtfark = int(mht)-2
         muhtartis = "EKSİLME"
      else:
         muhtfark = int(mht)-2
         muhtartis = "YOK"

      print("Standart Farklar : ",muhtartis , muhtfark)

      if hhm <=2869 >2500 and muhtfark == 1:
         agirlik = 10
      elif hhm <=3299 >=2870 and muhtfark ==1:
         agirlik = 11
      elif hhm <=3619 >=3300 and muhtfark ==1:
         agirlik = 12
      elif hhm <=3059 >2500 and muhtfark == -1:
         agirlik = -10
      elif hhm <=3489 >=3060 and muhtfark == -1:
         agirlik = -11
      elif hhm <=3819 >=3490 and muhtfark == -1:
         agirlik = -12
      elif hhm <=3900 >=2500 and muhtfark ==0:
         agirlik = 10

      print("Birim Düzeltmeleri : ", agirlik)

      if agirlik >0:
         agirlikdurum = "ARTI"
      else:
         agirlikdurum = "EKSİ"

      print(agirlikdurum, agirlik)
      print("")
      if bh == "13" or bh == "1300":
         ilkhiz = 165.7
      elif bh == "13 48" or bh == "1348" or bh=="13 4/8":
         ilkhiz = 169.3
      elif bh == "14" or bh == "1400":
         ilkhiz = 172.9
      elif bh == "14 48" or bh == "1448" or bh== "14 4/8":
         ilkhiz = 176.5
      elif bh == "15" or bh == "1500":
         ilkhiz = 180.1
      elif bh == "15 48" or bh == "1548" or bh == "15 4/8":
         ilkhiz = 183.8
      elif bh == "16" or bh == "1600":
         ilkhiz = 187.4
      elif bh == "16 48" or bh == "1648" or bh == "16 4/8":
         ilkhiz = 191.0
      elif bh == "17" or bh == "1700":
         ilkhiz = 194.6
      elif bh == "17 48" or bh == "1748" or bh == "17 4/8":
         ilkhiz = 198.2
      elif bh == "18" or bh == "1800":
         ilkhiz = 201.8
      elif bh == "19 48" or bh == "1948" or bh == "19 4/8":
         ilkhiz = 212.6
      elif bh == "20" or bh == "20":
         ilkhiz = 216.2
      elif bh == "20 48" or bh == "2048" or bh == "20 4/8":
         ilkhiz = 219.8

      ilkhizhesap = round(198.8 - ilkhiz,1)

      if ilkhizhesap >0:
         ilkhizartis = "ARTMA"
      elif ilkhizhesap <0:
         ilkhizartis = "EKSİLME"

      if ilkhizhesap > 0:
         if hhm <= 2549 >=2490:
            ilkhizdeger = -22.8
         elif hhm <=2589 >=2550:
            ilkhizdeger = -22.9
         elif hhm <=2659 >=2590:
            ilkhizdeger = -23.0
         elif hhm <=2719 >=2660:
            ilkhizdeger = -23.1
         elif hhm <=2779 >=2720:
            ilkhizdeger = -23.2
         elif hhm <=2849 >=2780:
            ilkhizdeger = -23.3
         elif hhm <=2909 >=2850:
            ilkhizdeger = -23.4
         elif hhm <=2969 >=2910:
            ilkhizdeger = -23.5
         elif hhm <=3059 >=2970:
            ilkhizdeger = -23.6
         elif hhm <=3149 >=3060:
            ilkhizdeger = -23.7
         elif hhm <3229 >=3150:
            ilkhizdeger = -23.8
         elif hhm <=3339 >=3330:
            ilkhizdeger = -23.9
         elif hhm <=3449 >=3340:
            ilkhizdeger = -24.0
         elif hhm <=3579 >=3450:
            ilkhizdeger = -24.1
         else:
            print("ARTMA 2500 ile 3500 m arası havan hedef mesafesi içindir")
      elif ilkhizhesap <0:
         if hhm <= 2509 >=2490:
            ilkhizdeger = 23.1
         elif hhm <=2529 >=2510:
            ilkhizdeger = 23.2
         elif hhm <=2589 >=2530:
            ilkhizdeger = 23.3
         elif hhm <=2679 >=2590:
            ilkhizdeger = 23.4
         elif hhm <=2739 >=2680:
            ilkhizdeger = 23.5
         elif hhm <=2829 >=2740:
            ilkhizdeger = 23.6
         elif hhm <=2909 >=2830:
            ilkhizdeger = 23.7
         elif hhm <=2999 >=2910:
            ilkhizdeger = 23.8
         elif hhm <=3099 >=3000:
            ilkhizdeger = 23.9
         elif hhm <=3209 >=3100:
            ilkhizdeger = 24.0
         elif hhm <3339 >=3210:
            ilkhizdeger = 24.1
         elif hhm <=3489 >=3340:
            ilkhizdeger = 24.2
         elif hhm <=3669 >=3490:
            ilkhizdeger = 24.3
         else:
            print("2500 ile 3500 m arası havan hedef mesafesi içindir")
      else:
         print("Hata")

      print(">>>>> İlk Hız <<<<<")
      print("Bilinen Değerler : ", ilkhizhesap, "m/s")
      print("Standart Değerler : 0")
      print("Standarttan Farklar : ", ilkhizartis, ilkhizhesap)
      print("Birim Düzeltme : ", ilkhizdeger)

      if ilkhizhesap*ilkhizdeger < 0:
         ilkhizartis = "EKSİ"
      else:
         ilkhizartis = "ARTI"

      print(ilkhizartis, ilkhizhesap * ilkhizdeger)
      print("")


      artiliste = []
      eksiliste = []

      if durumruzgar >= 0:
         artiliste.append(durumruzgar)
      else:
         eksiliste.append(durumruzgar)

      if round(durumyogunluk*yogunlukduzeltme,2) > 0:
         artiliste.append(round(durumyogunluk*yogunlukduzeltme,2))
      else:
         eksiliste.append(round(durumyogunluk*yogunlukduzeltme,2))

      if agirlik >= 0:
         artiliste.append(agirlik)
      else:
         eksiliste.append(agirlik)

      if ilkhizhesap*ilkhizdeger < 0:
         eksiliste.append(ilkhizhesap*ilkhizdeger)
      else:
         artiliste.append(ilkhizhesap*ilkhizdeger)

      print("TOPLAM (Artı) : ", sum(artiliste))
      print("TOPLAM (Eksi) : ", sum(eksiliste))
      print("TOPLAM MEVZİ DÜZELTME : ", sum(artiliste)+sum(eksiliste), "=", round(sum(artiliste)+sum(eksiliste)))

      print("")
      print("SON RAPOR :")
      zyx = round(ruzgar_hizi*bilesen_hiz*nat_ruzgar)
      if zyx >0:
         yandeger = "ARTI"
      else:
         yandeger = "EKSİ"
      print("YAN : ", bilesen_yon, yandeger, round(ruzgar_hizi*bilesen_hiz*nat_ruzgar))

      xyz = round(sum(artiliste)+sum(eksiliste))
      if xyz >0:
         mesafedeger = "ARTI"
      else:
         mesafedeger = "EKSİ"

      print("MESAFE : ", mesafedeger, round(sum(artiliste)+sum(eksiliste)), "Metre")

      print("")

   elif answer.lower().startswith != "e" or "E":
      print("")
      print("")
      print("Ok, Sayonnara !! Bye !!")
      time.sleep(2)
      exit()
