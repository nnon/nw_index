import pandas as pd

class nw_ind:

    def __init__(self, df):
        self.indexes = {}
        for index, row in df.iterrows():
            self.indexes.update({row['quarter_year']: row[1:].to_dict()})
