#Este es un juego de ahorcados, espero les guste, puse solo 4 palabras, pero pueden agregar mas si gustan :)
import random

words = ("manzana","pera","pizza","uva")
Muñequito = {
    0: ("---  ",
        "|  ",
        "|  "),
    1: (" o ",
        "   ",
        "   "),
    2: ("--- o ",
        "|   | ",
        "|   "),
    3: ("--- o ",
        "|  /| ",
        "|     "),
    4: ("--- o ",
        "|  /|\\",
        "|     "),
    5: ("--- o ",
        "|  /|\\",
        "|  /   "),
    6: ("--- o  ",
        "|  /|\\",
        "|  / \\"),    
}

def muñequito(incorrectas):
    print("******************")
    for line in Muñequito[incorrectas]:
        print(line)
    print("******************")
    pass
def mostrar_pista(pista):
    print(" ".join(pista))

def mostrar_respuesta(respuesta):
    print(" ".join(respuesta))

def main():
    respuesta = random.choice(words)
    pista = ["_"] * len(respuesta)
    incorrectas = 0
    buenas = set()
    is_running = True
    
    while is_running:
        muñequito(incorrectas)
        mostrar_pista(pista)
        Adivinar = input("¿Que letra crees que completara la palabra?:").lower()
        
        if len(Adivinar) != 1 or not Adivinar.isalpha():
            print("*****")
            print("Solo una letra por intento")
            print("Intenta denuevo....")
            continue
        if Adivinar in buenas:
            print(f"Ya adivinaste esta palabra.")
            continue
        buenas.add(Adivinar)
        
        if Adivinar in respuesta:
            for i in range(len(respuesta)):
                if respuesta[i] == Adivinar:
                    pista[i] = Adivinar      
        else:
            incorrectas += 1
            
        if "_" not in pista:
            muñequito(incorrectas)
            mostrar_respuesta(respuesta)
            print("GANASTE")
            is_running = False
        elif incorrectas >= len(Muñequito) - 1:
            muñequito(incorrectas)
            mostrar_respuesta(respuesta)
            print("PERDISTE")
            is_running = False
                    
if __name__ == "__main__":
    main()
    
