basic.forever(function on_forever() {
    fallLed(1000)
})
let Player = game.createSprite(2, 4)
function fallLed(speed: number) {
    let Random = randint(0, 4)
    let Block = game.createSprite(Random, 0)
    Block.setDirection(0)
    let i = 0
    while (i < 4) {
        basic.pause(speed)
        Block.move(-1)
        i += 1
    }
    basic.pause(speed)
    i = 0
    Block.delete()
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Player.move(-1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    Player.move(1)
})
