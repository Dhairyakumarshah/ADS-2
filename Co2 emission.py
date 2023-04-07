import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def read_world_bank_data(filename):
    # Read data from file
    df = pd.read_csv(filename)
    
    # Strip leading and trailing spaces from column names
    df.columns = [col.strip() for col in df.columns]
    
    # Set 'Years' column as the index
    df.set_index('Years', inplace=True)
    
    # Clean dataframe
    df.replace(to_replace='..', value=np.nan, inplace=True)
    
    # Transpose dataframe and clean again
    df_t = df.T
    df_t.replace(to_replace='..', value=np.nan, inplace=True)
    
    # Convert column names to integer type
    df_t.columns = df_t.columns.astype(int)
    
    # Get dataframes for years and countries
    df_years = df_t.loc[:, 2010:2015]
    df_countries = df_t.drop(columns=df_years.columns)
    
    return df_years, df_countries

# Example usage of the function
df_years, df_countries = read_world_bank_data("D:\Assignments ADS\ADS 2\second graph\gdp growth per capita.csv")

plt.figure(figsize=(10, 6))
sns.set_style('whitegrid')
ax = df_years.plot(kind='bar', width=0.8, color=['#008fd5', '#fc4f30', '#e5ae37', '#6d904f', '#8b8b8b', '#fc4f30'])
ax.set_xlabel('Countries', fontsize=12,color='Blue')
ax.set_ylabel('gdp growth', fontsize=12, color='red')
ax.set_title('gdp growth per capita(2010-2014)', fontsize=14,fontweight ='bold')
plt.legend(fontsize=5)

plt.show()

