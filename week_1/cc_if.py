def grade_conversion(grade_to_test):
    """
    This function converts numerical grades to letter grades based on predefined ranges.

    Args:
    grade_to_test (int): The numerical grade to be converted.

    Returns:
    str: The corresponding letter grade.
    """
    # Check if the grade is 100
    if grade_to_test == 100:
        return "A+"  # If true, return "A+"
    
    # Check if the grade is between 90 and 99 (inclusive)
    elif grade_to_test >= 90:
        return "A"  # If true, return "A"
    
    # Check if the grade is between 80 and 89 (inclusive)
    elif grade_to_test >= 80:
        return "B"  # If true, return "B"
    
    # Check if the grade is between 70 and 79 (inclusive)
    elif grade_to_test >= 70:
        return "C"  # If true, return "C"
    
    # Check if the grade is between 50 and 69 (inclusive)
    elif grade_to_test >= 50:
        return "D"  # If true, return "D"
    
    # If none of the above conditions are met, assume the grade is less than 50
    else:
        return "F"  # Return "F"

# Test the function with the given grade
grade_to_test = 100
print(grade_conversion(grade_to_test))
