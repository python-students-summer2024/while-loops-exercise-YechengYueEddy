def get_starting_number():
    valid_response = False
    while not valid_response:
        user_input = input("How many bottles of beer on the wall? ")
        if user_input.isdigit() and int(user_input) >= 1:
            valid_response = True
            user_input = int(user_input)
    return user_input

def sing(num_of_bottles):
    for round in range(num_of_bottles, 0, -1):
        if round == 1:
            print(f"{round} bottle of beer on the wall, {round} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            print(f"{round} bottles of beer on the wall, {round} bottles of beer.")
            if round - 1 == 1:
                print(f"Take one down, pass it around, {round - 1} bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {round - 1} bottles of beer on the wall.\n")