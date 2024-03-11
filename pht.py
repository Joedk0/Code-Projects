import random
import math

def jugar():
    
    usuario = input("ehlige una opcion. 'p' para piedra, 'h' para hoja, o 't' para tijeras: ")
    
    elementos = ['p', 'h', 't']
    computador = random.choice(elementos)
    
    if usuario == computador:
        return(0, usuario, computador)
    
    if is_ganador(usuario, computador):
        return(1, usuario,computador)
    return (-1,usuario, computador)

def is_ganador(jugador, oponente):
    #devolvemos True si el jugador le gana al oponente
    #Condicion para ganar: p > t, t > h, h > p

    if(jugador == 'p' and oponente == 't') or (jugador == 't' and oponente =='h') or (jugador == 'h' and oponente == 'p'):
        return True 
    return False

def el_mejor_jugador(n):
    #para ganar el juego, ceil(n/2) (ie. 2/3, 3/5, 4/7)
    
    jugador_contar = 0
    computador_contar = 0
    para_ganar = math.ceil(n/2)
    print(para_ganar)

    while jugador_contar < para_ganar and computador_contar < para_ganar:
    
        resultado, usuario, computador = jugar()

        #empate
        if resultado ==0:
            print("Es un empate. tu y el computador han elegido {}".format(usuario))
        
        #tu ganas
        elif resultado ==1: 
            jugador_contar += 1
            print("tu haz elegido {} y el computador {}. ganaste".format(usuario,computador))
        
    else:
        computador_contar +=1
        print("tu haz elegido {} y el computador {}. perdiste".format(usuario,computador))
        
    if jugador_contar > computador_contar:
        print("haz ganado los mejores de {} juegos. alto capo".format(n))
    else:
        print("el pc hizo mas {} juegos".format(n))
        

if __name__ == "__main__":
    el_mejor_jugador(5)