let I = 0
let A = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Welcome ")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    I = 90
    if ((1 as any) <= (90 as any)) {
        basic.showString("Excellent ")
    } else if ((1 as any) <= (50 as any)) {
        basic.showString("Pass")
    } else {
        basic.showString("Fail")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    A = 1
    basic.showNumber(3)
    A += 5
    basic.showNumber(0)
})
