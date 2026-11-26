
def calculate_fine(days, book_type="standard", premium=False):
    fine = 0

    if book_type == "standard":
        if days <= 5:
            fine = days * 5
        else:
            fine = 25 + (days - 5) * 10

    elif book_type == "reference":
        fine = days * 20

    else:
        return "Invalid book type"

    if premium:
        fine = fine * 0.80

    return fine


# Test cases
print("Test 1:", calculate_fine(3))
print("Test 2:", calculate_fine(8))
print("Test 3:", calculate_fine(4, "reference"))
print("Test 4:", calculate_fine(8, "standard", True))
print("Test 5:", calculate_fine(5, "reference", True))
print("Test 6:", calculate_fine(10, "reference", False))
