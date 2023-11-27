import pandas as pd
import seaborn as sns


def main():
  file_path = '../datasets/dataset_train.csv'
  df = pd.read_csv(file_path)

  sns.set(style='darkgrid')



if __name__ == '__main__':
  main()