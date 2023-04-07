

import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Set the "Years" column as the index
    df.set_index("Years", inplace=True)

    # Create a DataFrame with the desired columns
    df_countries = df[['China', 'Austria', 'Barbados', 'Chile', 'Ghana', 'Italy']]

    return df, df_countries

# Call the function to read the data and get the two dataframes
df, df_countries = read_data("D:/lab/forest.csv")

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the title and axis labels
ax.set_title('forest land as Percentage of Land Area 2010-2020',color = "black",fontweight ='bold')
ax.set_xlabel('Years',fontweight ='bold')
ax.set_ylabel('Percentage',fontweight ='bold')

# Plot each country as a line with a different color
for country in df_countries.columns:
    ax.plot(df.index, df_countries[country], linestyle='--', marker='o', label=country)

# Add a legend
ax.legend(fontsize=9)

# Display the graph
plt.show()
