def on_forever():
    pass
basic.forever(on_forever)

Player = game.create_sprite(2, 4)
#Random =  randint(0, 4) - לשים בפונקציה של יצירת בלוק נופל
#Block = game.create_sprite(Random, 0) - לשים בפונקציה של יצירת בלוק נופל

def on_button_pressed_a():
    Player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)