import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
image = "states.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv('50_states.csv')
all_states = data['state'].tolist()
guessed_states = []

while len(guessed_states) < 50:
    state_name = screen.textinput(title=f"{len(guessed_states)}/50 State Correct", prompt='What\'s another state\'s name?').title()
    if state_name in all_states:
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == state_name]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(state_name)
        guessed_states.append(state_name)


turtle.mainloop()
