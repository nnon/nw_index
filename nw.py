import requests
import pandas as pd
import io

n_url = """
https://www.nationwide.co.uk/-/media/MainSite/documents/about/house-price-index/downloads/all-prop.xls?date=june
"""

resp = (requests.get(n_url, verify=False))

with io.BytesIO(resp.content) as fh:
    df = pd.io.excel.read_excel(fh, skiprows=3, header=None, names=['north_val',
        'north_ind',
        'yorkshside_val',
        'yorkshside_ind',
        'northwest_val',
        'northwest_ind',
        'eastmids_val',
        'eastmids_ind',
        'westmids_val',
        'westmids_ind',
        'eastanglia_val',
        'eastanglia_ind',
        'outerseast_val',
        'outerseast_ind',
        'outermet_val',
        'outermet_ind',
        'london_val',
        'london_ind',
        'southwest_val',
        'southwest_ind',
        'wales_val',
        'wales_ind',
        'scotland_val',
        'scotland_ind',
        'nireland_val',
        'nireland_ind',
        'uk_val,uk_ind'])
print(df.__dict__)
