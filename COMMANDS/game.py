import random

#desc
help_game = "game     :    lets you play a simple rpg \n"

def gameLoop():
    
    #player stats
    health= 100
    pots= 1
    #enemy stats
    def genEnemy(option):
            name = "zombie"

            health= random.randint(60,100)
            attack= random.randint(15,20)
            potDrop= random.randint(1,3)
            
            try:
                if option == 1:return health
                elif option == 2:return attack
                elif option == 3:return potDrop
                elif option == 4: return name
            except: 
                # im too lazy to edit all the genEnemy(4) so ill just make it so if theres no input, itll just return name 
                return name 
            
    eneHealth = genEnemy(1)   
    
    #game loop
    while True:
        print("You encountered a " + genEnemy(4) + "! What do you do?\nHealth:   " + str(health) + " Potions: " + str(pots))
        action = int(input("\n| (1)attack | (2)use a potion | (3)quit |  " ))
        if action == 1:
            attk = random.randint(15,20)
            print("You attacked the " + genEnemy(4) + " by " + str(attk) + " damage! " + " He now has " + str(eneHealth) + " health left! ")
            eneHealth = eneHealth-attk
        elif action == 2:
            if pots != 0:
                healed = random.randint(10,50) 
                health+= healed
                pots -=1
                print("You healed for " + str(healed) + "! ")
            else:                 
                print("You dont have any pots! " + genEnemy(4) + " uses this chance, and... ")
        elif action == 3:
            break
        else: print("You couldnt react in time, and" + genEnemy(4) +" uses this chance to... ")
        
        atk = genEnemy(2)
        
        print("\n" +genEnemy(4) + " attacks!\n" + genEnemy(4) + " attacks for " + str(atk) + " damage. You have: " + str(health-atk) + " HP left" )
        health= health-atk  
        
        if eneHealth <= 0:
            potdrop = genEnemy(3)
            print("congrats! you defeated " + genEnemy(4) + "! You got: " + str(potdrop) + " potions from him. " )
            eneHealth = genEnemy(1)#generates new health pool for a new enemy
            pots = potdrop+pots #adds the drops to your inv
            
        elif health <= 0:
            print("You died! Try again next time! \n\n")
            break

        
