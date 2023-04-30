def on_button_pressed_a():
    global 计数
    计数 += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global 计数
    while 计数 != 0:
        basic.pause(1000)
        music.play_tone(988, music.beat(BeatFraction.EIGHTH))
        计数 += -1
    for index in range(10):
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_icon(IconNames.SKULL)
        music.play_tone(784, music.beat(BeatFraction.BREVE))
input.on_button_pressed(Button.B, on_button_pressed_b)

计数 = 0


def on_forever():
    if 计数 != 0:
        basic.show_number(计数)
basic.forever(on_forever)
