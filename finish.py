#To start the sim run the file
#The terminal will open then
#type "boot drawing sim"
#Then the sim will open
#And then you can draw with turtle
#for keybinds open the keybinds.txt file
#After you downloaded it in the webpage if needed

import time

def Program():
    import turtle
    wn = turtle.Screen()
    wn.bgcolor('black')

    t = turtle.Turtle()
    t.color('white')

    def w_keypress():
        t.forward(10)
    def a_keypress():
        t.left(45)
    def s_keypress():
        t.backward(10)
    def d_keypress():
        t.right(45)
    def z_fill():
        t.begin_fill()
    def x_fill():
        t.end_fill()
    def e_penup():
        t.penup()
    def r_pendown():
        t.pendown()

    wn.onkeypress(w_keypress, 'w')
    wn.onkeypress(a_keypress, 'a')
    wn.onkeypress(s_keypress, 's')
    wn.onkeypress(d_keypress, 'd')
    wn.onkeypress(z_fill, 'z')
    wn.onkeypress(x_fill, 'x')
    wn.onkeypress(e_penup, 'e')
    wn.onkeypress(r_pendown, 'r')
    wn.listen()

    turtle.done()

print('Terminal Booting')
time.sleep(1.25)
print('Terminal Booted')
time.sleep(0.5)

q_sim = print('C:\Terminal\Input')

cmd_start = {'boot drawing simulator', 'boot drawing sim', 'bt drawing sim', 'bt drawing simulator'}
cancel = {'cancel', 'close'}

q_sim = input().lower()

if q_sim in cmd_start:
    time.sleep(0.5)
    print('Simulator booting')
    time.sleep(2)
    print('Simulator booted')
    Program()
elif q_sim in cancel:
    time.sleep(0.5)
    print('Terminal Closing')
    time.sleep(1.25)
    print('Terminal Closed')
else:
    print('Error')
    time.sleep(0.5)
    print('command not found')
    time.sleep(0.75)
    print('Terminal Closing')
    time.sleep(1.25)
    print('Terminal Closed')