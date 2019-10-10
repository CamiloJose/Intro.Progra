import csv


#   Leer el archvio

##with open('Tabla de Productos1.csv',"r", newline='') as f:
##    reader = csv.reader(f)
##    for row in reader:
##        print(row)




#   Editar el archivo

with open("Tabla de Productos 2.csv", "w", newline= "") as f:
    field_names = ["Codigo", "Descripcion", "Existencia","Maximo","Costo","Precio","Venta","Imagen"]
    thewriter = csv.DictWriter(f, fieldnames=field_names)

    thewriter.writeheader()
    thewriter.writerow({"Codigo":"55","Descripcion":"", "Existencia":"55", "Maximo": "60","Costo":"55000", "Precio":"75000", "Venta":"20000","Imagen":""})
    thewriter.writerow({"Codigo":"04","Descripcion":"", "Existencia":"10", "Maximo": "15","Costo":"2525", "Precio":"4550", "Venta":"254540","Imagen":""})

#   Leer el archivo

with open("Tabla de Productos1.csv") as csv_file:
    
    reader = csv.DictReader(csv_file)

    objeto_precio = []

    objeto_cantidad = []

    for row in reader:
        objeto_precio.append(row["Descripcion"])

        objeto_precio.append(row["Precio"])

    #print (objeto_precio)


# -----------------------------
def readcsv():
    global scores
    scores = []
    with open('scores.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            scores += [row]
    
    csvFile.close()
# ---------------------------------

with open("Tabla de Productos1.csv", "r")as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("NUEVA Tabla de Productos1.csv", "w") as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        
        for row in csv_file:
            csv_writer.writerow(row)


with open("Tabla de Productos1.csv", "r")as csv_file:
    csv_reader = csv.DictReader(csv_file)

# -------------------------------

#Crear archivo en lista y luego pasarlo a csv

mydict = [{"Passenger":"1", "ID":"o-559", "Survived":"No"},
          {"Passenger":"2", "ID":"C-356", "Survived":"Yes"},
          {"Passenger":"2", "ID":"A-809", "Survived":"No"}]

fields = ["Passenger", "ID", "Survived"]

filename = "NUEVA Tabla de Productos1.csv"

with open("NUEVA Tabla de Productos1.csv", "w") as New_csv_file:

    writer = csv.DictWriter(New_csv_file, fieldnames = fields, delimiter=',')

    writer.writeheader()

    writer.writerows(mydict)





    
