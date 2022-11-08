from random import choices, shuffle

SOORTEN = "Hearts", "Diamonds", "Spades", "Clubs"

KAARTEN = "Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"

WAARDEN = {"Two": 2,"Three": 3,"Four": 4,"Five": 5,"Six": 6,"Seven": 7,"Eight": 8,"Nine": 9,"Ten": 10,"Jack": 10,"Queen": 10,"King": 10,"Ace": 11}

decklijst = []
spelerhand = []
computerhand = []
handwaardenspeler = []
handwaardencomputer = []
def start():
    print('WELKOM OP SYNTRAS BLACKJACK!')

def deck():
    for soort in SOORTEN:
            for kaart in KAARTEN:
                decklijst.append((soort,kaart))

def deckshuffle():
    shuffle(decklijst)

def deal_cards_speler():
    for speler in range(2):
        speler = choices(decklijst)
        spelerhand.append(speler)
    return speler

def deal_card_speler():
    speler = choices(decklijst)
    spelerhand.append(speler)
    return speler

def deal_card_computer():
    computer = choices(decklijst)
    computerhand.append(computer)
    return computer

def verdubbelen(geld):
    bedrag = geld*2
    print(f'U INZET IS NU {bedrag}!')
    geld = bedrag
    return bedrag

def tekst(geld):
    print('<---- BLACKJACK TABLE ---->')
    print(f'DIT IS U ORIGINEEL BEDRAG {geld}!')
    print('SPELER HEEFT ---->>>>',spelerhand)
    print('COMPUTER HEEFT ---->>>>',computerhand)

def inzet():
    counter=0
    while counter != 1:
        try:
            keuze = int(input('KIES EEN BEDRAG VAN MAX 50Euro INZET!:  '))
            counter +=1
        except:
            print('DIT IS ZIJN GEEN NUMMERS!')
            continue
        return keuze  


def blackjack_keuzes():
    counter=0
    while counter != 1:
        keuzelijst = ['passen','kopen','splitsen','verdubbelen','opgeven']
        keuze = input('KIES EEN OPTIE -->>  passen/kopen/splitsen/verdubbelen/opgeven: ')
        if keuze not in keuzelijst:
            print('Geef correcte input aub !')
            continue
        counter += 1
    return keuze


def Keuzes_Maken(opties,geld):
    if opties == 'opgeven':
        print('U HEBT OPGEGEVEN!')
    if opties == 'kopen':
        deal_card_speler()
    if opties == 'passen':
        print('YOU PASS !')
        pass
    if opties == 'splitsen':
        pass
    if opties == 'verdubbelen':
        verdubbelen(geld)

   
def berekenen():
    for x in WAARDEN:
        if x in spelerhand:
            handwaardenspeler.append(WAARDEN.values)
    for y in WAARDEN:
        if y in computerhand:
            handwaardencomputer.append(WAARDEN.values)
    print(handwaardenspeler)
    print(handwaardencomputer)

def kaarten_optellen_speler():
    return sum(handwaardenspeler)

def kaarten_optellen_computer():
    return sum(handwaardencomputer)
    
def game():
    start()
    deck()
    deckshuffle()
    geld = inzet()
    deal_cards_speler()
    deal_card_computer()
    while True:
        tekst(geld)
        opties = blackjack_keuzes()
        Keuzes_Maken(opties,geld)
        tekst(geld)
        berekenen()
        sum1 = kaarten_optellen_speler()
        sum2 = kaarten_optellen_computer()
        if sum1 >= 21:
            print('speler wint!')
        if sum2 >= 21:
            print('Het huis wint!')
        break

game()
        
    


   