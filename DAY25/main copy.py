from turtle import Turtle, Screen
import turtle
import pandas as pd

screen=Screen()
screen.title("US STATES GAME")
# screen.bgpic("./DAY25/blank_states_img.gif")
image= "./DAY25/blank_states_img.gif"
data_path="./DAY25/50_states.csv"
screen.addshape(image)


my_turtle=Turtle()
# my_turtle.hideturtle()
turtle.shape(image)

# def get_mouse_click_corr(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_corr)
# turtle.mainloop()

data=pd.read_csv(data_path)
all_states=data["state"].to_list()

# if data[answer_state]==data["state"]:
#     rows=data[data["state"]==answer_state]
#     x=rows["x"][0]
#     y=rows["y"][0]
#     turtle.write(answer_state)
#     turtle.goto(x,y)


guessed_list=[]

while len(guessed_list)<50:
    answer_state= screen.textinput(title=f"{len(guessed_list)}/50 the states",prompt="whats the another states name? ").title()

    if answer_state=="Exit":
        state_to_learn=[]
        for i in all_states:
            if i not in guessed_list:
                state_to_learn.append(i)
                print(state_to_learn)
        new_dataset=pd.DataFrame(state_to_learn)
        new_dataset.to_csv("./DAY25/States_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state not in guessed_list:
            guessed_list.append(answer_state)
            t=Turtle()
            t.hideturtle()
            t.penup()
            state_data=data[data.state == answer_state]
            t.goto(int(state_data.x.item()),int(state_data.y.item()))
            t.write(answer_state)

#states to learn

    