import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


'''
Questions:

make of a car and its effects on price:
    - .##DONE##

visual attributes and its effects on price:
    - get body style (sedan, coupe, etc..) and its coloration with price ##DONE##
    - get hight and see its corolation with price <xy graph> ##DONE##
    - get width and see its corolation with price <xy graph> ##DONE##

powertrain and its effects on price
    - horsepower and price <xy> ##DONE##
    - wheel drive [4wd, fwd, rwd] and price <bar graph> ##DONE##
    - diesel vs gas  ##DONE##
'''
#get every brand and its avg price
def make_and_price(data):
    makes_avgs = data.groupby('make')['price'].mean()
    makes_avgs.plot.bar(x='make', y='price')
    plt.show()
    plt.close()

# get the body style relation to price
def bodystyle_and_price(data):
    body_style_and_price = data.groupby("body-style")['price'].mean()
    body_style_and_price.plot.bar(x='body-style', y='price')
    plt.show()
    plt.close()

# get the length relation to price
def length_and_price(data):
    body_style_and_price = data.groupby('length')['price'].mean()
    body_style_and_price.plot.line(x='length', y='price')
    plt.show()
    plt.close()

# get the width relation to price
def width_and_price(data):
    body_style_and_price = data.groupby('width')['price'].mean()
    body_style_and_price.plot.line(x='width', y='price')
    plt.show()
    plt.close()

# get the horsepower relation to price
def horsepower_and_price(data):
    body_style_and_price = data.groupby('horsepower')['price'].mean()
    body_style_and_price.plot.line(x='horsepower', y='price')
    plt.show()
    plt.close()

# get the drivewheel relation to price
def drivewheel_and_price(data):
    makes_avgs = data.groupby('drive-wheels')['price'].mean()
    makes_avgs.plot.bar(x='drive-wheels', y='price')
    plt.show()
    plt.close()

# get the gas vs diesel relation to price
def gas_diesel_price(data):
    makes_avgs = data.groupby('diesel')['price'].mean()
    makes_avgs = makes_avgs.rename({0:'Gasoline', 1:'Diesel'})
    makes_avgs.plot.bar(y='price')
    plt.show()
    plt.close()


if __name__ == '__main__':

    # read dataset from "usedcars_dataset.csv"
    df = pd.read_csv('usedcars_dataset.csv')


    # list of the columns that we want to keep
    keeping = ['make', 'body-style', 'drive-wheels', 'length', 'width',
                'horsepower', 'diesel', 'gas', 'price']
    
    # list of the columns that we want to drop
    dropping = []

    for col in df.columns:
        if  not (col in keeping):
            dropping.append(col)

    data = df.drop(dropping, axis=1)
   
    # clean the data
    data = data.dropna()
    data = data.drop_duplicates()

make_and_price(data)
bodystyle_and_price(data)
length_and_price(data)
width_and_price(data)
drivewheel_and_price(data)
horsepower_and_price(data)
gas_diesel_price(data)