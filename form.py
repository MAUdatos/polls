import csv
 
Nombre = "An"
Nota = None

fields = [Nombre, Nota]
 
with open('data.csv','a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
