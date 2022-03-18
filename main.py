import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        t.goto(x_cor, y_cor)
        t.write(answer_state)
    elif answer_state == "Exit":
        missed_states = []
        for states in all_states:
            if states not in guessed_states:
                missed_states.append(states)
                new_data = pandas.DataFrame(missed_states)
                new_data.to_csv("states_to_learn.csv")
        break
