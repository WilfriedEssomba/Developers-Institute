# Exercise 1
def display_message():
    print("In this course i learn how to use functions in python")


display_message()


# Exercise 2
def favorite_book(title):
    print("One of my favorite book is " + title)


favorite_book("Noblesse")


# Exercise 3
def describe_city(city, country="Cameroon"):
    print(city + " is in " + country)


describe_city("Buea")


# Exercise 4
def random(a):
    b = int(input('Enter a number'))
    if b == a:
        print("Good job bro")
    else:
        print(a, b)


random(2)


# Exercise 5
def make_shirt(size="l", text="i love Python"):
    print("the size of my shirt " + size + " and the text is " + text)


make_shirt()
make_shirt("m")
make_shirt("s", "I love myself")

# Exercise 6

# Exercise 7
def get_random_temp(celsius) :
    return celsius
get_random_temp(20)