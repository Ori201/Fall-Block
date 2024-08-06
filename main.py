TimeGame = 0
def on_forever():
    OLED.write_num_new_line(1)
    TimeGame + 1
    if TimeGame < 10:
        fallLed(1000)
    elif TimeGame < 30:
        fallLed(600)
basic.forever(on_forever)

Player = game.create_sprite(2, 4)

def fallLed(speed):
    Random =  randint(0, 4)
    Block = game.create_sprite(Random, 0)
    Block.set_direction(0)

    i = 0
    while i < 4:
        basic.pause(speed)
        Block.move(-1)
        i += 1

    basic.pause(speed)
    i = 0
    Block.delete()



def on_button_pressed_a():
    Player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)