import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd

# 1. Initialize the multi-page PDF file
with PdfPages('multipage_plots.pdf') as pdf:
    
    # opens the file as a DataFrame organizing it into rows and columnns
    df = pd.read_csv('train.csv')
    
    # Loop to generate a list for every column (-1 because the last column is the label column)
    for i in range(len(df.columns)-1): 
        # 2. Always create a fresh figure instance
        fig, ax = plt.subplots(figsize=(8, 6))
        
#         # Generate dummy data and plot
#         x = df[df.columns[i]]
#         y = df[df.columns[-1]]  # Use the last column as y-values
#         ax.plot(x, y, label=f'Wave {i}')
#         ax.set_title(f'Graph Page {i+1}')
#         ax.legend()
        
#         # 3. Save the current figure to the PDF file
#         # 'bbox_inches="tight"' ensures labels don't get cut off
#         pdf.savefig(fig, bbox_inches='tight')
        
#         # 4. CRITICAL: Explicitly close the figure to free RAM
#         plt.close(fig)

# print("PDF exported successfully!")
