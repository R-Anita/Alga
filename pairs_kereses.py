def pairs(k, arr):
    #Halmazkent kezelem, mert keresni akarok majd benne (hasito tabla miatt O(1)) 
    halmaz = set(arr)
    mennyiseg = 0
    #Megnezem szerepel-e a halmazban egy szam parja, azaz a szam+k
    for par in arr:
        if par+k in halmaz:
            mennyiseg += 1
    
    return mennyiseg