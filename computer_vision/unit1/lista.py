cars = ["bmw","bocho"]
price = [1 ,5]
print(cars)
print(cars[0])

print(f"Mi primer carro fue un {cars[0]}")
for car in cars:
    print(f"Mi primer carro fue un {car}") # varible string pq es texto

for ind, value in enumarate(cars):
    print(ind, value)

for car, price in zip(cars,prices):
    print(car,prices)