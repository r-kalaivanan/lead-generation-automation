from datetime import datetime

def export_to_excel(df):
    try:
        filename = f"leads_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        df.to_excel(filename, index=False)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print("Error exporting file:", e)