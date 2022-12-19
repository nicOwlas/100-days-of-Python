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

guessed_states = []


def create_state(name, position):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.color("black")
    state.goto(position)
    state.pendown()
    state.write(name, align="center", font=FONT)


while len(guessed_states) < 50:
    guess = turtle.textinput(
        f"Guessed: {len(guessed_states)}/50", "Enter a US State name"
    ).title()
    if guess == "Exit":
        # States to learn
        states_to_learn = []
        data_dict = {}
        for state in data.state.values:
            if state not in guessed_states:
                states_to_learn.append(state)

        data_dict["States to learn"] = states_to_learn

        panda_frame = pandas.DataFrame(data_dict)
        panda_frame.to_csv("states_to_learn.csv", index=False)
        break
    elif guess in data.state.values:
        state_data = data[data.state == guess]
        state_name = state_data.state.item()
        state_position = (int(state_data.x), int(state_data.y))
        create_state(name=state_name, position=state_position)
        guessed_states.append(state_name)
