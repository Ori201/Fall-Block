basic.forever(function on_forever() {
    let speed = 1 * 1000
    fallLed(1000)
})
let Player = game.createSprite(2, 4)
function fallLed(speed: number) {
    let Random = randint(0, 4)
    let Block = game.createSprite(Random, 0)
    let i = 0
    while (i == 4) {
        Block.turn(Direction.Left, 180)
        Block.move(1)
        basic.pause(speed)
    }
    Block.turn(Direction.Left, 180)
    Block.move(1)
    basic.pause(99999999999)
    Block.delete()
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Player.move(-1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    Player.move(1)
})
