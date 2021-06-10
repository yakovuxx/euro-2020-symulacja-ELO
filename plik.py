import operator
import random

def goaldiff(szanse):
    #print(szanse)
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

def meczgrupowy(grupa, a, b):
    print(grupa[a][0], grupa[b][0])
    rankinga=grupa[a][1]
    rankingb=grupa[b][1]
    if grupa[a][0]=="Italy" or grupa[a][0]=="Denmark" or grupa[a][0]=="Russia" or grupa[a][0]=="Netherlands" or grupa[a][0]=="England" or grupa[a][0]=="Scotland" or grupa[a][0]=="Spain" or grupa[a][0]=="Germany" or grupa[a][0]=="Hungary":
        rankinga+=100
    else:
        if grupa[b][0]=="Italy" or grupa[b][0]=="Denmark" or grupa[b][0]=="Russia" or grupa[b][0]=="Netherlands" or grupa[b][0]=="England" or grupa[b][0]=="Scotland" or grupa[b][0]=="Spain" or grupa[b][0]=="Germany" or grupa[b][0]=="Hungary":
            rankingb+=100
    print(rankinga, rankingb)
    szanse=1 / (pow(10,((-(rankinga-rankingb))/400))+1)
    print(szanse)
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
    print(zmiana)
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

def meczpucharowy(faza, a, b, nastepnafaza, host):
    print(faza[a][0], faza[b][0])
    rankinga=faza[a][1]
    rankingb=faza[b][1]
    if host==faza[a][0]:
        rankinga+=100
    if host==faza[b][0]:
        rankingb+=100
    print(rankinga, rankingb)
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
    print(zmiana)
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

def grupa(grupa):
    print(meczgrupowy(grupa, 0, 1))
    print(meczgrupowy(grupa, 2, 3))
    print(meczgrupowy(grupa, 0, 2))
    print(meczgrupowy(grupa, 1, 3))
    print(meczgrupowy(grupa, 0, 3))
    print(meczgrupowy(grupa, 1, 2))
    return (grupa)

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


jednaosma=[]
cwiercfinaly=[]
polfinaly=[]
final=[]
zwyciesca=[]
trzeci=[]

def grupka(groupa):
    grupa(groupa)
    print(tabela(groupa))
    hu=tabela(groupa)
    trzeci.append(hu[2])
    jednaosma.append(hu[0])
    jednaosma.append(hu[1])

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

def euro():
    grupka(A)
    grupka(B)
    grupka(C)
    grupka(D)
    grupka(E)
    grupka(F)

    trzeci.sort(key=operator.itemgetter(8, 7, 5, 3), reverse=True)
    kod = ''.join(sorted(trzeci[4][9] + trzeci[5][9]))
    print(kod)
    awansztrzeciego(kod)
    print(trzeci)
    print('\n')
    print(meczpucharowy(jednaosma, 2, 12, cwiercfinaly, 'Spain'))
    print(meczpucharowy(jednaosma, 0, 5, cwiercfinaly, 'England'))
    print(meczpucharowy(jednaosma, 10, 15, cwiercfinaly, 'Romania'))
    print(meczpucharowy(jednaosma, 7, 9, cwiercfinaly, 'Denmark'))
    print(meczpucharowy(jednaosma, 8, 14, cwiercfinaly, 'Scotland'))
    print(meczpucharowy(jednaosma, 6, 11, cwiercfinaly, 'England'))
    print(meczpucharowy(jednaosma, 4, 13, cwiercfinaly, 'Hungary'))
    print(meczpucharowy(jednaosma, 1, 3, cwiercfinaly, 'Netherlands'))
    print('\n')
    print(meczpucharowy(cwiercfinaly, 0, 1, polfinaly, 'Germany'))
    print(meczpucharowy(cwiercfinaly, 2, 3, polfinaly, 'Russia'))
    print(meczpucharowy(cwiercfinaly, 4, 5, polfinaly, 'Italy'))
    print(meczpucharowy(cwiercfinaly, 6, 7, polfinaly, 'Azerbaijan'))
    print('\n')
    print(meczpucharowy(polfinaly, 0, 1, final, 'England'))
    print(meczpucharowy(polfinaly, 2, 3, final, 'England'))
    print('\n')
    print(meczpucharowy(final, 0, 1, zwyciesca, 'England'))
    print(zwyciesca[0][0])
    zwyciescy.append(zwyciesca[0][0])

for i in range(1):
    euro()
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

print(zwyciescy)
