"""
define.py
version 1.0
version date 6 Apr 2026
"""
from utils.objects import *

def define_objects() -> list:
    """
    Define the nodes, forces and loads here.

    Returns:
        Dict: dictionary with keys node_list, force_list and load_list
    """

    # ---------------------- Edit Here ----------------------- #
    A = Node('A',0,0)
    B = Node('B',0,2)
    C = Node('C',2,0) 
    nodeList = [A, B, C]

    Fab = MemberForce("Fab", A,B)
    Fac = MemberForce("Fac", A, C)
    Fbc = MemberForce("Fbc",B,C)
    Ay = SupportForce("Ay", A, 'y')
    Ax = SupportForce('Ax', A, 'x')
    Cy = SupportForce("Cy", C, 'y')
    forceList = [Fab, Fac, Fbc, Ay, Ax, Cy]

    Lb = LoadForce("Lb", B, 500, 0)
    loadList = [Lb]
    # ---------------------- Edit Here ----------------------- #

    return {
        'node_list': nodeList,
        'force_list': forceList,
        'load_list': loadList
    }

