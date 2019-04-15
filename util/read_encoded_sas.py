import pandas as pd

def read_encoded_sas(file):
    for enc in ['iso-8859-1','iso-8859-2','utf-8','unicode','ascii','windows-1250','windows-1252','latin-1']:
        try:
            df=pd.read_sas(file, encoding=enc)
        except Exception as e: 
            print(e)
        else:
            break
    print ("Encoding used: " + enc)
    return df

dm = read_encoded_sas('dm.sas7bdat')
print(dm.head())