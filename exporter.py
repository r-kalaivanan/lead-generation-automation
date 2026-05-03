def export_to_excel(df, filename="leads.xlsx"):
    try:
        df.to_excel(filename, index=False)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print("Error exporting file:", e)