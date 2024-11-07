# Fák, gráfok - HackerRank - Snakes and Ladders
## A feladat leírása
Markov előveszi a Snakes and Ladders játékot, ránéz a táblára és azon gondolkodik: "Ha mindig azt a számot dobnám, amit akarok, mi lenne a legkevesebb dobás, amivel elérhetem a célt?"
Szabályok:
A játék egy dobókockával van játszva, amelynek oldalai 1-től 6-ig vannak számozva.
A játékos az 1-es mezőről indul, és pontosan el kell érnie a 100-as mezőt. Ha a dobott szám a játékos számára túl nagy lépést jelentene (túllépné a 100-as mezőt), akkor nem történik mozgás.
Ha a játékos a létra aljára lép, fel kell másznia rajta. A létrák csak felfelé működnek, tehát ha valaki létrára lép, a létra végére kerül.
Ha a játékos a kígyó szájához érkezik, le kell csúsznia rajta, és a kígyó farkánál köt ki. A kígyók csak lefelé működnek, tehát ha a játékos kígyóra lép, a kígyó farkára kerül.
## A feladat megoldása
https://github.com/R-Anita/Alga/blob/main/snakesandladders.py
## Rövid magyarázat
Létrehozok egy listát a tábla szemléltetésére. A létrák és kígyók kezdeti és végpontjait beállítom a listában. Szélességi keresést alkalmazva megnézem, hogy legkevesebb hány dobásból lehet eljutni a tábla végére. 