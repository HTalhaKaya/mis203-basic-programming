# Lb 02 - Purchase Quote

### Test Run
-Tested with: 2x50, 1x80, delivery 20, tax 10%
-Result: Total caME OUT TO 218.00 exactly as expexted.

### Notes & Changes
- Initial test didn't separate tax from delivery; fixed order of operations to apply tax only to item subtotal before adding delivery fee.
- -**Why input() must be converted:** 'input()' returns data as a string. In order to do mathematical operations, value must be explicitly  cast to 'int' or 'float'.
- -**Stretch Task :** Entering non-numeric string into 'int()' causes a 'ValueError'. In feature versions, this can be handled us,ng 'try-except' blocks or '.isdigit()' validation in a 'while' loop.
