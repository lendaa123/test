I = 0
A = 0

def on_button_pressed_a():
    basic.show_string("Welcome ")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global I
    I = 90
    if (1) <= (90):
        basic.show_string("Excellent ")
    elif (1) <= (50):
        basic.show_string("Pass")
    else:
        basic.show_string("Fail")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global A
    A = 1
    basic.show_number(3)
    A += 5
    basic.show_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)
