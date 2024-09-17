def calculate_total_distance(good_string, name):
    good_chars = list(good_string)
    prev_good_char = good_chars[0]  # Initially, the first good character
    total_distance = 0
    
    for char in name:
        if char in good_chars:
            prev_good_char = char
            continue
        
        # Find the nearest good character to 'char'
        nearest_char = None
        min_distance = float('inf')
        
        for good_char in good_chars:
            current_distance = abs(ord(char) - ord(good_char))
            
            if current_distance < min_distance:
                min_distance = current_distance
                nearest_char = good_char
            elif current_distance == min_distance:
                # If tied, use the good letter closest to the previous good letter
                if abs(ord(prev_good_char) - ord(good_char)) < abs(ord(prev_good_char) - ord(nearest_char)):
                    nearest_char = good_char
        
        total_distance += abs(ord(char) - ord(nearest_char))
        prev_good_char = nearest_char  # Update previous good character to the selected one
    
    return total_distance

# Input reading
good_string = input().strip()  # Good string
name = input().strip()  # Student's name

# Calculate and print the total distance
result = calculate_total_distance(good_string, name)
print(result)
