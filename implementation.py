from kmeans import Simulator
import pandas as pd

path = r'example\data_1.csv'
data = pd.read_csv(path)
Simulator(data[['first','second']],4).fit().create_gif('output_1')

path = r'example\data_2.csv'
data = pd.read_csv(path)[['a','b']]
Simulator(data,3).fit().create_gif('output_2')

path = r'example\data_3.csv'
data = pd.read_csv(path)[['x','y']]
Simulator(data,6).fit().create_gif('output_3')