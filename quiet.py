import operator
import random
import time
f=open("winners.txt", "w+")
g=open("wyszli.txt", "w+")
#h=open("trzecie.txt", "w+")
k=open("polskagrupa.txt", "w+")


#FUNKCJA LOSUJE WYNIK W POSTACI RÓŻNICY BRAMEK, PATRZĄC Z PERSPEKTYWY PIERWSZEJ DRUZYNY
def goaldiff(szanse):
    #print(szanse)
    #TE WZORY PONIŻEJ TO WZORY NA PRAWDOPODOBIENSTWO WYGRANEJ JEDNĄ, DWOMA I TRZEMA LUB WIĘCEJ BRAMKAMI
    #UZYSKANE NA PODSTAWIE LINII TRENDU Z WYKRESÓW Z DANYCH OD BUKHMACHERÓW
    #KONKRETNIE WYKRES SZANSE NA WYGRANĄ U BUKA (Z ODLICZONYM REMISEM) vs SZANSE NA TE BRAMKI
    #NO I TERAZ W MIEJSCE SZANS JEST SZANSA OBLICZONA Z RANKINGU ELO
    plus1 = -2.3487*pow(szanse,6)+5.3368*pow(szanse,5)-5.5102*pow(szanse,4)+3.7108*pow(szanse,3)-1.8816*pow(szanse,2)+0.8416*pow(szanse,1)
    plus2= -0.1857*pow(szanse,6) - 1.6143*pow(szanse,5) + 4.3873*pow(szanse,4) - 3.5538*pow(szanse,3) + 1.0888*pow(szanse,2) + 0.115*pow(szanse,1)
    plus3= -4.3192*pow(szanse,6) + 14.799*pow(szanse,5) - 16.469*pow(szanse,4) + 7.8405*pow(szanse,3) - 1.4527*pow(szanse,2) + 0.1454*pow(szanse,1)
    minus1=-2.3487*pow(szanse-1,6)-5.3368*pow(szanse-1,5)-5.5102*pow(szanse-1,4)-3.7108*pow(szanse-1,3)-1.8816*pow(szanse-1,2)-0.8416*pow(szanse-1,1)
    minus2= -0.1857*pow(szanse-1,6) + 1.6143*pow(szanse-1,5) + 4.3873*pow(szanse-1,4) + 3.5538*pow(szanse-1,3) + 1.0888*pow(szanse-1,2) - 0.115*pow(szanse-1,1)
    minus3= -4.3192*pow(szanse-1,6) - 14.799*pow(szanse-1,5) - 16.469*pow(szanse-1,4) - 7.8405*pow(szanse-1,3) - 1.4527*pow(szanse-1,2) - 0.1454*pow(szanse-1,1)
    los=random.random()
    if los<(plus1):
        return 1
    if los<(plus1+plus2):
        return 2
    if los<(plus1+plus2+plus3):
        return 3
    if los<(plus1+plus2+plus3+minus1):
        return -1
    if los<(plus1+plus2+plus3+minus1+minus2):
        return -2
    if los<(plus1+plus2+plus3+minus1+minus2+minus3):
        return -3
    else:
        return 0

