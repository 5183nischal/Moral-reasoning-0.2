import pandas as pd 
md = pd.read_stata("../circuit_metadata_excerpt.dta") #md for metadata
print(md.keys())