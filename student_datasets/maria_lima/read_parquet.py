# coding: utf-8
#  !pip install pyarrow
#
import pandas as pd

# Read the Parquet file into a DataFrame
file_path = 'data_ocean_partition_MJL.parquet.gzip'  # Replace with the path to your Parquet file
df = pd.read_parquet(file_path)
#df.shape
#df.info()
print(df.describe())
