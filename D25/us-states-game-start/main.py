import turtle
import pandas

FONT = ("Courier", 18, "normal")

screen = turtle.Screen()
image = "./blank_states_img.gif"
screen.addshape(image)
screen.title("US States Game")
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("./50_states.csv")

game_is_on = True
score = 0


def create_state(name, position):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.color("black")
    state.goto(position)
    state.pendown()
    state.write(name, align="center", font=FONT)


while game_is_on:
    guess = turtle.textinput(f"Guessed: {score}/50", "Enter a US State name")
    print(data.state.str.lower())
    if guess.lower() in [state.lower() for state in data.state.to_list()]:
        state_data = data[data.state.str.lower() == guess.lower()]
        state_name = state_data.state.to_string(index=False)
        state_position = (int(state_data.x), int(state_data.y))
        create_state(name=state_name, position=state_position)
        score += 1
    elif guess is None:
        break

screen.exitonclick()
