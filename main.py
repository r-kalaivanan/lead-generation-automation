from scraper import fetch_companies
from cleaner import clean_data
from exporter import export_to_excel

def main():
    print("Starting lead generation process...\n")

    # Fetch raw data
    raw_data = fetch_companies()
    print(f"Raw data collected: {len(raw_data)} records")

    # Clean data
    cleaned_df = clean_data(raw_data)
    print(f"Cleaned data: {len(cleaned_df)} records\n")

    # Preview
    print("Sample cleaned data:")
    print(cleaned_df.head())

    # Export to Excel
    export_to_excel(cleaned_df)

    print("\nProcess completed successfully!")

if __name__ == "__main__":
    main()