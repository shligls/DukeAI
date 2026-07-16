import pandas as pd # libary for data analysis which is shorthanded to pd
import matplotlib.pyplot as plt # libary for data visualization which is shorthanded to plt
import seaborn as sns # libary for data visualization which is shorthanded to sns
from matplotlib.backends.backend_pdf import PdfPages # libary for creating multi-page PDF files shorthanded to PdfPages

# Load the CSV file into a DataFrame. The 'keep_default_na=False' argument keeps empty strings as empty strings instead of converting them to NaN.
df = pd.read_csv("train.csv", keep_default_na=False)  

# Identify the columns (features vs. target price)
all_columns = df.columns    # decoupling the columns from the DataFrame making the code more memory effieceint
feature_columns = all_columns[:-1]  # All columns except the last one
price_column = all_columns[-1]       # The very last column (Price)

# Create a multi-page PDF file
with PdfPages("housing_analysis.pdf") as pdf:
    
    # Loop through each factor and generate a scatter plot
    for factor in feature_columns:
        
        # Create a new figure for each page in the PDF
        plt.figure(figsize=(8, 6))
        
        # Draw the scatter plot
        plt.scatter(df[factor], df[price_column], alpha=0.6, color="blue")
        
        # Add title, axis labels, and a grid
        plt.title(f"House Price vs {factor}", fontsize=14, fontweight="bold")
        plt.xlabel(factor, fontsize=12)
        plt.ylabel(price_column, fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.5)
        
        # Adjust layout so labels don't get cut off
        plt.tight_layout()
        
        # Save the current figure as a new page in the PDF
        pdf.savefig()
        
        # Clear the memory by closing the figure
        plt.close()

print("PDF report 'housing_analysis.pdf' generated successfully!")