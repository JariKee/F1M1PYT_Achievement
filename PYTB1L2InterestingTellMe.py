import time
def einde():
    time.sleep(1)
    print("heel erg bedank voor het antwoorden van de vragen. fijne dag verder :)")

def vraag3():
    antwoord = input("volgende vraag: wat is jouw woonplaats?:")
    print("")
    time.sleep(1)
    print(antwoord + "? dat is een mooie plaats om te wonen")
    print("")
    time.sleep(1)
    einde()

def vraag2():
    antwoord = input("volgende vraag: wat is jouw leeftijd?:")
    print("")
    time.sleep(1)
    print(antwoord + " Jaar? dat is een mooie leeftijd")
    print("")
    time.sleep(1)
    vraag3()

def eerstevraag():
    print("ik stel een paar vragen")
    print("")
    time.sleep(1)
    Answer = input("ga jij hier mee akkord? Ja/Nee: ")
    print("")
    time.sleep(1)
    if Answer == "Ja":
        time.sleep(1)
        print("goed laten we verder gaan!")
        print("")
        time.sleep(1)
        vraag1()
    elif Answer == "Nee" :
        print ("oke toch bedankt!")
        time.sleep(1)
        exit() 
    else:
        print("vul een geldig antwoord in")
        print("")
        time.sleep(1)
        eerstevraag()


def vraag1():
    naam = input("Wat is jouw naam?:")
    print("")
    time.sleep(1)
    print(naam + " ? dat is een mooie naam")
    print("")
    time.sleep(1)
    vraag2()

eerstevraag()