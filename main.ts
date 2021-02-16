basic.forever(function () {
    if (AlphaBot2.Ultrasonic() > 15) {
        AlphaBot2.Run(Dir.forward, 80)
    } else {
        AlphaBot2.Run(Dir.turnRight, 30)
    }
    basic.pause(500)
})
