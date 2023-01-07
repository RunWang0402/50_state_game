import turtle

screen=turtle.Screen()

screen.title("U.S. States Game")

image="blank_states_img.gif"
screen.addshape(image)    #add shape which can be any image file, added shape to the screen; than you can change the shape to the
#to the image
turtle.shape(image)

# def get_mouse_click_coordinate(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coordinate) #an event listener; get the location of the mouse click and pass it onto the function in the ()
#
# turtle.mainloop() #keep screen open even though our code finish running

import pandas
data=pandas.read_csv("50_states.csv")
state_list=data["state"].tolist()

correct_states=[]

while len(correct_states)<50:
    if len(correct_states)<1:
        answer_state=screen.textinput(title="Guess the state",prompt="What's another state?")
    else:
        answer_state = screen.textinput(title=f"{len(correct_states)}/50 states correct", prompt="What's another state?")
    converted=answer_state.title()
    if converted=="Exit":
        break
    tim=turtle.Turtle()
    tim.hideturtle()
    if converted in state_list:
        correct_states.append(converted)
        location=data[data["state"]==converted]
        location_x=int(location.x)
        location_y=int(location.y)
        tim.penup()
        tim.setposition(location_x,location_y)
        tim.write(arg=converted,move=False,align="center",font=('Arial',8, 'normal'))


final_list=[state for state in state_list if state not in correct_states]
# for state in state_list:
#     if state not in correct_states:
#         final_list.append(state)


df=pandas.DataFrame(final_list)   # you can convert a list to a data frame too
df.to_csv("missing states")




