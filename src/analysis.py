import matplotlib.pyplot as plt

def plot_trends(df):
    plt.figure(figsize=(10,5))
    
    # Temperature Line
    plt.plot(df['Year'], df['Temperature'], marker='o', label='Temperature')
    
    # Rainfall Bar
    plt.bar(df['Year'], df['Rainfall'], alpha=0.5, label='Rainfall')
    
    plt.legend()
    plt.title("Climate Trend Analysis")
    
    plt.savefig('outputs/trend.png')
    plt.show()