#FUNKCJA LOSUJE DOKLADNY WYNIK MECZU, SZANSE NA WYNIKI NA PODSTAWIE DANYCH ZNALEZIONYCH W NECIE
#WYCHODZI ZAJEBIŚCIE, ŚREDNIA BRAMEK JAK W RZECZYWISTOŚCI
def result(diff):
    los = 100 * random.random()
    resulta, resultb = 0, 0
    absdiff=abs(diff)
    if absdiff==0:
        if 0<=los<=32.69:
            resulta, resultb = 0, 0
        if 32.69<los<=79.39:
            resulta, resultb = 1, 1
        if 79.39<los<=96.7:
            resulta, resultb = 2, 2
        if 96.7<los<=99.65:
            resulta, resultb = 3, 3
        if 99.65<los<=100:
            resulta, resultb = 4, 4
    if absdiff==1:
        if 0<=los<=49.84:
            resulta, resultb = 1, 0
        if 49.84<los<=88.19:
            resulta, resultb = 2, 1
        if 88.19<los<=98.12:
            resulta, resultb = 3, 2
        if 98.12<los<=99.87:
            resulta, resultb = 4, 3
        if 99.87<los<=100:
            resulta, resultb = 5, 4
    if absdiff==2:
        if 0<=los<=62.04:
            resulta, resultb = 2, 0
        if 62.04<los<=93.24:
            resulta, resultb = 3, 1
        if 93.24<los<=99.26:
            resulta, resultb = 4, 2
        if 99.26<los<=100:
            resulta, resultb = 5, 3
    if absdiff==3:
        if 0<=los<=43.01:
            resulta, resultb = 3, 0
        if 43.01<los<=61.24:
            resulta, resultb = 4, 0
        if 61.24<los<=77.19:
            resulta, resultb = 4, 1
        if 77.19<los<=83.92:
            resulta, resultb = 5, 0
        if 83.92<los<=90.07:
            resulta, resultb = 5, 1
        if 90.07<los<=93.01:
            resulta, resultb = 5, 2
        if 93.01<los<=96.47:
            resulta, resultb = 6, 0
        if 96.47<los<=98.37:
            resulta, resultb = 6, 1
        if 98.37<los<=99.02:
            resulta, resultb = 6, 2
        if 99.02<los<=98.22:
            resulta, resultb = 6, 3
        if 99.22<los<=99.67:
            resulta, resultb = 7, 1
        if 99.67<los<=100:
            resulta, resultb = 7, 2
    if diff<0:
        resulta, resultb = resultb, resulta
    return (resulta, resultb)

#FUNKCJA LOSUJE KARNE, JAKO ŻE KARNE TO LOTERIA TO RANKING NIE MA WPLYWU XD
def karne():
    wynika=0
    wynikb=0
    for i in range(5):
        if random.random()<0.76:
            wynika+=1
        if random.random()<0.76:
            wynikb+=1
        if abs(wynika-wynikb)>4-i:
            return (wynika, wynikb)
    while wynika==wynikb:
        if random.random()<0.75:
            wynika+=1
        if random.random()<0.75:
            wynikb+=1
    return (wynika, wynikb)

#FUNKCJA LOSUJE WYNIK MECZU NA PODSTAWIE SZANS OBLICZONYCH JAK W RANKINGU ELO
#I WSTAWIA DANE PO MECZU DO TABELI GRUPY
def meczgrupowy(grupa, a, b):
    rankinga=grupa[a][1]
    rankingb=grupa[b][1]
    if grupa[a][0]=="Italy" or grupa[a][0]=="Denmark" or grupa[a][0]=="Russia" or grupa[a][0]=="Netherlands" or grupa[a][0]=="England" or grupa[a][0]=="Scotland" or grupa[a][0]=="Spain" or grupa[a][0]=="Germany" or grupa[a][0]=="Hungary":
        rankinga+=100
    else:
        if grupa[b][0]=="Italy" or grupa[b][0]=="Denmark" or grupa[b][0]=="Russia" or grupa[b][0]=="Netherlands" or grupa[b][0]=="England" or grupa[b][0]=="Scotland" or grupa[b][0]=="Spain" or grupa[b][0]=="Germany" or grupa[b][0]=="Hungary":
            rankingb+=100
    szanse=1 / (pow(10,((-(rankinga-rankingb))/400))+1)
    wynik=result(goaldiff(szanse))
    roz=abs(wynik[0]-wynik[1])
    k=50
    if roz>=2:
        if roz==2:
            k+=25
        if roz>2:
            k+=((0.75+(roz-3)/8)*50)
    if wynik[0]>wynik[1]:
        res=1-szanse
    if wynik[0]==wynik[1]:
        res=0.5-szanse
    if wynik[0]<wynik[1]:
        res=0-szanse
    zmiana=round(k*res)
    grupa[a][1]+=zmiana
    grupa[b][1]-=zmiana
    grupa[a][5] += wynik[0]
    grupa[b][5] += wynik[1]
    grupa[a][6] += wynik[1]
    grupa[b][6] += wynik[0]
    if wynik[0]>wynik[1]:
        grupa[a][2] += 1
        grupa[b][4] += 1
    if wynik[1]>wynik[0]:
        grupa[b][2] += 1
        grupa[a][4] += 1
    if wynik[0]==wynik[1]:
        grupa[b][3] += 1
        grupa[a][3] += 1
    return wynik

