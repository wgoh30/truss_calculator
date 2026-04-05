"""
objects.py
version: 1.0
version date: 05 Apr 2026
"""
from math import atan, pi, sin, cos

class Node:
    def __init__(self, name: str, xPositionVector: float, yPositionVector: float) -> None:
        """
        Nodes where the members connect.
        
        Parameters:
            name (str): The name of the node
            xPositionVector (float): the x coordinate of where the node is relative to the origin.
            yPositionVector (float): the y coordinate of where the node is relative to the origin.
        """
        self.xPositionVector = xPositionVector
        self.yPositionVector = yPositionVector
        self.name = name
    def info(self) -> None:
        """
        Prints node information to the console

        Parameters:
            None

        Returns:
            None
        """
        print(f'{self.name} Coordinate: ({self.xPositionVector}, {self.yPositionVector})')

class Force:
    def __init__(self, name:str) -> None:
        self.magnitude = 0
        self.xDirectionVector = 0
        self.yDirectionVector = 0
        self.angle = 0
        self.name = name
    def info(self) -> None:
        """
        Prints force information

        Parameters:
            None

        Returns:
            None
        """
        print(f'Parent Nodes: {self.parentNode}\nDirection: ({self.xDirectionVector}, {self.yDirectionVector})\nAngle: {self.angle:.2f} rad\nMagnitude: {self.magnitude} N')

class SupportForce(Force):
    def __init__(self, name:str, parentNode: Node, axis: str):
        """
        Reaction force applied onto a joint.
        
        Parameters:
            name (str): Name of the force.
            parentNode (Node): The node of which the reaction force is applied on.
            axis (str): Takes in the axis of which the force is applied onto (x/y).
        """
        super().__init__(name)
        self.parentNode = parentNode
        if axis.lower() == 'x':
            self.angle = 0
            self.xDirectionVector = 1
        elif axis.lower() == 'y':
            self.angle = pi / 2
            self.yDirectionVector = 1

class MemberForce(Force):
    def __init__(self, name:str, parentNode1, parentNode2):
        """
        Force that is applied onto the member.
        
        Parameters:
            name (str): Name of the force.
            parentNode1 (Node): The first node of the member.
            parentNode2 (Node): The second node of the member.
        """
        super().__init__(name)
        self.parentNode1 = parentNode1
        self.parentNode2 = parentNode2
        self.xDirectionVector = parentNode2.xPositionVector - parentNode1.xPositionVector
        self.yDirectionVector = parentNode2.yPositionVector - parentNode1.yPositionVector 
        if self.xDirectionVector == 0:
            if self.yDirectionVector > 0:
                self.angle = pi / 2
            elif self.yDirectionVector < 0:
                self.angle = - pi / 2
            else:
                self.angle = 0
        else:
            self.angle = atan(self.yDirectionVector / self.xDirectionVector)

class LoadForce (Force):
    def __init__(self, name: str, parentNode: Node, magnitude: float, angle: float):
        """
        Load force applied onto a node.

        Parameters:
            name (str): Name of the force.
            parentNode (Node): The node that the load is applied onto.
            magnitude (float): The magnitude of the force in Newtons.
            angle (float): The angle of the force relative to the x-axis in radians.
        """
        super().__init__(name)
        self.parentNode = parentNode
        self.magnitude = magnitude
        self.angle = angle
        self.xDirectionVector = cos(self.angle)
        self.yDirectionVector = sin(self.angle)
