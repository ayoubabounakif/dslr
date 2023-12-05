import pandas as pd
import numpy as np
import math

class MyNumDataFrame:
    def __init__(self, df):
        df = df.select_dtypes(include=np.number)
        df = df.interpolate(method='linear')
        self.df = df

    def count(self):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            s[col] = len(self.df[col])
        return s

    def mean(self):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            n = len(self.df[col])
            s[col] = np.sum(self.df[col]) / n
        return s

    def median(self):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            n = len(self.df[col])
            values = sorted(self.df[col])
            if n % 2 == 0:
                index = n // 2
                s[col] = (values[index] + values[index - 1]) / 2
            else:
                index = (n - 1) // 2
                s[col] = values[index]
        return s

    def var(self, ddof=1):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            n = len(self.df[col]) - ddof
            s[col] = (1 / n) * np.sum((self.df[col] - self.mean()[col]) ** 2)
        return s

    def std(self, ddof=1):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            n = len(self.df[col]) - ddof
            s[col] = np.sqrt((1 / n) * np.sum((self.df[col] - self.mean()[col]) ** 2))
        return s

    def min(self):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            s[col] = min(self.df[col])
        return s

    def max(self):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            s[col] = max(self.df[col])
        return s

    def quantile(self, q=0.5):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            sorted_values = sorted(self.df[col])
            index = (len(sorted_values) - 1) * q
            if index.is_integer():
                s[col] = sorted_values[int(index)]
            else:
                lower_index = math.floor(index)
                upper_index = math.ceil(index)
                s[col] = (sorted_values[lower_index] + sorted_values[upper_index]) / 2
        return s

    def describe(self):
        df = pd.DataFrame(dtype=object, columns=self.df.columns)

        df.loc['count'] = self.count()
        df.loc['mean'] = self.mean()
        df.loc['median'] = self.median()
        df.loc['var'] = self.var()
        df.loc['std'] = self.std()
        df.loc['min'] = self.min()
        df.loc['25%'] = self.quantile(0.25)
        df.loc['50%'] = self.quantile(0.5)
        df.loc['75%'] = self.quantile(0.75)
        df.loc['max'] = self.max()

        return df

# TODO: Edit script to take in command line arguments
def main():
#   file_path = input("Enter the dataset filepath: ")

  try:
    file_path = '../datasets/dataset_train.csv'
    df = pd.read_csv(file_path)
    print(df.describe())
    # my_df = MyNumDataFrame(df)
    # print(my_df.describe())

  except:
    print("File not found!")

if __name__ == '__main__':
  main()