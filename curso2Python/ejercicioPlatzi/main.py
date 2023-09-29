import csv

def read_csv(path):
#Tucodigo aquí:
    total = 0
    with open(path, "r") as csvFile:
        reader = csv.reader(csvFile)
        for data in reader:
            total += int(data[1])
    return total

response = read_csv('./ejercicioPlatzi/data.csv')
print(response)