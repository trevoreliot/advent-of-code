# Trying to unlock the safe without help from AI
# Lessons learned:
# - Modulo operator evaluations negative to positive absolute value
# - Even though our range is from 0-99 we still need to modulo by 100
#
start_position = 50
zero_counter = 0
total_clicks = 0
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

    total_clicks = 0
    raw_position = current_position + dial_input

    if dial_input > 0: # Clockwise
        total_clicks = (current_position + dial_input) // number_of_steps - current_position // number_of_steps
    elif dial_input < 0: # Counter-clockwise
        total_clicks = (-(current_position + dial_input)) // number_of_steps - (-current_position) // number_of_steps
    
    new_position = (raw_position % number_of_steps)

    ##TODO: add counter for all the times the dial traverses 0 or 99 (probably // operator)
    return new_position, raw_position, total_clicks

print_line = 0
for entry in puzzle_entry:
    entry = entry.rstrip()
    dial_input = convert_input(entry)
    prev_pos_debug = current_position
    current_position, raw_position, total_clicks = calc_dial_spin(current_position, dial_input)

    #debug
    print(str(print_line) + ' / ' +
          str(entry) + ' / ' +
          str(prev_pos_debug) + ' / ' +
          str(dial_input) + ' / ' +
          str(raw_position)+ ' / ' +
          str(total_clicks) + ' / ' +
          str(current_position))
    print_line += 1
    #end debug
    
    zero_counter = zero_counter + total_clicks

print(f"There are {zero_counter} zero-values")

