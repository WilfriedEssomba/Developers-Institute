
a = int(input("Enter a number between 1 and 12 "))
if 6 <= a <= 8:
    print("Summer")
elif 9 <= a <= 11:
    print("Autumn")
elif 3 <= a <= 5:
    print("Spring")
elif 1 <= a <= 2 or a == 12:
    print("Winter")
