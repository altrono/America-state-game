import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "states.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

state_name = turtle.textinput(title='Guess the State', prompt='What\'s another state\'s name?')
state_name.penup()
state_name.goto(-275, 240)
print(state_name)

turtle.mainloop()