#FUNKCJA LOSUJE WYNIK MECZU NA PODSTAWIE SZANS OBLICZONYCH JAK W RANKINGU ELO
#I WSTAWIA PO MECZU DANE DO TABLIC Z FAZAMI PUCHAROWYMI
def meczpucharowy(faza, a, b, nastepnafaza, host):
    rankinga=faza[a][1]
    rankingb=faza[b][1]
    if host==faza[a][0]:
        rankinga+=100
    if host==faza[b][0]:
        rankingb+=100
    szanse=1 / (pow(10,((-(rankinga-rankingb))/400))+1)
    wynik=result(goaldiff(szanse))
    roz = abs(wynik[0] - wynik[1])
    k = 50
    if roz >= 2:
        if roz == 2:
            k += 25
        if roz > 2:
            k += ((0.75 + (roz - 3) / 8) * 50)
    if wynik[0] > wynik[1]:
        res = 1 - szanse
    if wynik[0] == wynik[1]:
        res = 0.5 - szanse
    if wynik[0] < wynik[1]:
        res = 0 - szanse
    zmiana = round(k * res)
    faza[a][1]+=zmiana
    faza[b][1]-=zmiana
    if wynik[0]==wynik[1]:
        karniaki=karne()
    if nastepnafaza is not None:
        if wynik[0]>wynik[1]:
            nastepnafaza.append(faza[a])
        if wynik[1]>wynik[0]:
            nastepnafaza.append(faza[b])
        if wynik[0]==wynik[1]:
            if karniaki[0]>karniaki[1]:
                nastepnafaza.append(faza[a])
            if karniaki[0]<karniaki[1]:
                nastepnafaza.append(faza[b])
    if wynik[0]!=wynik[1]:
        return wynik
    if wynik[0]==wynik[1]:
        return (wynik, karniaki)

#FUNKJA PRZEPROWADZA 6 MECZÓW GRUPOWYCH
def grupa(grupa):
    (meczgrupowy(grupa, 0, 1))
    (meczgrupowy(grupa, 2, 3))
    (meczgrupowy(grupa, 0, 2))
    (meczgrupowy(grupa, 1, 3))
    (meczgrupowy(grupa, 0, 3))
    (meczgrupowy(grupa, 1, 2))
    return (grupa)

#FUNKCJA LICZY RÓŻNICE BRAMEK I PUNKTY W GRUPIE I SORTUJE JĄ WG 4 KRYTERIÓW
def tabela(data):
    data = [[data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][5] - data[0][6],
             3 * data[0][2] + data[0][3], data[0][7]],
            [data[1][0], data[1][1], data[1][2], data[1][3], data[1][4], data[1][5], data[1][6], data[1][5] - data[1][6],
            3 * data[1][2] + data[1][3], data[1][7]],
            [data[2][0], data[2][1], data[2][2], data[2][3], data[2][4], data[2][5], data[2][6], data[2][5] - data[2][6],
            3 * data[2][2] + data[2][3], data[2][7]],
            [data[3][0], data[3][1], data[3][2], data[3][3], data[3][4], data[3][5], data[3][6], data[3][5] - data[3][6],
            3 * data[3][2] + data[3][3], data[3][7]]]
    data.sort(key=operator.itemgetter(8, 7, 5, 3), reverse=True)
    return data

#INPUT: GRUPY, CZYLI ZESPÓL, JEGO ELO, W, R, P, Z, S, GRUPA
A = [["Italy", 2013, 0, 0, 0, 0, 0, "A"],
    ["Turkey", 1801, 0, 0, 0, 0, 0, "A"],
    ["Switzerland", 1890, 0, 0, 0, 0, 0, "A"],
    ["Wales", 1833, 0, 0, 0, 0, 0, "A"]]
B = [["Denmark", 1973, 0, 0, 0, 0, 0, "B"],
    ["Finland", 1685, 0, 0, 0, 0, 0, "B"],
    ["Belgium", 2100, 0, 0, 0, 0, 0, "B"],
    ["Russia", 1744, 0, 0, 0, 0, 0, "B"]]
