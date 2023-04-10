# In this program, we are going to cover conditionals in python!!!!!!!!!!!!!!!!!!!!!!!!!

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters...")
    else:
        print("Your username is valid!!!!")


hint_username("Hey")


def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    if denominator == 0 or denominator == numerator or numerator == 0:
        part = 0
    else:
        part = (numerator % denominator) / denominator
    return part


print(fractional_part(5, 5))  # Should print 0
print(fractional_part(5, 4))  # Should print 0.25
print(fractional_part(5, 3))  # Should print 0.66...
print(fractional_part(5, 2))  # Should print 0.5
print(fractional_part(5, 0))  # Should print 0
print(fractional_part(0, 5))  # Should print 0
