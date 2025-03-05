# try 
# except
# else
# finally:



import pandas as pd


df = pd.read_csv("/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY30/nato_phonetic_alphabet.csv")
# print(df)

dict={row.letter: row.code for (index, row) in df.iterrows()}
# print(dict)


def generate_phonotic():
    try:
        nameinput=input("enter a name:").upper()
        output=[dict[i] for i in nameinput]
    except KeyError:
        print("Please enter the alphabets and not numbers")
        generate_phonotic()

    else:
        print(output)

generate_phonotic()
