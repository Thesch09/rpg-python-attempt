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



def do_combat(player, e):

    print(f"{player.first_name} {player.surname}, [red]{player.hp} HP[/red], level {player.level}")
    print("VS")
    print(f"{e.first_name} {e.surname}, [red]{e.hp} HP[/red], level {player.level}")
    turn_count = 1

    while player.is_alive() and e.is_alive():
        print()
        print()
        print(f"It is turn number {turn_count}")
        player.fix_stf()
        time.sleep(1)
        print()

        # Player action
        player.turn()
        time.sleep(0.5)
        if not e.is_alive():
            break
        print()
        e.fix_stf()

        # Enemy action
        # Un-hardcode it <- done <- Less done <- More done

        e.AI(e, player)
            
        time.sleep(0.5)
        print()
        
        # Increase turn_count so the fight doesn't last forever
        turn_count += 1
        if turn_count > 50:
            print("The battle ran out of time!")
            return