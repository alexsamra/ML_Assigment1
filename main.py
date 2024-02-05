import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dc = pd.read_csv('Boston.csv')

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 1]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('crim')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 2]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('zn')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 3]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('indus')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 4]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('chas')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 5]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('nox')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 6]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('rm')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 7]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('age')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 8]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('dis')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 9]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('rad')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 10]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('tax')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 11]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('ptratio')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 12]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('lstat')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

ds = np.array(dc)
x = ds[:, 0]
y = ds[:, 13]
plt.plot(x, y, 'o', color='black')
plt.xlabel('Suburb Number')
plt.ylabel('medv')
plt.locator_params(axis='x', nbins=9) # set the number of bins for the x-axis
plt.show()

#dc.drop(dc[dc.horsepower == '?'].index, inplace=True)

#dc.drop(dc.index[10:85], inplace=True)

#dc.drop(dc[dc.horsepower == '?'].index, inplace=True)
# print(dc.dtypes)
# for column in dc.columns:
#     if column == 'horsepower':
#         horsepower = dc[dc.horsepower != '?']
#         horsepower = horsepower.astype({'horsepower': 'int64'})
#         #print(horsepower[horsepower.horsepower == '?'])
#         print(column)
#         print(horsepower[column].max(numeric_only=True)-horsepower[column].min(numeric_only=True))
#         print(horsepower[column].mean())
#         print(horsepower[column].std())
#     elif column != 'name':
#         print(column)
#         print((int(dc[column].max())-int(dc[column].min())))
#         print(dc[column].mean())
#         print(dc[column].std())

# print(dc['horsepower'].max())