windSpeed = input("Enter the average windspeed here in m/s")
operatingEfficiency = input("Enter the operating efficiency here")
radius = input("Enter the blade radius here")
area = 3.14159 * float(radius) * float(radius)
density = 1.2
pmax = 0.5 * float(windSpeed) * float(windSpeed) * float(windSpeed) * float(area) * float(density)
print(pmax)
pact = pmax * float(operatingEfficiency)
print(pact)
numberTurbines = 2.57E10 / pact
print(numberTurbines)