C = [["Netherlands", 1950, 0, 0, 0, 0, 0, "C"],
    ["Ukraine", 1814, 0, 0, 0, 0, 0, "C"],
    ["Austria", 1747, 0, 0, 0, 0, 0, "C"],
    ["North Macedonia", 1603, 0, 0, 0, 0, 0, "C"]]
D = [["England", 1982, 0, 0, 0, 0, 0, "D"],
    ["Croatia", 1825, 0, 0, 0, 0, 0, "D"],
    ["Scotland", 1678, 0, 0, 0, 0, 0, "D"],
    ["Czech Republic", 1768, 0, 0, 0, 0, 0, "D"]]
E = [["Spain", 2033, 0, 0, 0, 0, 0, "E"],
    ["Sweden", 1849, 0, 0, 0, 0, 0, "E"],
    ["Poland", 1796, 0, 0, 0, 0, 0, "E"],
    ["Slovakia", 1656, 0, 0, 0, 0, 0, "E"]]
F = [["Germany", 1936, 0, 0, 0, 0, 0, "F"],
    ["France", 2088, 0, 0, 0, 0, 0, "F"],
    ["Portugal", 2039, 0, 0, 0, 0, 0, "F"],
    ["Hungary", 1741, 0, 0, 0, 0, 0, "F"]]

#PUSTE TABLICZKI DO WYPELNIANIA W FAZIE PUCHAROWEJ
jednaosma=[]
cwiercfinaly=[]
polfinaly=[]
final=[]
zwyciesca=[]
trzeci=[]

#WYPELNIA TABLICE NA TRZECIE MIEJSCA I FAZE PUCHAROWA
def grupka(groupa):
    grupa(groupa)
    hu=tabela(groupa)
    trzeci.append(hu[2])
    if groupa[0][0]=="Spain":
        for i in range(4):
            k.write(str(hu[i][0])+';')
        k.write('\n')
    jednaosma.append(hu[0])
    jednaosma.append(hu[1])

#DOPASOWUJE PRZEBIEG FAZY PUCHAROWEJ NA PODSTAWIE TEGO KTO WYSZEDL (A RACZEJ KTO NIE XD) Z 3 MIEJSC
def awansztrzeciego(kod):
    if kod=="EF":
        jednaosma.append(tabela(A)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(B)[2])
        jednaosma.append(tabela(C)[2])
    if kod=="DF":
        jednaosma.append(tabela(A)[2])
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(B)[2])
        jednaosma.append(tabela(C)[2])
    if kod=="DE":
        jednaosma.append(tabela(A)[2])
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(B)[2])
        jednaosma.append(tabela(C)[2])
    if kod=="CF":
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(A)[2])
        jednaosma.append(tabela(B)[2])
    if kod=="CE":
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(A)[2])
        jednaosma.append(tabela(B)[2])
    if kod=="CD":
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(B)[2])
        jednaosma.append(tabela(A)[2])
    if kod=="BF":
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(C)[2])
        jednaosma.append(tabela(A)[2])
    if kod=="BE":
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(C)[2])
        jednaosma.append(tabela(A)[2])
    if kod=="BD":
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(C)[2])
        jednaosma.append(tabela(A)[2])
    if kod=="BC":
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(A)[2])
    if kod=="AF":
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(B)[2])
        jednaosma.append(tabela(C)[2])
    if kod=="AE":
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(C)[2])
        jednaosma.append(tabela(B)[2])
    if kod=="AD":
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(C)[2])
        jednaosma.append(tabela(B)[2])
    if kod=="AC":
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(B)[2])
    if kod=="AB":
        jednaosma.append(tabela(F)[2])
        jednaosma.append(tabela(E)[2])
        jednaosma.append(tabela(D)[2])
        jednaosma.append(tabela(C)[2])

zwyciescy=[]

