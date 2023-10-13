# Bulk Save - Contact VCF Generator

Bulk Save is a Python application that allows you to quickly convert a CSV file containing contact information into a VCF (Virtual Contact File) format, which is commonly used for importing contacts into various devices and applications. This tool simplifies the process of creating VCF files for multiple contacts at once.

## Features

- **CSV to VCF Conversion:** Bulk Save takes a CSV file as input and converts the data into a VCF format, making it easy to import contacts into your phone, tablet, or other contact management tools.

- **Customizable Suffix:** You can specify a suffix (e.g., your college name or abbreviation) that will be added to the contact names in the generated VCF files. This feature is useful for categorizing or identifying contacts.

- **User-Friendly UI:** The application provides a simple and user-friendly graphical user interface (GUI) to input the CSV file path and suffix. This makes it accessible to users with little programming experience.

## Prerequisites

Before using Bulk Save, you'll need the following:

- Python: The application is written in Python, so make sure you have Python 3 installed.

- Required Python Packages: Install the necessary Python packages using pip. You can do this by running the following command:

```bash
pip install pandas tkinter
```

## Getting Started

1. **Clone the Repository:** Start by cloning the Bulk Save repository to your local machine using Git. Open your command line or terminal and run the following command:

```bash
git clone https://github.com/your-username/bulk-save.git
```

2. **Run the Application:** Navigate to the project directory and run the Python script:

```bash
cd bulk-save
python bulk_save.py
```

3. **Using the Application:**
   - In the GUI, input the full path of the CSV file (including the filename and extension).
   - Enter the desired suffix (e.g., your college name abbreviation).
   - Click the "Submit" button to initiate the conversion process.

4. **Output File:** The VCF file will be generated in the 'D' drive as 'numbers.vcf'. You can collect the output from there and use it for importing contacts.

## Notes

- It's important to ensure that the input CSV file is accurate for efficient results.
- The application provides instructions and guidance for usage through message boxes in the GUI.

*Created by [Srihari M](https://github.com/SrihariMurali01/Bulk-Save_Colleges)*
