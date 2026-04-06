from turtle import *
from utils.objects import *

def draw_truss(turtle, forceList):
    scaleFactor = 100
    hideturtle()
    for member in forceList:
        forceType = type(member)
        if forceType == SupportForce:
            penup()
            goto(member.parentNode.xPositionVector * scaleFactor, member.parentNode.yPositionVector * scaleFactor)
            pendown()
        if forceType == MemberForce:
            penup()
            goto(member.parentNode1.xPositionVector * scaleFactor, member.parentNode1.yPositionVector * scaleFactor)
            pendown()
            write(member.parentNode1.name)
            goto(member.parentNode2.xPositionVector * scaleFactor, member.parentNode2.yPositionVector * scaleFactor)
            write(member.parentNode2.name)
        # print(f'position {pos()}')

    exitonclick()