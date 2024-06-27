#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Sally', 7)
cat2 = Cat('Tom', 5)
cat3 = Cat('Thomas', 9)


# 2 Create a function that finds the oldest cat
def oldest():
        if cat1.age > cat2.age and cat1.age > cat3.age:
            print(f'The oldest cat is {cat1.age} years old')
        elif cat2.age > cat1.age and cat2.age > cat3.age:
            print(f'The oldest cat is {cat2.age} years old')
        elif cat3.age > cat1.age and cat3.age > cat2.age:
            print(f'The oldest cat is {cat3.age} years old')


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(oldest())

# FAILED