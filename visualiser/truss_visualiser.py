from turtle import *
from utils.objects import *

def color_scale_setup(solvedForces: list) -> list:
    """
    Creates a scale of the forces as a decimal (0 - 1)
    
    Parameters:
        solvedForces (list): The array of solved forces

    Returns:
        colorList (list): The list of rgb values (also a list) in relation to the largest force on each member.
    """
    magnitudeList: list = []
    colorList: list = []
    red = 255
    green = 255
    for force in solvedForces:
        magnitudeList.append(abs(force[0]))
    largestForce = max(magnitudeList)
    for iteration in range(len(magnitudeList)): # make the percentages
        magnitudeList[iteration] /= largestForce
    for percentage in magnitudeList: # assign the color list
        colorList.append((int(red * percentage), int(green * (1 - percentage)), 0))
    # print(f'Mag: {magnitudeList}\nCol: {colorList}')
    return colorList

def draw_truss(turtle, forceList, solvedForces):
    scaleFactor = 1
    hideturtle()
    colorList = color_scale_setup(solvedForces)
    for iteration in range(len(forceList)):
        member = forceList[iteration]
        forceType = type(member)
        if forceType == SupportForce:
            penup()
            goto(member.parentNode.xPositionVector * scaleFactor, member.parentNode.yPositionVector * scaleFactor)
            pendown()
        if forceType == MemberForce:
            penup()
            goto(member.parentNode1.xPositionVector * scaleFactor, member.parentNode1.yPositionVector * scaleFactor)
            pendown()
            color('black')
            write(member.parentNode1.name)
            color(colorList[iteration])
            goto(member.parentNode2.xPositionVector * scaleFactor, member.parentNode2.yPositionVector * scaleFactor)
            write(member.parentNode2.name)
        # print(f'position {pos()}')

    exitonclick()