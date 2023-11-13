def on_button_pressed_a():
    global timeA
    timeA = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def move():
    pass
timeA = 0
wait = 1

def on_forever():
    move()
basic.forever(on_forever)

def on_in_background():
    global timeA
    while True:
        control.wait_micros(0)
        timeA += 1
        basic.show_string("" + str((timeA)))
control.in_background(on_in_background)

def on_every_interval():
    if wait == 0:
        pass
    else:
        pass
loops.every_interval(100, on_every_interval)
