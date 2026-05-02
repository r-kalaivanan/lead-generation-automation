from scraper import fetch_companies

if __name__ == "__main__":
    data = fetch_companies()

    print(f"Total companies scraped: {len(data)}")

    for d in data[:5]:
        print(d)