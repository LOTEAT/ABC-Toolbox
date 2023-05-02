import pandas as pd

def _xlsx2csv(in_file, out_file):
    try:
        data_xls = pd.read_excel(in_file, index_col=0)
        data_xls.to_csv(out_file, encoding='utf-8')
        return True
    except:
        return False

