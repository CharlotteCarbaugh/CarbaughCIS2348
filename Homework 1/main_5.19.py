#Charlotte Carbaugh, Student ID 1815532

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 'No service'}

print("Davy's auto shop services")
print("Oil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

service_1 = str(input("Select first service:\n"))
service_2 = str(input("Select second service:\n"))

print("\nDavy's auto shop invoice\n")
if service_1 == '-':
    print("Service 1:", services[service_1])
else:
    print("Service 1:", service_1 + ", $" + str(services[service_1]))
if service_2 == '-':
    print("Service 2:", services[service_2] + '\n')
else:
    print("Service 2:", service_2 + ", $" + str(services[service_2]) + "\n")

if (service_1 == '-') and (service_2 == '-' ):
    invoice  = 0
elif service_2 == '-':
    invoice = services[service_1]
elif service_1 == '-':
    invoice = services[service_2]
else:
    invoice = services[service_1] + services[service_2]


print("Total: $"+str(invoice))