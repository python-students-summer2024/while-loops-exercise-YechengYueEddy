def get_starting_number():
    valid_response = False
    while not valid_response:
        user_input = input("How many bottles of beer on the wall? ")
        if user_input.isdigit() and int(user_input) >= 1:
            valid_response = True
            user_input = int(user_input)
    return user_input

def sing(num_of_bottles):
    round = 0
    while round < num_of_bottles:
        current_bottles = num_of_bottles - round
        next_rounds_bottles = current_bottles - 1
        if current_bottles == 1:
            print(f"{num_of_bottles - round} bottle of beer on the wall, {num_of_bottles - round} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            print(f"{num_of_bottles - round} bottles of beer on the wall, {num_of_bottles - round} bottles of beer.")
            if next_rounds_bottles == 1:
                print(f"Take one down, pass it around, {num_of_bottles - round - 1} bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {num_of_bottles - round - 1} bottles of beer on the wall.\n")
        round += 1    