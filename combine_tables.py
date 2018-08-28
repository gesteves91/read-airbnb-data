import pandas
filenames = ["for.csv", "bh.csv", "poa.csv",
"sp.csv", "rj.csv", "sal.csv"]
df = pandas.DataFrame()
for filename in filenames:
    df = df.append(pandas.read_csv(filename))
df.to_csv('br.csv', index=False)

