import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def make_and_price(data):
    """
   get every brand and its avg price and plot the relation between them as a bar graph.
  
    Parameters:
    data (pandas.DataFrame): a DataFrame containing the data after it has been cleaned.
  
    Returns:
    None
  
    """
    makes_avgs = data.groupby('make')['price'].mean()
    makes_avgs.plot.bar(x='make', y='price')
    plt.show()
    plt.close()


def bodystyle_and_price(data):
    """
   get every body style and its avg price and plot the relation between them as a bar graph.
  
    Parameters:
    data (pandas.DataFrame): a DataFrame containing the data after it has been cleaned.
  
    Returns:
    None
  
    """
    body_style_and_price = data.groupby("body-style")['price'].mean()
    body_style_and_price.plot.bar(x='body-style', y='price')
    plt.show()
    plt.close()


def length_and_price(data):
    """
   get the length relation to price and plot it as a line graph.
  
    Parameters:
    data (pandas.DataFrame): a DataFrame containing the data after it has been cleaned.
  
    Returns:
    None
  
    """
    body_style_and_price = data.groupby('length')['price'].mean()
    body_style_and_price.plot.line(x='length', y='price')
    plt.show()
    plt.close()


def width_and_price(data):
    """
  get the width relation to price and plot it as a line graph.
  
    Parameters:
    data (pandas.DataFrame): a DataFrame containing the data after it has been cleaned.
  
    Returns:
    None
  
    """
    body_style_and_price = data.groupby('width')['price'].mean()
    body_style_and_price.plot.line(x='width', y='price')
    plt.show()
    plt.close()


def horsepower_and_price(data):
    """
   get the horsepower relation to price and plot it as a line graph.
  
    Parameters:
    data (pandas.DataFrame): a DataFrame containing the data after it has been cleaned.
  
    Returns:
    None
  
    """
    body_style_and_price = data.groupby('horsepower')['price'].mean()
    body_style_and_price.plot.line(x='horsepower', y='price')
    plt.show()
    plt.close()


def drivewheel_and_price(data):
    """
   get every drive wheel type and its avg price and plot the relation between them as a bar graph.
  
    Parameters:
    data (pandas.DataFrame): a DataFrame containing the data after it has been cleaned.
  
    Returns:
    None
  
    """
    makes_avgs = data.groupby('drive-wheels')['price'].mean()
    makes_avgs.plot.bar(x='drive-wheels', y='price')
    plt.show()
    plt.close()


def gas_diesel_price(data):
    """
   get diesel and gasoline fuel types and their avg price and plot the relation between them as a bar graph.
  
    Parameters:
    data (pandas.DataFrame): a DataFrame containing the data after it has been cleaned.
  
    Returns:
    None
  
    """
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