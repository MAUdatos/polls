import csv
 
st.text_input('Nomnbre',nombre, 'Nota', nota)
fields = [nombre, nota]
with open('data.csv','a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
