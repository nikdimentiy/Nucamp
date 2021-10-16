# Experiments on String [slices]

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])       # abcdefghijklmnopqrstuvwxyz
print(letters[20:])     # uvwxyz
print(letters[10:])     # klmnopqrstuvwxyz
print(letters[12:15])   # mno
print()
print(letters[-3:])     # xyz
print(letters[18:-3])   # stuvw
print(letters[-6:-2])   # uvwx
print(letters[::7])     # ahov
print()
print(letters[4:20:3])  # ehknqt
print(letters[19::4])   # tx
print(letters[:21:5])   # afkpu
print(letters[-1::-1])  # zyxwvutsrqponmlkjihgfedcba
print()
print(letters[::-1])    # zyxwvutsrqponmlkjihgfedcba
print(letters[-50:])    # abcdefghijklmnopqrstuvwxyz'
print(letters[-51:-50]) # ' '
print(letters[:70])     # abcdefghijklmnopqrstuvwxyz
print(letters[70:71])   # ' '
