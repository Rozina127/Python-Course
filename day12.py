################### Scope ####################

enemies = 1

def increase_enemies():
    #enemy has local scope in side if a variake has defined in a function it has local scope it we cqallitoutside the function it give us different output 
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#**********block scope ****************#

"""if (true) {
    let x = 10;
    console.log(x);  // Accessible here
}
console.log(x);  // Not accessible here (ReferenceError)"""


#*************** local scope ***************#

"""def my_function():
    y = 20  # Local scope
    print(y)  # Accessible here

my_function()
print(y)  # Not accessible here (NameError)"""


#*************** global scope ***************#

"""x = "global"

def outer_function():
    x = "enclosing"
    
    def inner_function():
        x = "local"
        print(x)  # Prints "local"
    
    inner_function()
    print(x)  # Prints "enclosing"

outer_function()
print(x)  # Prints "global" """

################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159




