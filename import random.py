import random

print("välkommen till dagens boxnings fight")

def fight(spelare1, spelare2):
    hp1 = 100
    hp2 = 100
    
    while hp1 > 0 and hp2 > 0:
        
        skada1 = random.randint(5, 15)
        hp2 -= skada1
        print(spelare1 + " attackerar " + spelare2 + " och gör " + str(skada1) + " skada!")
        print(spelare2 + " har " + str(hp2) + " HP kvar.\n")
        
        if hp2 <= 0:
            print(spelare2 + " har blivit besegrad! " + spelare1 + " vinner!")
            break
        
        skada2 = random.randint(5, 15)
        hp1 -= skada2
        print(spelare2 + " attackerar " + spelare1 + " och gör " + str(skada2) + " skada!")
        print(spelare1 + " har " + str(hp1) + " HP kvar.\n")
        
        if hp1 <= 0:
            print(spelare1 + " har blivit besegrad! " + spelare2 + " vinner!")
            break

def main():
    spelare1 = input("Skriv in namnet på spelare 1: ")
    spelare2 = input("Skriv in namnet på spelare 2: ")
    
    fight(spelare1, spelare2)

if __name__ == "__main__":
    main()

    
