import os  #Importē os bibliotēku
from random import randint  #Importē randint funkciju no random bibliotēkas


def clear(): #def funkcija, kas izdzēš konsoli
  print(end="\033c")
  
jūtos_drosmigs = True  #Iesāk cikla darbību
rezultāts = 0  #Nosaka sākuma punktu skaitu
dzīvības = 3
print('Spoku spēle 👻')  #Izvada spēles nosaukumu
print('Tev priekšā ir trīs durvis...')  #Izvada spēles instrukcijas lietotājam
print('Aiz vienām ir SPOKS!')  #Izvada spēles instrukcijas lietotājam

while jūtos_drosmigs:  #Cikla sākums
  rnd = randint(1,20)  #Izvēlas nejaušu skaitli no 1 līdz 20
  if rnd == 2:  #Ja izvēlētais skaitlis ir 2
    print(
        'Tavā priekšā parādās maģiska plazmas bumba 🔮, ja tu izvēlēsies pacelt, tā vai nu tev piešķirs dzīvību, vai tu zaudēsi dzīvību!'
    )  #Izvada spēles noteikumus saistībā ar plazmas bumbu.
    print('')
    ievade = int(input('1 - pacelt, 2 - turpini iet: '))  #Lietotājs izvada
    os.system('clear') #notīra konsoli
    while (ievade > 2 or ievade < 1): #pārbauda vai ievadītais skaitlis ir atšķirīgs no 1 vai 2
      ievade = int(input('Ievadi ciparu 1 vai 2')) #ja ievadītais skaitlis ir lielāks par 2 vai mazāks par 1, jautā ievadīt vēlreiz
      os.system('clear') #notīra konsoli
    if ievade == 1:  #Ja lietotājs izvēlas 1
      rnd2 = randint(1, 2)  #Izvēlas nejaušu skaitli no 1 līdz 2
      if rnd2 == 1:  #Ja izvēlētais skaitlis ir 1
        dzīvības = dzīvības + 1  #Pievieno 1 dzīvību
        print('Plazmas bumba piešķīra tev dzīvību ❤️'
              )  #Norāda ka plazmas bumba piešķīra lietotājam dzīvību
        print('Tev ir', dzīvības, 'dzīvības.')  #Izvada dzīvību skaitu
      else:
        dzīvības = dzīvības - 1  #Noņem 1 dzīvību
        print('Plazmas bumba noņēma tev dzīvību 💔')
        print('Tev ir', dzīvības, 'dzīvības.')
        if dzīvības == 0: #pārbada vai dzīvības ir 0
          jūtos_drosmigs = False #beidz ciklu
    else:
      print('Mīkstmiesis!')
  if rnd == 4:  #Ja izvēlētais skaitlis ir 4
    print(
        '👻 Spoks ar tevi komunicējas, sniedzot tev iespēju dubultot savu esošo rezultātu! 👻'
    )
    print(
        'Ja tu izvēlēsies piekrist, spoks pieaicinās draugu un abi paslēpsies starp trim durvīm!'
    )
    print(
        'Izvēloties tukšās durvis, tu rezultātu dubultosi, bet ja izvēlēsies durvis ar spoku, tu zaudē pusi no sava rezultāta.'
    )
    alpha = int(input('1 - piekrist, 2 - nepiekrist'))
    os.system('clear') #notīra konsoli
    while (alpha > 2 or alpha < 1): #Pārbauda vai ievadītais skaitlis ir lielāks par 2 vai mazāks par 1
      alpha = int(input('Ievadi ciparu 1 vai 2')) #prasa ievadīt vēlreiz
      os.system('clear') #notīra konsoli
    if alpha == 1:
      beta1 = randint(1, 3) #nosaka kurās divās durvīs ir spoks
      if beta1 == 1: #nosaka kurās divās durvīs ir spoks
        beta2 = randint(2, 3) #nosaka kurās divās durvīs ir spoks
      if beta1 == 2: #nosaka kurās divās durvīs ir spoks
        beta2 = randint(1, 2) #nosaka kurās divās durvīs ir spoks
        if beta2 == 2: #nosaka kurās divās durvīs ir spoks
          beta2 = 3 #nosaka kurās divās durvīs ir spoks
      if beta1 == 3: #nosaka kurās divās durvīs ir spoks
        beta2 = randint(1, 2) #nosaka kurās divās durvīs ir spoks
      print('🚪 🚪 🚪')
      print('')
      charlie = int(input('Izvēlies durvis 1, 2 vai 3!')) #Lietotājs izvēlas durvis papildspēlē
      os.system('clear')
      if charlie == beta2 or charlie == beta1: #pārbauda vai izvēlētajās durvīs nav spoks
        rezultāts = rezultāts // 2
        print('SPOKS!💀')
        print("Tu zaudē pusi no sava rezultāta!")
        print('Tev ir', rezultāts, 'punkti!')
      else:
        rezultāts = rezultāts * 2
        print('Spoka nav!')  #Izvada rezultātu
        print('Tavs rezultāts dubultojas!')
        print('Tev ir', rezultāts, 'punkti!') #izvada rezultātu
    elif alpha == 2:
      print("Mīkstmiesis!")
  else:
    print('Kuras durvis Tu atvērsi?')  #Izvada norādes lietotājam
    print('🚪 🚪 🚪')
    print('')
    durvis = int(input('1, 2 vai 3?'))  #izvada opcijas
    os.system('clear')
    print('')
    while (durvis > 3 or durvis < 1):
      durvis = int(input('Ievadi ciparu 1, 2 vai 3!'))
      os.system('clear')
    spoka_durvis = randint(1,
                           3)  #Izvēlas nejaušu skaitli  no 1 līdz 3 (durvīm)
    durvju_num = int(durvis)  #Lietotājs ievada ciparu no 1 līdz 3
    if durvju_num == spoka_durvis:  #Salīdzina vai durvju numurs ir vienāds ar spoka durvīm
      if durvju_num == 1: #vizuāli attēlo kurās durvīs bija spoks
        print('👻 🚪 🚪')
      elif durvju_num == 2:
        print('🚪 👻 🚪')
      elif durvju_num == 3:
        print('🚪 🚪 👻')
      print('')
      print('SPOKS!💀')  #Izvada rezultātu
      print('Bēdz prom!')  #Prikols
      print('')
      dzīvības = dzīvības - 1  #Samazina dzīvības skaitu par
      print('Tev ir', dzīvības, 'dzīvības.')
    else:  #Pārvada lietotāju uz nākamajām durvīm
      print('Spoka nav!')  #Izvada rezultātu
      print('Tev ir', dzīvības, 'dzīvības.')
      rezultāts = rezultāts + 1  #Pieskaita punktu
      print('Tu vari ienākt nākamajā istabā.')  #Izvada norādes lietotājam
  if dzīvības == 0:  #Salīdzina vai dzīvības skaits ir 0
    jūtos_drosmigs = False  #Aptur ciklu
print('Spēle beigusies. Tu ieguvi', rezultāts, 'punktus.')  #Izvada rezultātu