import numpy
import pandas as pd
from pyq import q


def df2kdb():
  '''
  converts a panda dataframe built up from a dictionary to a 
  '''
  f = pd.DataFrame.from_dict({'a': [1,2], 'b':[3,4]})
  t = q('!', f.columns, f.values.T).flip
  t.show()
  
  
def df2kdb_fast():
  df = pd.DataFrame.from_dict({'a': [1,2], 'b':[3,4]})
  t = q('!', df.columns, [numpy.array(df[x]) for x in df.columns]).flip
  t.show()
