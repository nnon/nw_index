import requests
import xlrd
import pandas as pd
import io
from pprint import pprint

n_url = """
https://www.nationwide.co.uk/-/media/MainSite/documents/about/house-price-index/downloads/all-prop.xls?date=june
"""

resp = (requests.get(n_url, verify=False))

with io.BytesIO(resp.content) as fh:
    df = pd.io.excel.read_excel(fh)

print(df)
