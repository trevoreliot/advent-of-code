# This was easy but I have a feeling part 2 will punish me for not being more clever

puzzle_input = []
with open('../puzzle-input.txt', 'r') as file:
    puzzle_string = file.read()
    puzzle_rows = puzzle_string.split(',')


puzzle_input_expanded = []
puzzle_solution = 0

for row in puzzle_rows:
    range_ends = row.split('-')
    range_min = int(range_ends[0])
    range_max = int(range_ends[1])
    range_full = range(range_min, range_max+1)
    
    for num in range_full:
        puzzle_input_expanded.append(num)

for row_num in puzzle_input_expanded:
    product_id = str(row_num)
    if len(product_id) % 2 != 0:
        continue
    halfway_mark = len(product_id) // 2
 #   print (product_id, halfway_mark)
    if product_id[:halfway_mark] == product_id[-halfway_mark:]:
        #print(product_id, ' true!')
        puzzle_solution += int(product_id)

print(puzzle_solution)
