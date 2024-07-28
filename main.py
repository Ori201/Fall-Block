def on_forever():
    speed = 1 * 1000
    fallLed(1000)
basic.forever(on_forever)

Player = game.create_sprite(2, 4)

def fallLed(speed):
    Random =  randint(0, 4)
    Block = game.create_sprite(Random, 0)

    i = 0
    while i == 4:
        Block.turn(Direction.LEFT, 180)
        Block.move(1)
        basic.pause(speed)

    Block.turn(Direction.LEFT, 180)
    Block.move(1)
    basic.pause(99999999999)
    Block.delete()



def on_button_pressed_a():
    Player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)