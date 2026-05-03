# Lead Generation Automation

## Overview

This project automates lead generation by scraping company data from a public source and organizing it into a structured format for easy use.

## Features

- Web scraping using Selenium (handles dynamic content)
- Data cleaning and preprocessing using Pandas
- Duplicate removal and missing value handling
- Email generation for leads (simulated)
- Export to Excel with timestamped filenames
- Optional scheduling automation for periodic execution

## Tech Stack

- Python
- Selenium
- Pandas
- OpenPyXL
- Schedule (for automation)

## How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/lead-generation-automation.git
cd lead-generation-automation
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the script:

```
python main.py
```

## Output

- Generates an Excel file with cleaned lead data
- Filename includes timestamp for automation use

## Bonus Features

- Email generation for each lead
- Scheduling automation using Python's schedule library

## Future Improvements

- Integration with Google Sheets API
- Real email extraction using APIs
- Advanced data validation

---

This project demonstrates automation, data handling, and practical problem-solving skills.
