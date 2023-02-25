import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
class NYImporter:

    def __init__(self):
        self.puzzle = [[0] * 9] * 9
        self.difficulty = input("Select Difficulty 1: Easy 2: Hard 3: Medium ")


    def getNYTPuzzle(self):
        url = 'https://www.nytimes.com/puzzles/sudoku'
        x = requests.get(url)
        html = BeautifulSoup(x.text, 'html.parser')
        scripts_data = html.find('script', attrs = {'type':'text/javascript'})
        puzzle_data = scripts_data.contents[0]
        sudoku_puzzle = puzzle_data.split('.gameData = ')[1]
        json_puzzle = json.loads(sudoku_puzzle)

        if int(self.difficulty) == 1:
            sudoku = json_puzzle['easy']['puzzle_data']['puzzle']
        elif int(self.difficulty) == 2:
            sudoku = json_puzzle['hard']['puzzle_data']['puzzle']
        else:
            sudoku = json_puzzle['medium']['puzzle_data']['puzzle']

        print(sudoku)

        self.puzzle = self.data_to_matrix(sudoku)

    def data_to_matrix(self, string):
        matrix_list = np.array(string)
        return matrix_list.reshape(9,9)




