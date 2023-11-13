let ran = 0
input.onButtonPressed(Button.A, function () {
    basic.showString("pedra")
})
input.onGesture(Gesture.Shake, function () {
    ran = randint(0, 2)
    if (ran == 0) {
        basic.showString("pedra")
    }
    if (ran == 1) {
        basic.showString("paper")
    }
    if (ran == 2) {
        basic.showString("tisores")
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("tisores")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("paper")
})
