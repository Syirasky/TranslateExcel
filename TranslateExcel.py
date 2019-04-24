import xlrd
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from googletrans import Translator

translator = Translator()
print("Excel File Translate for Apps Language Translate")

loc = ("Example_Labels.xlsx")

df = pd.read_excel(loc)
print("Count in data record")
print(df.count())

start_at = 1
end_at = 10

for start_at in range(end_at):
	EnWordStr = df['EN'][start_at].encode('utf-8')
	TranslatedEnStr = translator.translate(EnWordStr , dest='ms')

	print(df['EN'][start_at].encode('utf-8')," : ",TranslatedEnStr.text.encode('utf-8'))
