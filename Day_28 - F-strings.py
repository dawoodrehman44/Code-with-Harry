letter = "Hey my name is {} and i am from {}"
name = "Dawood"
country = "Pak"

print(f"hey i am from {country} and i am {name}")

print(letter.format(country, name))

price = 49.699999
txt = f"For only {price : .2f} doolors"
print(txt)