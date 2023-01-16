import rotatescreen

screen = rotatescreen.get_primary_display()
for i in range(5):
   screen.rotate_to(i*90%360)