from functools import reduce


def check_arguments(*args):
    return(f"These are the arguments {args}")
print(check_arguments('hello', 'hey'))
def salut(*args):
    print(f"{args} bro my name is {args}")
salut("bonjour","Essomba")

def  check_keywordedarguments(**kwargs):
    print(kwargs)

check_keywordedarguments(name="Sarah", age=24)

def check_arguments_keywordedarguments (required_arg,*args, **kwargs):
    print(required_arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

check_arguments_keywordedarguments("required argument")
check_arguments_keywordedarguments("required argument", 1, 2, 'hey')
check_arguments_keywordedarguments("required argument", 1, 2, 'hey', name="Sarah", age=24)

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))

def sum_numbers(first, second):
    return first+second

my_list = [1, 3, 5, 7]
reduced_list = reduce(sum_numbers, my_list)

print(reduced_list)