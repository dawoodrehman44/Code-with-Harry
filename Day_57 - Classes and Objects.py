class Person:
    name = "Dawood Rehman"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Dawood Rehman"
a.occupation = "AI Engineer"

b = Person()
b.name = "Amjad"
b.occupation = "Civil Engineer"
a.info()
b.info()