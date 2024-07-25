basic.forever(function on_forever() {
    
})
let Player = game.createSprite(2, 4)
// Random =  randint(0, 4) - לשים בפונקציה של יצירת בלוק נופל
// Block = game.create_sprite(Random, 0) - לשים בפונקציה של יצירת בלוק נופל
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Player.move(-1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    Player.move(1)
})