#WPIERDOLENIE CALEGO TURNIEJU W JEDNA PROSTA FUNKCE
def euro():
    #FAZA GRUPOWA
    grupka(A)
    grupka(B)
    grupka(C)
    grupka(D)
    grupka(E)
    grupka(F)
    #TRZECIE MIEJSCA
    trzeci.sort(key=operator.itemgetter(8, 7, 5, 3), reverse=True)
    kod = ''.join(sorted(trzeci[4][9] + trzeci[5][9]))
    awansztrzeciego(kod)
    #h.write(kod)
    #h.write('\n')
    #1/8 FINALU
    (meczpucharowy(jednaosma, 2, 12, cwiercfinaly, 'Spain'))
    (meczpucharowy(jednaosma, 0, 5, cwiercfinaly, 'England'))
    (meczpucharowy(jednaosma, 10, 15, cwiercfinaly, 'Romania'))
    (meczpucharowy(jednaosma, 7, 9, cwiercfinaly, 'Denmark'))
    (meczpucharowy(jednaosma, 8, 14, cwiercfinaly, 'Scotland'))
    (meczpucharowy(jednaosma, 6, 11, cwiercfinaly, 'England'))
    (meczpucharowy(jednaosma, 4, 13, cwiercfinaly, 'Hungary'))
    (meczpucharowy(jednaosma, 1, 3, cwiercfinaly, 'Netherlands'))
    #1/4 FINALU
    (meczpucharowy(cwiercfinaly, 0, 1, polfinaly, 'Germany'))
    (meczpucharowy(cwiercfinaly, 2, 3, polfinaly, 'Russia'))
    (meczpucharowy(cwiercfinaly, 4, 5, polfinaly, 'Italy'))
    (meczpucharowy(cwiercfinaly, 6, 7, polfinaly, 'Azerbaijan'))
    #1/2 FINALU
    (meczpucharowy(polfinaly, 0, 1, final, 'England'))
    (meczpucharowy(polfinaly, 2, 3, final, 'England'))
    #FINAL
    (meczpucharowy(final, 0, 1, zwyciesca, 'England'))
    f.write(zwyciesca[0][0])
    f.write('\n')
    #zwyciescy.append(zwyciesca[0][0])



start=time.time()

#WYWOLANIE TEGO WSZYSTKIEGO I POTEM WYCZYSZCZENIE, DOWOLNĄ ILOSC RAZY
#NA MOIM KOMPIE ~1750 SYMULACJI W 1 SEKUNDE
for i in range(1000000):
    euro()
    for i in range(len(jednaosma)):
        g.write(jednaosma[i][0])
        g.write(';')
    g.write('\n')
    jednaosma = []
    cwiercfinaly = []
    polfinaly = []
    final = []
    zwyciesca = []
    trzeci = []
    A = [["Italy", 2013, 0, 0, 0, 0, 0, "A"],
         ["Turkey", 1801, 0, 0, 0, 0, 0, "A"],
         ["Switzerland", 1890, 0, 0, 0, 0, 0, "A"],
         ["Wales", 1833, 0, 0, 0, 0, 0, "A"]]
    B = [["Denmark", 1973, 0, 0, 0, 0, 0, "B"],
         ["Finland", 1685, 0, 0, 0, 0, 0, "B"],
         ["Belgium", 2100, 0, 0, 0, 0, 0, "B"],
         ["Russia", 1744, 0, 0, 0, 0, 0, "B"]]
    C = [["Netherlands", 1950, 0, 0, 0, 0, 0, "C"],
         ["Ukraine", 1814, 0, 0, 0, 0, 0, "C"],
         ["Austria", 1747, 0, 0, 0, 0, 0, "C"],
         ["North Macedonia", 1603, 0, 0, 0, 0, 0, "C"]]
    D = [["England", 1982, 0, 0, 0, 0, 0, "D"],
         ["Croatia", 1825, 0, 0, 0, 0, 0, "D"],
         ["Scotland", 1678, 0, 0, 0, 0, 0, "D"],
         ["Czech Republic", 1768, 0, 0, 0, 0, 0, "D"]]
    E = [["Spain", 2033, 0, 0, 0, 0, 0, "E"],
         ["Sweden", 1849, 0, 0, 0, 0, 0, "E"],
         ["Poland", 1796, 0, 0, 0, 0, 0, "E"],
         ["Slovakia", 1656, 0, 0, 0, 0, 0, "E"]]
    F = [["Germany", 1936, 0, 0, 0, 0, 0, "F"],
         ["France", 2088, 0, 0, 0, 0, 0, "F"],
         ["Portugal", 2039, 0, 0, 0, 0, 0, "F"],
         ["Hungary", 1741, 0, 0, 0, 0, 0, "F"]]
    #if i%10000==0:
        #print(i/10000)

end=time.time()
print(end-start)
#print(zwyciescy)
#print(count)