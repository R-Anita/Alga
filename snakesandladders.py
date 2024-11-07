from collections import deque
def quickestWayUp(ladders, snakes):
    # Letrehozom a tablat
    tabla = list(range(101))
    
    # A letrak es kigyok adatai alapjan frissitem a tablat
    # Ha a kezdeti pontjukra lepunk, akkor elvisz rogton a vegpontjukra
    for start, end in ladders:
        tabla[start] = end
    for start, end in snakes:
        tabla[start] = end
    
    # BFS
    # deque, mert jobb vele a pop, mint egy listaval
    # itt (aktualis mezo, dobasok szama), 1es mezorol indul, 0 dobassal
    queue = deque([(1, 0)])
    visited = [False] * 101  # mar erintett mezok
    visited[1] = True  # true, mert innen indul
    
    while queue:
        mezo, dobas = queue.popleft()
        
        # ha elerjuk az utolso mezot, adja vissza a dobasok szamat
        if mezo == 100:
            return dobas
        
        # dobasok
        for kocka_dobas in range(1, 7):
            szamitott_mezo = mezo + kocka_dobas
            
            # nem lephetunk tul az utolso mezon
            if szamitott_mezo <= 100:
                # ha letra vagy kigyo a szamitott mezo
                lepett_mezo = tabla[szamitott_mezo] 
                
                if not visited[lepett_mezo]:  # csak olyan mezot adunk hozza, ahol meg nem jartunk
                    visited[lepett_mezo] = True
                    queue.append((lepett_mezo, dobas + 1))
    
    # ha nem tudjuk elerni a 100as mezot
    return -1