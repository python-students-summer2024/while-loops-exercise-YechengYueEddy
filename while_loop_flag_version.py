def get_starting_number():
    valid_response = False
    while not valid_response:
        user_input = input("How many bottles of beer on the wall? ")
        if user_input.isdigit() and int(user_input) >= 1:
            valid_response = True
            user_input = int(user_input)
    return user_input

def sing(num_of_bottles):
    last_round = False
    while not last_round:
        if num_of_bottles == 1:
            print(f"{num_of_bottles} bottle of beer on the wall, {num_of_bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            last_round = True
        else:
            print(f"{num_of_bottles} bottles of beer on the wall, {num_of_bottles} bottles of beer.")
            if num_of_bottles - 1 == 1:
                print(f"Take one down, pass it around, {num_of_bottles - 1} bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {num_of_bottles - 1} bottles of beer on the wall.\n")
        num_of_bottles -= 1