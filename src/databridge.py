# Configuration of pandas functions
import os
import numpy as np
import pandas as pd

FILES_FOLDER = os.path.join(os.getcwd(),'files')

def get_sheets(path_doc):
    path_doc = os.path.join(FILES_FOLDER,path_doc)
    exceldoc = pd.ExcelFile(path_doc)
    print(exceldoc.sheet_names)

if __name__ == '__main__':
    get_sheets('despachos.xlsx')



