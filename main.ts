let 计数 = 0
input.onButtonPressed(Button.A, function () {
    计数 += 1
})
input.onButtonPressed(Button.B, function () {
    while (计数 != 0) {
        basic.pause(1000)
        music.playTone(988, music.beat(BeatFraction.Eighth))
        计数 += -1
    }
    for (let index = 0; index < 10; index++) {
        basic.showIcon(IconNames.Chessboard)
        basic.showIcon(IconNames.Skull)
        music.playTone(784, music.beat(BeatFraction.Breve))
    }
})
basic.forever(function () {
    if (计数 != 0) {
        basic.showNumber(计数)
    }
})
