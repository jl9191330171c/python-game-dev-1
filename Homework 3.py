def group_by_length(words):

    # Initialize an empty dictionary to store our groups
    result = {}

    for word in words:
        # Calculate the length of the current word
        length = len(word)
        
        # If the length is not already a key in the dictionary, 
        # add it with an empty list as the value
        if length not in result:
            result[length] = []
            
        # Append the current word to the list corresponding to its length
        result[length].append(word)
        
    return result

# --- Testing the Mini-Project ---
if __name__ == "__main__":
    # Example input list
    word_list = ["apple", "dog", "cat", "banana", "kiwi", "pear", "egg"]
    
    # Call the function
    grouped_data = group_by_length(word_list)
    
    # Display the results
    print("Grouped Words Dictionary:")
    print(grouped_data)
    
    # Optional: Formatted output for readability
    print("\nBreakdown:")
    for length in sorted(grouped_data.keys()):
        print(f"Length {length}: {grouped_data[length]}")