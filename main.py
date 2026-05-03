from scraper import fetch_companies
from cleaner import clean_data

def main():
    print("🔄 Starting lead generation process...\n")

    # Fetch raw data
    raw_data = fetch_companies()
    print(f"Raw data collected: {len(raw_data)} records")

    # Clean data
    cleaned_df = clean_data(raw_data)
    print(f"Cleaned data: {len(cleaned_df)} records\n")

    # Preview output
    print("Sample cleaned data:")
    print(cleaned_df.head())

    return cleaned_df


if __name__ == "__main__":
    main()