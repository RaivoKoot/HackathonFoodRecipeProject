import pandas as pd

file = pd.read_pickle('ingredient_compounds_binary.pkl')
file.to_csv('ingr_comp_bin.csv')
