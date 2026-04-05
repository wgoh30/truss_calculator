"""
main.py
version: 1.0
version date: 05 Apr 2026
"""
from utils.setup_functions import setup
from utils.calculation_functions import solve_axial_force
from numpy import printoptions

def main() -> None:
    setupDict = setup()
    solvedForces = solve_axial_force(setupDict['coefficient_matrix'], setupDict['load_matrix'])

    # print out the output
    with printoptions(suppress=True, precision=3):
        for iteration in range(len(setupDict['force_matrix'])):
            print(f"{setupDict['force_list'][iteration].name}: {solvedForces[iteration][0]:.2f}")
if __name__ == "__main__":
    main()