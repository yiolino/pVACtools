import pandas as pd
import polars as pl

path = '/Users/tetsu/Repositories/pVACtools/tests/test_data/pvacbind/MHC_Class_I/Test.all_epitopes.tsv'

df = pd.read_csv(path, delimiter='\t', float_precision='high', low_memory=False, na_values="NA", keep_default_na=False, dtype={"Mutation": str})
# df.sort_values(by=["Median Score"], inplace=True, ascending=True)
pd.DataFrame(df.groupby(['HLA Allele', 'Epitope Seq']).size().reset_index())

df = pl.read_csv(path, sep='\t', null_values="NA", dtypes={"Mutation": str})
df.groupby(['HLA Allele', 'Epitope Seq']).count().sort([pl.col("HLA Allele"), pl.col("Epitope Seq"), pl.col("count") **3], reverse=[False, False, True])

# float_precision='high', low_memory=False, na_values="NA", keep_default_na=False, dtype={"Mutation": str}``tyぺ

keys = df.columns
values = df[0, :].transpose().to_series().to_list()

dict = dict(zip(keys, values))
