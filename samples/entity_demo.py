from ursina import *
import csv
from ursina.shaders import lit_with_shadows_shader # you have to apply this shader to enties for them to recieve shadows.

app = Ursina()

title = Text('''position, rotation, scale and parenting demo''', position=(-.85, .475), scale=1.5)
window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counte
    
entity = Entity(model='cube', texture='white_cube')
child = Entity(parent=entity, x=1, model='cube', scale=.5, texture='white_cube', color=color.azure)
spacing = .04
ui_parent = Entity(parent=camera.ui, scale=.8, x=-.85)

PointLight(x=0, y=0, z=50, shadows=True)

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
            e= Entity(parent=entity, model='sphere',color=color.rgb(100, 50, int(abs(float(row[2])*10000))), shader=lit_with_shadows_shader, scale=1)
            e.x = float(row[0])*1
            e.y = float(row[1])*1
            e.z = float(row[2])*100
    print(f'Processed {line_count} lines.')



for y, e in enumerate((entity, child)):
    for i, name in enumerate(('x', 'y', 'z')):
        slider = Slider(-1, 1, default=getattr(e, name), text=name, dynamic=True, position=(.1, .4-(i*spacing)-y*.5), parent=ui_parent)
        def on_slider_changed(e=e, slider=slider, attr_name=name):
            setattr(e, attr_name, slider.value)
        slider.on_value_changed = on_slider_changed

        name = 'rotation_' + name
        slider = Slider(0, 360, default=getattr(e, name), text=name, dynamic=True, position=(.1, .4-(i*spacing)-(spacing*3)-y*.5), parent=ui_parent)
        def on_slider_changed(e=e, slider=slider, attr_name=name):
            setattr(e, attr_name, slider.value)
        slider.on_value_changed = on_slider_changed

        name = 'scale_' + name.split('_')[1]
        slider = Slider(.1, 3, default=getattr(e, name), text=name, dynamic=True, position=(.1, .4-(i*spacing)-(spacing*6)-y*.5), parent=ui_parent)
        def on_slider_changed(e=e, slider=slider, attr_name=name):
            setattr(e, attr_name, slider.value)
        slider.on_value_changed = on_slider_changed

t = Text('''white cube:''', position=(0, .4+spacing*1.5), parent=ui_parent)
t.create_background(.025, 0.0125)
t = Text('''blue cube (parented to the white cube):''', position=(0, -spacing), parent=ui_parent)
t.create_background(.025, 0.0125)

EditorCamera()

app.run()
