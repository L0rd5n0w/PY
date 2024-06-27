class SuperList(list):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        return 1000
    
sup1 = SuperList('kunle', 20)
print(len(sup1))
sup1.append(1)
print(sup1)

# PASSED