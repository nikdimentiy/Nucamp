def print_total_snowfall(inches_snow):
    """
    Prints the total snowfall in inches for the given days.

    Args:
    - inches_snow (dict): A dictionary where keys are days of the week and values are inches of snowfall.

    Returns:
    - None
    """
    total_inches = 0  # Initialize the total snowfall counter

    for inches in inches_snow.values():  # Iterate through the values in the dictionary
        total_inches += inches  # Add the inches of snowfall to the total counter

    print("Total snowfall inches:", total_inches)  # Print the total snowfall

# Sample data of snowfall for the first three days of the week
inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

# Call the function with the provided data
print_total_snowfall(inches_snow)

# Ask the user for the snowfall on Thursday and update the data
inches_snow["Thursday"] = int(input("How many inches of snow fell on Thursday? "))

# Call the function again with the updated data
print_total_snowfall(inches_snow)
