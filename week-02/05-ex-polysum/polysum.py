import math
def polysum(n, s):
    # Polysum function has 2 arguments, n(number of sides) and s(length of each side)  
    # This function should sum the area and square of the perimeter of the regular polygon. 
    # The function returns the sum, rounded to 4 decimal places.
    
    area = (0.25 * n * s * s) / math.tan(math.pi / n)
    perimeter = n * s
    result =  area + perimeter * perimeter
    result = round(result, 4)
    return result