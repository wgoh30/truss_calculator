"""
setup_functions.py
version: 1.0
version date: 5 Apr 2026
"""
from math import pi, cos, sin
from numpy import array
from .objects import MemberForce, SupportForce, LoadForce, Node

def force_matrix_setup(forceList: list):
    """
    Makes the magnitude matrix for the forces in a column matrix.

    Parameter:
        forceList (list): The list of forces.

    Returns:
        forceMatrix (NDArray): the nx1 matrix of forces.
    """
    forceMatrixList: list = []
    for forces in forceList:
        forceMatrixList.append([forces])
    forceMatrix = array(forceMatrixList)
    return forceMatrix


def coefficient_matrix_setup(nodeList: list, forceList: list) -> array:
    """
    Makes the coeffiecient matrix of forces based off of the node list and the force list

    Parameter:
        nodeList (list): The list of the nodes.
        forceList (list): The list of the forces in a vertical matrix form

    Returns:
        coefficientMatrix (NDArray): the nxn coefficient matrix of the forces.
    """
    coefficientList = []

    # print(f'Total unknown forces: {len(forceList)}') # Debug line 
    for nodeToAnalyse in nodeList: # Iterates the following for each node in the nodeList
        coefficientListRow1 = [] # Equation on the x axis
        coefficientListRow2 = [] # Equation on the y axis
        for forces in forceList: # Iterates for each force in the forceList
            forceType = type(forces) # Gets the type of force in the list
            # print(f'ForceType: {forceType}\n') # Debug Line
            if forceType == MemberForce:
                # print(f'force analysed parent nodes: {forces[0].parentNode1}, {forces[0].parentNode2}\n') # Debug Line
                if forces.parentNode1 == nodeToAnalyse: # The force is pointing in the positive direction
                    coefficientListRow1.append(cos(forces.angle))
                    coefficientListRow2.append(sin(forces.angle))
                elif nodeToAnalyse == forces.parentNode2: # The force is the opposing force on the same member. This means that the coefficients will be negative
                    coefficientListRow1.append(-cos(forces.angle))
                    coefficientListRow2.append(-sin(forces.angle))
                else:
                    coefficientListRow1.append(0)
                    coefficientListRow2.append(0)
            elif forceType == SupportForce:
                if forces.parentNode == nodeToAnalyse:
                    coefficientListRow1.append(cos(forces.angle))
                    coefficientListRow2.append(sin(forces.angle))
                else:
                    coefficientListRow1.append(0)
                    coefficientListRow2.append(0)

        # print(f'{coefficientListRow1} - {len(coefficientListRow1)} entries\n{coefficientListRow2}') # Debug line
        coefficientList.append(coefficientListRow1)
        coefficientList.append(coefficientListRow2)
    
    # print(coefficientList) # Debug line
    coefficientMatrix = array(coefficientList)
    return coefficientMatrix

def load_matrix_setup(nodeList: list, loadList: list):
    """
    Makes the matrix of loads on the joints. All joints are assumed to be in static equilibirum.

    Parameter:
        nodeList (list): a list of nodes.
        loadList (list): a list of loads.

    Returns:
        loadMatrix (NDArray): a nx1 matrix of the loads.
    """
    loadMatrixList = []
    for nodeToAnalayse in nodeList:
        for load in loadList:
            if load.parentNode == nodeToAnalayse:
                loadMatrixList.append([load.magnitude * cos(load.angle)])
                loadMatrixList.append([load.magnitude * sin(load.angle)])
            else:
                loadMatrixList.append([0])
                loadMatrixList.append([0])
    loadMatrix = array(loadMatrixList)
    return loadMatrix



def setup() -> dict:
    """
    Setups the program or something like that.

    Parameters:
        None

    Returns:
        returnDict (dict): dictionary with a the force_matrix, coefficient_matrix and load_matrix.
    """
    #  ------------------------------ Edit Here ------------------------------ #
    # nodes
    A = Node('A',0,0)
    B = Node('B',1,1)
    C = Node('C',2,0) 
    nodeList = [A, B, C]

    # Forces
    Fab = MemberForce("Fab", A,B)
    Fac = MemberForce("Fac", A,C)
    Fbc = MemberForce("Fbc",B,C)
    Ax = SupportForce("Ax", A, 'x')
    Ay = SupportForce("Ay", A, 'y')
    Cy = SupportForce("Cy", C, 'y')
    forceList = [Ax, Ay, Fab, Fac, Fbc, Cy]

    # Loads
    Lb = LoadForce("Lb", B, 100, -pi/2)
    loadList = [Lb]
    #  ------------------------------ Edit Here ------------------------------ #

    forceMatrix = force_matrix_setup(forceList)
    coefficientMatrix = coefficient_matrix_setup(nodeList, forceList)
    loadMatrix = load_matrix_setup(nodeList, loadList)

    returnDict = {
        'force_matrix': forceMatrix,
        'force_list': forceList,
        'coefficient_matrix': coefficientMatrix,
        'load_matrix': loadMatrix
    }

    return returnDict