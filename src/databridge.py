# Configuration of pandas functions
import os
import numpy as np
import pandas as pd

FILES_FOLDER = os.path.join(os.getcwd(),'files')

class ExcelDataFile():
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.path_filename = os.path.join(self.path,self.filename)

    def get_sheets(self):
        exceldoc = pd.ExcelFile(self.path_filename)
        return exceldoc.sheet_names

# if __name__ == '__main__':
    # excel = ExcelDataFile(FILES_FOLDER,'pendientes.xlsx') 
    # print(excel.get_sheets())



