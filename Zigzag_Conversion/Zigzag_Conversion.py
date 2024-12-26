def convert(s, numRows):
    # If numRows is 1 or the string is shorter than numRows, return the string
    if numRows == 1 or len(s) <= numRows:
        return s
    
    # rows is a list of strings, one for each
    rows = [''] * numRows
    
    # current_row is the index of the current row, direction is the direction of the next row +1 or -1 for up or down
    current_row = 0
    direction = 1 

    # For each character in the string, add it to the current row and update the current row and direction
    for char in s:
        rows[current_row] += char
        
        # If the current row is at the top or bottom, change the direction
        if current_row == 0:
            direction = 1
        elif current_row == numRows - 1:
            direction = -1
        
        # Update the current row
        current_row += direction
    
    # Join the rows into a single string and return it
    return ''.join(rows)

