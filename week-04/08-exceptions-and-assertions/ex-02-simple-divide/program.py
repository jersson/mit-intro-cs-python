def simple_divide(item, denom):
   result = 0
   try:
       result = item / denom
   except ZeroDivisionError:
       result = 0
   return result

print(simple_divide(4, 2))
print(simple_divide(4, 0))