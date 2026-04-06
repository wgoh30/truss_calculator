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

    # ---------------------- Section B stand alone- Version 1 ----------------------- #
    # A = Node('A', 0, 53.57)
    # B = Node('B', 100.31, 53.57)
    # C = Node('C', 175.33, 53.57) 
    # D = Node('D', 231.43, 53.57)
    # E = Node('E', 273.39,53.57)
    # F = Node('F', 304.76, 53.37)
    # G = Node('G', 397.8, 53.37)

    # H = Node('H', 0, 0)
    # I = Node('I', 75.24, 10.13)
    # J = Node('J', 156.58, 21.09)
    # K = Node('K', 217.41, 29.28)
    # L = Node('K', 262.41, 35.4)
    # M = Node('M', 296.92, 39.98)
    # nodeList = [A, B, C, D, E, F, G, H, I, J, K, L, M]

    # Fab = MemberForce("Fab", A,B)
    # Fbc = MemberForce('Fbc', B, C)
    # Fcd = MemberForce('Fcd', C, D)
    # Fde = MemberForce('Fde', D, E)
    # Fef = MemberForce('Fef', E, F)
    # Ffg = MemberForce('Ffg', F, G)

    # Fhi = MemberForce('Fhi', H, I)
    # Fij = MemberForce('Fij', I, J)
    # Fjk = MemberForce('Fjk', J, K)
    # Fkl = MemberForce('Fkl', K, L)
    # Flm = MemberForce('Flm', L, M)
    # Fmg = MemberForce('Fmg', M, G)

    # # Fah = MemberForce('Fah', A, H)
    # Fai = MemberForce('Fai', A, I)
    # Fib = MemberForce('Fib', I, B)
    # Fbj = MemberForce('Fbj', B, J)
    # Fjc = MemberForce('Fjc', J, C)
    # Fck = MemberForce('Fck', C, K)
    # Fkd = MemberForce('Fkd', K, D)
    # Fdl = MemberForce('Fdl', D, L)
    # Fle = MemberForce('Fle', L, E)
    # Fem = MemberForce('Fem', E, M)
    # Fmf = MemberForce('Fmf', M, F)

    # Ax = SupportForce('Ax', A, 'x')
    # Ay = SupportForce('Ay', A, 'y')
    # Hy = SupportForce('Hy', H, 'y')
    # Hx = SupportForce('Hx', H, 'x')
    # # forceList = [Fab, Fbc, Fcd, Fde, Fef, Ffg, Fhi, Fij, Fjk, Fkl, Flm, Fmg, Fah, Fai, Fib, Fbj, Fjc, Fck, Fkd, Fdl, Fle, Fem, Fmf, Ax, Ay, Hy]
    # forceList = [Fab, Fbc, Fcd, Fde, Fef, Ffg, Fhi, Fij, Fjk, Fkl, Flm, Fmg, Fai, Fib, Fbj, Fjc, Fck, Fkd, Fdl, Fle, Fem, Fmf, Ax, Ay, Hx, Hy]

    # Lg = LoadForce("Lg", G, 2.5 * 9.8, -pi/2)
    # loadList = [Lg]

    # ---------------------- Section A Pratt Truss ----------------------- #
    # #  Section B nodes
    # A = Node('A', 0, 53.57)
    # B = Node('B', 100.31, 53.57)
    # C = Node('C', 175.33, 53.57) 
    # D = Node('D', 231.43, 53.57)
    # E = Node('E', 273.39,53.57)
    # F = Node('F', 304.76, 53.37)
    # G = Node('G', 397.8, 53.37)

    # H = Node('H', 0, 0)
    # I = Node('I', 75.24, 10.13)
    # J = Node('J', 156.58, 21.09)
    # K = Node('K', 217.41, 29.28)
    # L = Node('K', 262.41, 35.4)
    # M = Node('M', 296.92, 39.98)
    # # Section A nodes
    # sectionAHeight = 53.57
    # N = Node('N', -400, sectionAHeight)
    # O = Node('O', -320, sectionAHeight) 
    # P = Node('P', -240, sectionAHeight) 
    # Q = Node('Q', -160, sectionAHeight)
    # R = Node('R', -80, sectionAHeight)

    # S = Node('S', -400, 0)
    # T = Node('T', -320, 0) 
    # U = Node('U', -240, 0) 
    # V = Node('V', -160, 0) 
    # W = Node('W', -80, 0) 

    # nodeList = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W]

    # # Section B members
    # Fab = MemberForce("Fab", A,B)
    # Fbc = MemberForce('Fbc', B, C)
    # Fcd = MemberForce('Fcd', C, D)
    # Fde = MemberForce('Fde', D, E)
    # Fef = MemberForce('Fef', E, F)
    # Ffg = MemberForce('Ffg', F, G)

    # Fhi = MemberForce('Fhi', H, I)
    # Fij = MemberForce('Fij', I, J)
    # Fjk = MemberForce('Fjk', J, K)
    # Fkl = MemberForce('Fkl', K, L)
    # Flm = MemberForce('Flm', L, M)
    # Fmg = MemberForce('Fmg', M, G)

    # Fah = MemberForce('Fah', A, H)
    # Fai = MemberForce('Fai', A, I)
    # Fib = MemberForce('Fib', I, B)
    # Fbj = MemberForce('Fbj', B, J)
    # Fjc = MemberForce('Fjc', J, C)
    # Fck = MemberForce('Fck', C, K)
    # Fkd = MemberForce('Fkd', K, D)
    # Fdl = MemberForce('Fdl', D, L)
    # Fle = MemberForce('Fle', L, E)
    # Fem = MemberForce('Fem', E, M)
    # Fmf = MemberForce('Fmf', M, F)

    # # Section A members
    # Fno = MemberForce('Fno', N, O)
    # Fop = MemberForce('Fop', O, P)
    # Fpq = MemberForce('Fpq', P, Q)
    # Fqr = MemberForce('Fqr', Q, R) 
    # Fra = MemberForce('Fra', R, A)

    # Fst = MemberForce('Fst', S, T)
    # Ftu = MemberForce('Ftu', T, U)
    # Fuv = MemberForce('Fuv', U, V)
    # Fvw = MemberForce('Fvw', V, W)
    # Fwh = MemberForce('Fwh', W, H)

    # Fns = MemberForce('Fns', N, S)
    # Fot = MemberForce('Fot', O, T)
    # Fpu = MemberForce('Fpu', P, U)
    # Fqv = MemberForce('Fqv', Q, V)
    # Frw = MemberForce('Frw', R, W)

    # Fnt = MemberForce('Fnt', N, T)
    # Fou = MemberForce('Fou', O, U)
    # Fpv = MemberForce('Fpv', P, V)
    # Fqw = MemberForce('Fqw', Q, W)
    # Frh = MemberForce('Frh', R, H)

    # # Supports
    # Hy = SupportForce('Hy', H, 'y')
    # Sx = SupportForce('Sx', S, 'x')
    # Sy = SupportForce('Sy', S, 'y')

    # forceList = [Fab, Fbc, Fcd, Fde, Fef, Ffg, Fah, Fhi, Fij, Fjk, Fkl, Flm, Fmg, Fai, Fib, Fbj, Fjc, Fck, Fkd, Fdl, Fle, Fem, Fmf, Fno, Fop, Fpq, Fqr, Fra, Fst, Ftu, Fuv, Fvw, Fwh, Fns, Fot, Fpu, Fqv, Frw, Fnt, Fou, Fpv, Fqw, Frh, Hy, Sx, Sy]

    # Lg = LoadForce("Lg", G, 2.5 * 9.8, -pi/2)
    # loadList = [Lg]

    # ---------------------- Section A Warren Truss ----------------------- #
    #  Section B nodes
    A = Node('A', 0, 53.57)
    B = Node('B', 100.31, 53.57)
    C = Node('C', 175.33, 53.57) 
    D = Node('D', 231.43, 53.57)
    E = Node('E', 273.39,53.57)
    F = Node('F', 304.76, 53.37)
    G = Node('G', 397.8, 53.37)

    H = Node('H', 0, 0)
    I = Node('I', 75.24, 10.13)
    J = Node('J', 156.58, 21.09)
    K = Node('K', 217.41, 29.28)
    L = Node('K', 262.41, 35.4)
    M = Node('M', 296.92, 39.98)
    # Section A nodes
    sectionAHeight = 53.57
    N = Node('N', -400, sectionAHeight)
    O = Node('O', -320, sectionAHeight) 
    P = Node('P', -240, sectionAHeight) 
    Q = Node('Q', -160, sectionAHeight)
    R = Node('R', -80, sectionAHeight)

    S = Node('S', -400, 0)
    T = Node('T', -320, 0) 
    U = Node('U', -240, 0) 
    V = Node('V', -160, 0) 
    W = Node('W', -80, 0) 

    nodeList = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W]

    # Section B members
    Fab = MemberForce("Fab", A,B)
    Fbc = MemberForce('Fbc', B, C)
    Fcd = MemberForce('Fcd', C, D)
    Fde = MemberForce('Fde', D, E)
    Fef = MemberForce('Fef', E, F)
    Ffg = MemberForce('Ffg', F, G)

    Fhi = MemberForce('Fhi', H, I)
    Fij = MemberForce('Fij', I, J)
    Fjk = MemberForce('Fjk', J, K)
    Fkl = MemberForce('Fkl', K, L)
    Flm = MemberForce('Flm', L, M)
    Fmg = MemberForce('Fmg', M, G)

    Fah = MemberForce('Fah', A, H)
    Fai = MemberForce('Fai', A, I)
    Fib = MemberForce('Fib', I, B)
    Fbj = MemberForce('Fbj', B, J)
    Fjc = MemberForce('Fjc', J, C)
    Fck = MemberForce('Fck', C, K)
    Fkd = MemberForce('Fkd', K, D)
    Fdl = MemberForce('Fdl', D, L)
    Fle = MemberForce('Fle', L, E)
    Fem = MemberForce('Fem', E, M)
    Fmf = MemberForce('Fmf', M, F)

    # Section A members
    Fno = MemberForce('Fno', N, O)
    Fop = MemberForce('Fop', O, P)
    Fpq = MemberForce('Fpq', P, Q)
    Fqr = MemberForce('Fqr', Q, R) 
    Fra = MemberForce('Fra', R, A)

    Fst = MemberForce('Fst', S, T)
    Ftu = MemberForce('Ftu', T, U)
    Fuv = MemberForce('Fuv', U, V)
    Fvw = MemberForce('Fvw', V, W)
    Fwh = MemberForce('Fwh', W, H)

    Fns = MemberForce('Fns', N, S)
    Fot = MemberForce('Fot', O, T)
    Fpu = MemberForce('Fpu', P, U)
    Fqv = MemberForce('Fqv', Q, V)
    Frw = MemberForce('Frw', R, W)

    Fso = MemberForce('Fnt', S, O)
    Fou = MemberForce('Fou', O, U)
    Fuq = MemberForce('Fpv', U, Q)
    Fqw = MemberForce('Fqw', Q, W)
    Fwa = MemberForce('Frh', W, A)

    # Supports
    Hy = SupportForce('Hy', H, 'y')
    Sx = SupportForce('Sx', S, 'x')
    Sy = SupportForce('Sy', S, 'y')

    forceList = [Fab, Fbc, Fcd, Fde, Fef, Ffg, Fah, Fhi, Fij, Fjk, Fkl, Flm, Fmg, Fai, Fib, Fbj, Fjc, Fck, Fkd, Fdl, Fle, Fem, Fmf, Fno, Fop, Fpq, Fqr, Fra, Fst, Ftu, Fuv, Fvw, Fwh, Fns, Fot, Fpu, Fqv, Frw, Fso, Fou, Fuq, Fqw, Fwa, Hy, Sx, Sy]

    Lg = LoadForce("Lg", G, 2.5 * 9.8, -pi/2)
    loadList = [Lg]

    return {
        'node_list': nodeList,
        'force_list': forceList,
        'load_list': loadList
    }