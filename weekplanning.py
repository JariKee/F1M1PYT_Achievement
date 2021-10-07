import time

def begin():
    print("Hello you")
    print("")
    time.sleep(2)
    print("dit is mijn weekplannig en jij mag die bepalen")
    print("")
    time.sleep(2)
    maandag()

def einde():
    print("dit was het einde van me week planning")
    print("")
    time.sleep(2)
    print("bedankt voor het invulen!!")
    print("")
    time.sleep(2)
    print("ik wens u een vijne dag verder")
    print("")
    time.sleep(2)

def vrijdag():
    print("voor vrijdag heb ik deze keer 3 keuzens")
    print("")
    time.sleep(2)
    print("na school ga ik gamen maar ik weet niet welke")
    print("")
    time.sleep(2)
    print("of ik ga Escape from tarkov spelen| EFT")
    print("")
    time.sleep(2)
    print("of ik ga Boneworks VR spelen")
    print("")
    time.sleep(2)
    print("enda laatste keuze is Pavlov VR")
    print("")
    time.sleep(2)
    antwoord = input("Maak je keuze EFT, Boneworks of Pavlov: ")
    print("")
    time.sleep(2)
    print("")
    time.sleep(1)
    if antwoord == "EFT":
        print("oke vrijdag ga ik Escape from Tarkov spelen")
        print("")
    time.sleep(2)
    if antwoord == "Pavlov":
        print("oke dan ga ik vrijdag Pavlov VR spelen")
    time.sleep(1)
    print("")
    if antwoord == "Boneworks":
        print("top vrijdag ga ik dan Boneworks spelen ")
        time.sleep(1)
        print("")
    else:
        print("vul een geldig antwoord in")
        print("")
        time.sleep(1)
        vrijdag()
    einde()

def donderdag():
    print("Voor donderdag heb ik ook weer 2 keuzes")
    print("")
    time.sleep(2)
    print("of ik ga in de ochtend fietsend naar school")
    print("")
    time.sleep(2)
    print("of ik ga lopend naar school")
    print("")
    time.sleep(2)
    antwoord = input("Maak je keuze fietsen of lopen: ")
    print("")
    time.sleep(2)
    print("")
    time.sleep(1)
    if antwoord == "fietsen":
        print("fietsen is wel beter dan ben ik sneller op school")
        print("")
    time.sleep(2)
    if antwoord == "lopen":
        print("lopen is is wel makkelijker maar ik moet aleen wat eerder van huis vertrekken")
        time.sleep(2)
        print("")
    else:
        print("vul een geldig antwoord in")
        print("")
        time.sleep(2)
        donderdag()
    vrijdag()

def woensdag():
    print("voor woensdag heb ik geen keuze door naar de volgende dag")
    print("")
    time.sleep(2)
    donderdag()

def dinsdag():
    print("voor dinsdag avond heb ik ook een keuze")
    print("")
    time.sleep(2)
    print("of ik ga savond gamen")
    print("")
    time.sleep(2)
    print("of ik ga savonds sporten")
    print("")
    time.sleep(2)
    antwoord = input("Maak je keuze sporten of gamen: ")
    print("")
    time.sleep(2)
    print("")
    time.sleep(2)
    if antwoord == "gamen":
        print("oke savonds ga ik gamen")
        print("")
    time.sleep(2)
    if antwoord == "sporten":
        print("top savond ga ik sporten")
        time.sleep(2)
        print("")
    else:
        print("vul een geldig antwoord in")
        print("")
        time.sleep(2)
        dinsdag()
    woensdag()



def maandag():
    print("Ik heb 2 keuzens voor maandag of ik ga huiswerk maken na school")
    print("")
    time.sleep(2)
    print("of ik ga na school een vriend afspreken")
    print("")
    time.sleep(2)
    antwoord = input("Maak je keuze huiswerk of afspreken: ")
    print("")
    time.sleep(2)
    if antwoord == "huiswerk":
        print("goed na school ga ik aan mijn huiswerk")
    elif antwoord == "afspreken":
        print("Oke na school ga ik met een vriend afspreken")
        print("")
        time.sleep(2)
    else:
        print("vul een geldig antwoord in")
        print("")
        time.sleep(2)
        maandag()
    dinsdag()

begin()