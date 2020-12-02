import pandas as pd
import numpy as np

from quickscreen.analysis.linear_analysis import *
from quickscreen.analysis.datafill import *

if __name__ == "__main__":

    def datafill_example():
        return

    def init_example():
        df = pd.read_csv("./data/CarPrice.csv")
        
        de = DataEdit(df)

        print(type(de).__name__)

    def display_example():
        df = pd.read_csv("./data/CarPrice.csv")
        
        de = DataEdit(df)

        print(de.display().head())

    def column_type_example():
        df = pd.read_csv("./data/CarPrice.csv")
        
        de = DataEdit(df)

        # getting column type by column index
        print(de.columntype(2))

        # getting column type by column name
        print(de.columntype("enginesize"))

    def add_example():
        data1 = {
                "a":[1,2,3,4,5,6,4],
                "b":[11,12,13,14,15,np.nan,14]
        }
        df = pd.DataFrame(data1, columns=["a", "b"])
        de = DataEdit(df)

        data2 = {
                "a":[x for x in range(0, 10)],
                "b":[2*x for x in range(0, 10)]
        }

        df2 = pd.DataFrame(data2, columns=["a", "b"])
        # print(df.shape)
        # print(df2.shape)

        # print(df.append(df2))
        # print(df.append(df2).shape)

        de2 = de + df2

        print(de.data.shape, df2.shape, de2.data.shape)

    
    def sub_example():
        # sub example

        df = pd.read_csv("./data/CarPrice.csv")
        # print(df.head())

        de = DataEdit(df)
        de1 = DataEdit(df)

        two_row = (df.iloc[0:2])
        print(type(two_row.iloc[0:1]))
        print(two_row)

        d = de - two_row
        print(df.shape)
        print(d.data.shape)

    def rm_duplicates_example():

        # rm_duplicates example
        data = {
                "a":[1,2,3,4,5,6,4],
                "b":[11,12,13,14,15,np.nan,14]
                }
        df = pd.DataFrame(data, columns=["a", "b"])
        de = DataEdit(df)

        print(de.data.head(10))

        de_no_na = de.rm_duplicates()
        print(de_no_na.data.head(10))

    def rm_nan_example():
        # rm_nan example
        data = {
                "a":[1,2,3,4,5,6,7],
                "b":[11,12,13,14,15,np.nan,17]
                }
        df = pd.DataFrame(data, columns=["a", "b"])
        de = DataEdit(df)

        print(de.data.head(10))

        de_no_na = de.rm_nan()
        print(de_no_na.data.head(10))

    def quick_clean_example():

        # quick clean example
        data = {
                "a":[1,2,3,4,5,6,4],
                "b":[11,12,13,14,15,np.nan,14]
                }
        df = pd.DataFrame(data, columns=["a", "b"])
        de = DataEdit(df)

        print(de.data.head(10))

        de_no_na = de.quick_clean()
        print(de_no_na.data.head(10))

    def Lm_example():
        return

    def lm_init_example():
        df = pd.read_csv("./data/CarPrice.csv")
        lm = Lm(df)
    
    def single_linear_example():
        df = pd.read_csv("./data/CarPrice.csv")
        lm = Lm(df)
        print(df.columns)
        slr = lm.single_linear("horsepower", "enginesize")    
        print(slr)


    def single_linear_plot_example():
        df = pd.read_csv("./data/CarPrice.csv")
        lm = Lm(df)
        lm.single_linear_plot("horsepower", "enginesize")

    def single_linear_eqn_example():
        df = pd.read_csv("./data/CarPrice.csv")
        lm = Lm(df)
        lm.single_linear_eqn("horsepower", "enginesize")



single_linear_eqn_example()