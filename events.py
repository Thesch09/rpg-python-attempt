'''
#Event ideas#
Combat
Shop
HP fount
MP fount
Dead traveler
Town
Little Girl (THUNDERSPELL)
'''
import time
from rich import print



def do_combat(player, enemieses, e1, e2, e3):

    listEnemies = [e1, e2, e3]
    print(listEnemies[1])

    print(f"{player.first_name} {player.surname}, [red]{player.hp} HP[/red], level {player.level}")
    print("VS")
    for i in range(enemieses):
        print(i)
        print(f"{listEnemies[i].first_name} {listEnemies[i].surname}, [red]{listEnemies[i].hp} HP[/red], level {listEnemies[i].level}")
    
    turn_count = 1

    while player.is_alive() and e1.is_alive():
        print()
        print()
        print(f"It is turn number {turn_count}")
        player.fix_stf()
        time.sleep(1)
        print()
        for i in range(len(player.moves)):
            player.moves[i].cooldown()

        # Player action
        player.turn()
        time.sleep(0.5)
        print()
        

        # Enemy action
        # Un-hardcode it <- done <- Less done <- More done

        for i in range(enemieses):
            e1.fix_stf()
            for i in range(len(listEnemies[i].moves)):
                listEnemies[i].moves[i].cooldown()
            
            if listEnemies[i].is_alive:
                listEnemies[i].AI(listEnemies[i], player)
            else:
                print(f"{listEnemies[i].name} is dead!")
                
            time.sleep(0.5)
            print()
        
        # Increase turn_count so the fight doesn't last forever
        turn_count += 1
        if turn_count > 50:
            print("The battle ran out of time!")
            return
