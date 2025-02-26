import pandas as pd


df = pd.read_csv("DAY26/nato_phonetic_alphabet.csv")
# print(df)

dict={row.letter: row.code for (index, row) in df.iterrows()}
print(dict)

nameinput=input("enter a name:").upper()
output=[dict[i] for i in nameinput]
print(output)

