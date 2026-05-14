import pandas as pd

data = pd.read_excel("restoran.xlsx")

def pelayanan_buruk(x):
    if x <= 30:
        return 1
    elif x >= 50:
        return 0
    else:
        return (50 - x) / 20

def pelayanan_sedang(x):
    if x <= 30 or x >= 80:
        return 0
    elif 30 < x < 55:
        return (x - 30) / 25
    else:
        return (80 - x) / 25

def pelayanan_baik(x):
    if x <= 60:
        return 0
    elif x >= 80:
        return 1
    else:
        return (x - 60) / 20

def harga_murah(x):
    if x <= 25000:
        return 1
    elif x >= 35000:
        return 0
    else:
        return (35000 - x) / 10000

def harga_sedang(x):
    if x <= 30000 or x >= 45000:
        return 0
    elif 30000 < x < 37500:
        return (x - 30000) / 7500
    else:
        return (45000 - x) / 7500

def harga_mahal(x):
    if x <= 40000:
        return 0
    elif x >= 55000:
        return 1
    else:
        return (x - 40000) / 15000

hasil = []

for index, row in data.iterrows():

    pelayanan = row["Pelayanan"]
    harga = row["harga"]

    rule1 = min(pelayanan_baik(pelayanan), harga_murah(harga))      
    rule2 = min(pelayanan_baik(pelayanan), harga_sedang(harga))     
    rule3 = min(pelayanan_baik(pelayanan), harga_mahal(harga))      

    rule4 = min(pelayanan_sedang(pelayanan), harga_murah(harga))    
    rule5 = min(pelayanan_sedang(pelayanan), harga_sedang(harga))   
    rule6 = min(pelayanan_sedang(pelayanan), harga_mahal(harga))    

    rule7 = min(pelayanan_buruk(pelayanan), harga_murah(harga))     
    rule8 = min(pelayanan_buruk(pelayanan), harga_sedang(harga))    
    rule9 = min(pelayanan_buruk(pelayanan), harga_mahal(harga))     

    total_rule = (
        rule1 + rule2 + rule3 +
        rule4 + rule5 + rule6 +
        rule7 + rule8 + rule9
    )

    if total_rule != 0:
        z = (
            (rule1 * 100) +
            (rule2 * 80) +
            (rule3 * 60) +
            (rule4 * 80) +
            (rule5 * 60) +
            (rule6 * 40) +
            (rule7 * 60) +
            (rule8 * 40) +
            (rule9 * 20)
        ) / total_rule
    else:
        z = 0
    hasil.append([
        row["id Pelanggan"],
        pelayanan,
        harga,
        z
    ])

hasil = sorted(hasil, key=lambda x: x[3], reverse=True)

print("===== 5 RESTORAN TERBAIK =====")

for i in range(5):
    print("ID:", hasil[i][0])
    print("Pelayanan:", hasil[i][1])
    print("Harga:", hasil[i][2])
    print("Skor Kelayakan:", hasil[i][3])
    print("----------------------------")