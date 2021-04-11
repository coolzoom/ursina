from ursina import *
import csv
from ursina.shaders import lit_with_shadows_shader # you have to apply this shader to enties for them to recieve shadows.
app = Ursina()
EditorCamera()
Entity(model='plane', scale=10, color=color.gray, shader=lit_with_shadows_shader)
Entity(model='cube', y=1, shader=lit_with_shadows_shader)
pivot = Entity()
PointLight(parent=pivot, x=0, y=0, z=50, shadows=True)
#AmbientLight(parent=pivot, y=2, z=50, shadows=True)

with open('C:\\Users\\Administrator\\Desktop\\data2.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
            e= Entity(parent=pivot, model='sphere',color=color.rgb(100, 50, int(abs(float(row[2])*10000))), scale=1)
            e.x = float(row[0])*1
            e.y = float(row[1])*1
            e.z = float(row[2])*100
    print(f'Processed {line_count} lines.')
    
app.run()
