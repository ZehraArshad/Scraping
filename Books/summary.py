import re

def generate_data_summary(df):
   
    print("\nData Summary")
    print("-" * 30)

    print(f"Total books scraped: {len(df)}")

    available = df['Availability'].str.contains("In stock").sum()
    print(f"Available: {available}")
    print(f"Unavailable: {len(df) - available}")

    print("\nStar Rating Distribution:")
    print(df['Star Rating'].value_counts())

    df['Price Num'] = df['Price'].apply(lambda x: float(re.sub(r'[^\d.]', '', x)))
    print(f"\nAverage book price: £{df['Price Num'].mean():.2f}")
