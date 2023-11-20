import pandas as pd
import numpy as np

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

    ################################################
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
    ################################################

    def var(self, ddof=1):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            n = len(self.df[col]) - 1
            s[col] = (1 / n) * np.sum((self.df[col] - self.mean()[col]) ** 2)
        return s

    def std(self, ddof=1):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            n = len(self.df[col]) - 1
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

    ################################################
    def quantile(self, q=0.5):
        s = pd.Series(dtype=object)
        for col in self.df.columns:
            values = sorted(self.df[col])
            index = q * (len(values) - 1) 
            if index.is_integer():
                s[col] = values[int(index)]
            else:
                lower_index = int(index)
                upper_index = lower_index + 1
                lower_value = values[lower_index]
                upper_value = values[upper_index]
                interpolation = lower_value + (upper_value - lower_value) * (index - lower_index)
                s[col] = interpolation
        return s
    ################################################

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

def main():
  file_path = input("Enter the dataset filepath: ")

  try:
    df = pd.read_csv(file_path)
    my_df = MyNumDataFrame(df)
    print(my_df.describe())

  except:
    print("File not found!")

if __name__ == '__main__':
  main()