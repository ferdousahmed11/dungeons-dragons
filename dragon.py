import random

def roll_dice(sides):
    return random.randint(1, sides)

def create_character():
    character = {}
    character['name'] = input("Enter your character's name: ")
    character['class'] = input("Enter your character's class: ")
    character['level'] = 1
    character['experience'] = 0
    character['hit_points'] = roll_dice(10) + 10
    character['gold'] = 100
    return character

def print_character(character):
    print("Character Information:")
    print("Name:", character['name'])
    print("Class:", character['class'])
    print("Level:", character['level'])
    print("Experience:", character['experience'])
    print("Hit Points:", character['hit_points'])
    print("Gold:", character['gold'])

def encounter_enemy(character):
    enemy_hit_points = roll_dice(10) + 5
    print("You encountered an enemy!")
    while character['hit_points'] > 0 and enemy_hit_points > 0:
        print("Your HP:", character['hit_points'])
        print("Enemy HP:", enemy_hit_points)
        action = input("Enter your action (1. Attack, 2. Flee): ")
        if action == '1':
            character_attack = roll_dice(6) + character['level']
            enemy_attack = roll_dice(6)
            if character_attack >= enemy_attack:
                enemy_hit_points -= character_attack
                print("You dealt", character_attack, "damage to the enemy!")
            else:
                character['hit_points'] -= enemy_attack
                print("The enemy dealt", enemy_attack, "damage to you!")
        elif action == '2':
            print("You fled from the battle!")
            return
        else:
            print("Invalid action. Try again.")

    if character['hit_points'] > 0:
        print("Congratulations! You defeated the enemy!")
        character['experience'] += 10
        character['gold'] += 50
        if character['experience'] >= character['level'] * 100:
            character['level'] += 1
            character['experience'] = 0
            print("Level up! You are now level", character['level'])
    else:
        print("Game Over! You were defeated by the enemy.")

def main():
    print("Welcome to Dungeons & Dragons!")
    character = create_character()
    print_character(character)
    play_again = 'yes'
    while play_again.lower() == 'yes':
        encounter_enemy(character)
        print_character(character)
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thank you for playing Dungeons & Dragons!")

if __name__ == "__main__":
    main()
