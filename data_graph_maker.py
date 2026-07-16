import pandas as pd # libary for data analysis which is shorthanded to pd
import matplotlib.pyplot as plt # libary for data visualization which is shorthanded to plt
import seaborn as sns # libary for data visualization which is shorthanded to sns
from matplotlib.backends.backend_pdf import PdfPages # libary for creating multi-page PDF files shorthanded to PdfPages

# Load the CSV file into a DataFrame. The 'keep_default_na=False' argument keeps empty strings as empty strings instead of converting them to NaN.
df = pd.read_csv("train.csv", keep_default_na=False)  

# creating a list that will hold the price column
price_column = df.columns[-1]       # The very last column (Price)
df[price_column] = pd.to_numeric(df[price_column], errors='coerce') # Convert the price column to numeric and non numbers to NaN

# Create a multi-page PDF file
with PdfPages("housing_price_vs_features_analysis.pdf") as pdf:
    
    # Loop through each column and generate a scatter plot
    for col in df.columns[:-1]:
        
        # Create a new figure for each page in the PDF
        plt.figure(figsize=(10, 6))
        
        # Conditional that tells if the data from the column is numeric or not
        if pd.api.types.is_numeric_dtype(df[col]):
            # adding a line of best fit when the column is numeric
            sns.regplot(data=df, x=col, y=price_column, 
                        scatter_kws={'alpha':0.4, 'color':'blue'},  # Settings for  the scatter points
                        line_kws={'color':'red', 'linewidth':2})    # Settings for the line of best fit
            
            # Correlation coefficient (r) calculation
            correlation = df[col].corr(df[price_column])
            
            # Title for numerical graphs
            plt.title(f"House Price vs {col}\nCorrelation: {correlation}", fontsize=12, fontweight="bold")
            
        else:
            # For non-numaric columns a box plot is used
            sns.boxplot(data=df, x=col, y=price_column, palette="Set2") # Creates a box plot
            plt.xticks(rotation=45, ha="right") # Making x values more readable
            
            # Title for non-numerical graphs
            plt.title(f"House Price vs {col}", fontsize=12, fontweight="bold")  # Adding a title to each graph
            
            
        
        
        # # Draw the scatter plot
        # plt.scatter(df[factor], df[price_column], alpha=0.6, color="blue")
        
        # # Add title, axis labels, and a grid
        # plt.title(f"House Price vs {factor}", fontsize=14, fontweight="bold")
        # plt.xlabel(factor, fontsize=12)
        # plt.ylabel(price_column, fontsize=12)
        # plt.grid(True, linestyle="--", alpha=0.5)
        
        # Adjust layout so labels don't get cut off
        plt.tight_layout()
        
        # Save the current figure as a new page in the PDF
        pdf.savefig()
        
        # Clear the memory by closing the figure
        plt.close()

print("pdf 'housing_price_vs_features_analysis.pdf' generated successfully.")