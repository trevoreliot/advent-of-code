# Trying to unlock the safe without help from AI
# Lessons learned:
# - Modulo operator evaluations negative to positive absolute value
# - Even though our range is from 0-99 we still need to modulo by 100
#
start_position = 50
zero_counter = 0
dial_min = 0
dial_max = 99
number_of_steps = 100

puzzle_entry_loc = '../puzzle-input.txt'
puzzle_entry = []

with open(puzzle_entry_loc, 'r') as file:
    puzzle_entry = file.readlines()

current_position = start_position

def convert_input(inputs: str):

    inputs = inputs.upper()
    inputs = int(inputs.replace('L', '-').replace('R','+'))

    return inputs

def calc_dial_spin(current_position = 50,
                   dial_input = 0,
                   dial_min = dial_min,
                   dial_max = dial_max) -> int:

    if dial_input == 0:
        return current_position

    dial_modifier = 1
    if dial_input < 0:
        dial_modifier = 0
    
    raw_position = current_position + dial_input

    if raw_position >= dial_min and raw_position <= dial_max:
        current_position = raw_position
    else:
        current_position = (raw_position % number_of_steps)

    return current_position, raw_position

print_line = 0
for entry in puzzle_entry:
    entry = entry.rstrip()
    dial_input = convert_input(entry)
    prev_pos_debug = current_position
    current_position, raw_position = calc_dial_spin(current_position, dial_input)

    #debug
    print(str(print_line) + ' / ' +
          str(entry) + ' / ' +
          str(prev_pos_debug) + ' / ' +
          str(dial_input) + ' / ' +
          str(raw_position)+ ' / ' +
          str(current_position))
    print_line += 1
    #end debug
    
    if current_position == 0:
        zero_counter += 1

print(f"There are {zero_counter} zero-values")

