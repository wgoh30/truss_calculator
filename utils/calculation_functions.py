"""
calculation_functions.py
version 1.0
version date: 05 Apr 2026
"""
from numpy import linalg, matmul

def solve_axial_force(coefficientMatrix, loadMatrix):
    inverseCoefficientMatrix = linalg.inv(coefficientMatrix)
    answerMatrix = matmul(inverseCoefficientMatrix, loadMatrix)
    return answerMatrix