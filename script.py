#!/usr/bin/env python3

"""
Author: Prakash Gautam
This script prompts the user for numbers, calculates the average, 
and ignores invalid inputs. The loop continues until the user 
presses Enter without entering a number.
"""

# Step 1: Initialize variables to store total sum and count of numbers
total = 0
count = 0

# Step 2: Start an infinite loop to get user input
while True:
    # Step 3: Ask the user to enter a number
    user_input = input("Enter a number (or press Enter to finish): ").strip()
    
    # Step 4: If the user presses Enter without typing anything, stop the loop
    if user_input == "":
        break
    
    # Step 5: Check if the input is a valid number using isnumeric()
    if user_input.isnumeric():
        total += int(user_input)  # Convert to integer and add to total
        count += 1  # Increase the count

# Step 6: Calculate and display the average, if at least one valid number was entered
if count > 0:
    average = total / count  # Calculate average
    print(f"Average: {average:.2f}")  # Print average with 2 decimal places
else:
    print("No valid numbers were entered.")  # If no numbers, print a message
