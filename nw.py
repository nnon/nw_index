import requests
import pandas as pd
import io
import math
import datetime

class nw_ind:

    def __init__(self, df):
        self.indexes = {}
        for index, row in df.iterrows():
            self.indexes.update({row['quarter_year']: row[1:].to_dict()})
        self.lastQuarter = df.tail(1)['quarter_year'].item()

def main():

    n_url = """
    https://www.nationwide.co.uk/-/media/MainSite/documents/about/house-price-index/downloads/all-prop.xls?date=june
    """

    resp = (requests.get(n_url, verify=False))

    with io.BytesIO(resp.content) as fh:
        df = pd.io.excel.read_excel(fh, skiprows=3, header=None,
                                    names=['quarter_year',
                                            'north_val',
                                            'north',
                                            'yorkshside_val',
                                            'yorkshside',
                                            'northwest_val',
                                            'northwest',
                                            'eastmids_val',
                                            'eastmids',
                                            'westmids_val',
                                            'westmids',
                                            'eastanglia_val',
                                            'eastanglia',
                                            'outerseast_val',
                                            'outerseast',
                                            'outermet_val',
                                            'outermet',
                                            'london_val',
                                            'london',
                                            'southwest_val',
                                            'southwest',
                                            'wales_val',
                                            'wales',
                                            'scotland_val',
                                            'scotland',
                                            'nireland_val',
                                            'nireland',
                                            'uk_val',
                                            'uk']).drop(columns=['north_val',
                                                                 'yorkshside_val',
                                                                 'northwest_val',
                                                                 'eastmids_val',
                                                                 'westmids_val',
                                                                 'eastanglia_val',
                                                                 'outerseast_val',
                                                                 'outermet_val',
                                                                 'london_val',
                                                                 'southwest_val',
                                                                 'wales_val',
                                                                 'scotland_val',
                                                                 'nireland_val',
                                                                 'uk_val'])
    nw = nw_ind(df)
    iv = index_val(datetime.date(2011, 11, 30), 250000, 'westmids', nw)
    print(iv)


def quarter_year(dateIn: datetime) -> str:
    return f'Q{str(math.ceil(dateIn.month/3.))} {dateIn.year}'


def index_val(dateOfLastVal: datetime, lastVal: float, region: str,
              nw: nw_ind) -> float:
    valQuarterYear = quarter_year(dateOfLastVal)
    origInd = nw.indexes[valQuarterYear][region]
    latestInd = nw.indexes[nw.lastQuarter][region]
    return latestInd/origInd * lastVal


if __name__ == '__main__':
    main()
