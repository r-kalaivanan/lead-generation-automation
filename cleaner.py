import pandas as pd

def generate_email(name):
    if name and name != "N/A":
        domain = name.lower().replace(" ", "") + ".com"
        return f"contact@{domain}"
    return "N/A"

def clean_data(data):
    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Drop duplicate entries based on Name + Website
    df = df.drop_duplicates(subset=["Name", "Website"])

    # Handle missing values
    df = df.fillna("N/A")

    # Clean text fields
    df["Name"] = df["Name"].astype(str).str.strip()
    df["Location"] = df["Location"].astype(str).str.strip()
    df["Website"] = df["Website"].astype(str).str.strip()

    df["Name"] = df["Name"].str.title()
    df = df[df["Name"] != "N/A"]
    df = df.reset_index(drop=True)
    
    df["Email"] = df["Name"].apply(generate_email)
    return df