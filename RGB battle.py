# RPG battle game

import random



def game_start():

    player_health = 100
    enemy_health = 100

    while player_health >0 and enemy_health >0:

        player_move = input("\nEnter your move: ").lower()

        enemy_attack = random.randint(10,35)

        print(f'Enemy attack value: {enemy_attack}')
        
        if player_move == 'attack':

            
            player_attack = random.randint(10,30)
            print(f'Player attack value: {player_attack}')

            if (player_attack - enemy_attack) > 0:
                enemy_health = enemy_health- (player_attack-enemy_attack)

                if enemy_health >100:
                    enemy_health =100
                

            elif (player_attack - enemy_attack) < 0:
                
                player_health = player_health-(enemy_attack-player_attack)

                if player_health >100:
                    player_health =100
                
               

            
        elif player_move == "defend":

            player_health = player_health - (enemy_attack/2)

        elif player_move == "heal":

            player_health = player_health-enemy_attack
            heal_player = player_health + random.randint(10,25)
            
            if heal_player <= 100:
                player_health = heal_player

            elif heal_player >100:
                print("Heal Overshoots !! Setting to 100")
                player_health = 100

        print(f"\nPlayer health now: {player_health} :: Enemy health now: {enemy_health}\n")
        

        if player_move not in ["attack", "defend", "heal"]:

            print('\nPlease enter valid player moves!!!\n')
            continue
        
    return player_health, enemy_health



pl_health, en_health = game_start()

print(f"\nPlayer health: {pl_health} :: Enemy health:{en_health} \n")

if pl_health >0:

    print("You Won the game")

else:
    print("You Lost the game")