import numpy as np
import pandas as pd
import os


df = pd.read_csv('D:\Vs code\dvc-demo\data\Ecommerce Customers.csv')


df = df.iloc[:, 3:]

df = df[df['Length of Membership'] > 3]

df.to_csv(os.path.join('data','customers.csv'))