def on_forever():
    if AlphaBot2.ultrasonic() > 15:
        AlphaBot2.run(Dir.FORWARD, 80)
    else:
        AlphaBot2.run(Dir.TURN_RIGHT, 20)
    basic.pause(500)
basic.forever(on_forever)
