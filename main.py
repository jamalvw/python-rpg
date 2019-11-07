import vars
import entities
import items
import random

def start_game():
    vars.player = entities.Player("Player", 100, 10, [items.Potion(100), items.Potion(100)])
    vars.enemy = generate_enemy()

    goto_menu(menu_name_update)

    while vars.player.health > 0:
        goto_menu(menu_battle)

    print("You died!")

# Generates a new random enemy.
def generate_enemy() -> entities.Entity:
    return entities.Entity(random.choice(['Elf', 'Goblin', 'Wolf', 'Beast', 'Skeleton']), random.randint(20, 70), random.randint(2, 10))

# Opens a new menu and clears menu info vars.
def goto_menu(menu):
    if vars.current_menu != menu:
        vars.current_menu = menu
        vars.display = False
        vars.instruct = False
    menu()

def menu_win():
    print()
    print("You defeated " + vars.enemy.name + "! The next enemy is approaching.")
    # TODO add exp
    print("Experience gained: 0")
    # TODO add loot table
    print("Items looted: Nothing")
    print("Press enter to continue.")
    input()
    vars.enemy = generate_enemy()
    goto_menu(menu_battle)

def menu_battle():
    if not vars.display:
        vars.display = True
        print(vars.enemy.name + ": " + str(vars.enemy.health))
        print(vars.player.name + ": " + str(vars.player.health))
    if not vars.instruct:
        vars.instruct = True
        print("Type 'a' to attack.")
        print("Type 'i' to use items.")
        print("Type 's' to change settings.")

    action = input().lower()
    if action == 'a':
        # TODO create damage function
        vars.display = False
        vars.enemy.health -= vars.player.damage
        print(vars.player.name + " dealt " + str(vars.player.damage) + " damage.")
        if vars.enemy.health > 0:
            vars.player.health -= vars.enemy.damage
            print(vars.enemy.name + " dealt " + str(vars.enemy.damage) + " damage.")
        else:
            goto_menu(menu_win)
    elif action == 'i':
        if not vars.player.items:
            print("You do not have any items.")
        else:
            goto_menu(menu_items)
    elif action == 's':
        goto_menu(menu_settings)

def menu_items():
    if not vars.display:
        vars.display = True
        print("Items: " + ', '.join([item.name for item in vars.player.items]))
    if not vars.instruct:
        vars.instruct = True
        print("Enter the name of the item to use it.")
        print("Type 'b` to go back.")

    action = input().lower()
    if action == 'b':
        pass
    else:
        # Try to find item by name
        for item in vars.player.items:
            if action == item.name.lower():
                # Use then remove the item
                vars.display = False
                vars.player.items.remove(item)
                print("You used a(n) " + item.name + ".")
                print(item.use(vars.player))
                break
        if vars.player.items:
            goto_menu(menu_items)

def menu_settings():
    if not vars.instruct:
        vars.instruct = True
        print("Type 'c' to change your name.")
        print("Type 'b' to go back.")

    action = input().lower()
    if action == "c":
        goto_menu(menu_name_update)
    elif action == 'b':
        pass
    else:
        goto_menu(menu_settings)

def menu_name_update():
    vars.player.name = input("Enter a name for yourself: ")


start_game()
