
def df2kdb():


f = pd.DataFrame.from_dict({'a': [1,2], 'b':[3,4]})
t = q('!', f.columns, f.values.T).flip
t.show()
