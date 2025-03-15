# https://docs.python.org/3/library/turtle.html         --turtle graphics docs
# https://cs111.wellesley.edu/reference/colors          --turtle colors
# https://pypi.org/project/prettytable/                 --prettytable
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki         --prettytable docs


# from turtle import *
from prettytable import PrettyTable

# anuja=Turtle()
# nishank=Turtle()
# print(anuja)
# anuja.shape("turtle")
# anuja.color("green","red")
# anuja.left(90)
# anuja.forward(100)
# anuja.right(130)
# anuja.forward(150)
# anuja.left(130)
# anuja.forward(100)


# nishank.shape("turtle")
# nishank.color("blue")
# nishank.left(60)
# nishank.forward(100)
# nishank.right(120)
# nishank.forward(100)
# nishank.penup()
# nishank.backward(50)
# nishank.pendown()
# nishank.right(120)
# nishank.forward(50)





# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


anujas_table=PrettyTable()

anujas_table.field_names = ["Pokemon name", "Type"]
anujas_table.add_rows(
    [["Pikachu", "Electric"],
    ["Squirtle","Water"],
    ["Charmender","Fire"]]
)

print(anujas_table)