# Binary to Decimal Converter

from convert import converter

print('Binary to Decimal Converter')

while True:
    initial = input('Binary number ("e" to exit): ')
    if initial == "e":
        print("Closing program")
        exit(0)
    else:
        converter(initial)
