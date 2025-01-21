import pandas as pd

def process_sales_data(filepath):
    """
    Reads sales data from a CSV file and calculates total sales.
    """
    try:
        data = pd.read_csv(filepath)
        total_sales = data['sales_amount'].sum()
        print(f"Data loaded successfully. Total sales: ${total_sales:.2f}")
    except FileNotFoundError:
        print("File not found. Please check the filepath and try again.")
    except KeyError:
        print("The expected 'sales_amount' column is missing in the data.")

def main():
    """
    Main function to run our sales metrics calculations.
    """
    filepath = 'daily_sales.csv'  # Path to your sales data file
    process_sales_data(filepath)

if __name__ == '__main__':
    main()
