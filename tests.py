from solver import Solver
from nytimporter import NYImporter
from puzzlecreator import PuzzleCreator


##p = PuzzleCreator(1,9)
##s = Solver()
##p.generate_puzzle()
##p.print_puzzle()
##print()
##result = s.solve(p.puzzle)
##if result is None:
    ##print("L")
##else:
    ##for x in range(9):
        ##for y in range(9):
            ##print(result[x][y], end = " ")
        ##print()

nyt = NYImporter()
nyt.getNYTPuzzle()
for x in range(9):
    for y in range(9):
        print(nyt.puzzle[x][y], end = " ")
    print()
print()
s = Solver()
result = s.solve(nyt.puzzle)
for x in range(9):
    for y in range(9):
        print(nyt.puzzle[x][y], end = " ")
    print()