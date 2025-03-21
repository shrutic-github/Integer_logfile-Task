# Task Overview: Log File Data Extraction and Analysis

This document outlines the steps I took to analyze a provided log file, extract structured data, and present it in an organized manner, adhering to the specified task requirements.

## 1. Log File Analysis and Pattern Identification

**Task:** Analyze the provided log file to determine table structures, identify 'START' and 'END' blocks, and determine the number of tables.

**Process:**

* I began by inspecting the provided `log_file.txt` to understand its structure.
* I identified consistent patterns of data enclosed within `START` and `END` markers. Specifically, I observed the format `MAL03377:<TABLE NAME> START` and `MAL03377:<TABLE NAME> END`, which clearly delineated table boundaries.
* By examining the lines following the `START` markers, I was able to determine the column headers for each table, typically separated by semicolons (`;`) or spaces.
* I confirmed that the log file contained **multiple tables**, each with distinct data and column structures.



# Identified Tables and Their Structures

This section details the tables identified within the log file, including their start and end markers, as well as the column headers extracted.

## 1. ALARM STATUS

* **Start Marker:** `MAL03377:ALARM STATUS START`
* **End Marker:** `MAL03377:ALARM STATUS END`
* **Columns:** `Date_Time`, `Severity`, `Object`, `Problem`

## 2. AVG PRB BRANCH RSSI

* **Start Marker:** `MAL03377:AVG PRB BRANCH RSSI START`
* **End Marker:** `MAL03377:AVG PRB BRANCH RSSI END`
* **Columns:** `Cell`, `SECTOR_X_Branch_Y`, `AVG_ULRSSI`, `PRBGroup1-10`, `...`, `PRBGrp90-`

## 3. AVG PER BRANCH RSSI

* **Start Marker:** `MAL03377:AVG PER BRANCH RSSI START`
* **End Marker:** `MAL03377:AVG PER BRANCH RSSI END`
* **Columns:** `CELL`, `SC`, `FRU`, `BOARD`, `PUSCH`, `PUCCH`, `A`, `B`, `C`, `D`, `DELTA`

## 4. RFBRANCH STATUS

* **Start Marker:** `MAL03377:RFBRANCH STATUS START`
* **End Marker:** `MAL03377:RFBRANCH STATUS END`
* **Columns:** `MO`, `auPortRef`, `dlAttenuation`, `dlTrafficDelay`, `reservedBy`, `rfPortRef`, `tmaRef`, `ulAttenuation`, `ulTrafficDelay`

## 5. BASIC DETAIL

* **Start Marker:** `MAL03377:BASIC DETAIL START`
* **End Marker:** `MAL03377:BASIC DETAIL END`
* **Columns:** `Proxy`, `Adm State`, `Op. State`, `MO`

## 6. HARDWARE INVENTORY

* **Start Marker:** `MAL03377:HARDWARE INVENTORY START`
* **End Marker:** `MAL03377:HARDWARE INVENTORY END`
* **Description:** This table contains information about hardware components and connectivity.
* 
## 3. ChatGPT Prompt Engineering

**Task:** Craft effective ChatGPT/Gemini prompts to extract table data.

**Process:**

* I formulated prompts that instructed the AI to identify and isolate data blocks between the `START` and `END` markers.
* I specified the need to extract relevant columns and values from each table, using the previously identified column headers.
* I requested that the output be formatted as structured tables, suitable for direct conversion to Excel.
* I iteratively refined the prompts based on the AI's initial responses, adjusting them to handle variations in data formatting and ensure accurate extraction.

## 4. Data Extraction and Excel Conversion

**Task:** Use ChatGPT/Gemini output to extract table data and save it to an Excel file.

**Process:**

* I used the refined prompts to extract the table data from the log file.
* I processed the AI's output, ensuring that the extracted data was correctly aligned with the identified column headers.
* I saved the extracted tables into an Excel file (`extracted_data.xlsx`), with each table residing on a separate sheet.
* I verified that the Excel file contained correct column headers and properly formatted data, without any missing or misaligned values.
* I used the `xlsxwriter` python library to wrap the long text data for better readability.

## 5. Documentation

**Task:** Document the extraction process in a `README.md` file.

**Process:**

* I created a `README.md` file to thoroughly document the entire extraction process.
* I explained how I identified the `START` and `END` blocks and determined the table structures.
* I listed the number of tables found and their titles.
* I described the logic behind my code(if code was used) or my process to extract data and explained why my approach was effective.
* I detailed the design and refinement of my ChatGPT/Gemini prompts.

  

## 6. GitHub Upload and Submission

**Task:** Upload the project to a public GitHub repository and share the link.

**Process:**

* I created a public GitHub repository.
* I uploaded the following files:
    * `log_file.txt` (the provided log file)
    * `extracted_data.xlsx` (the extracted tables in Excel format)
    * `README.md` (this documentation file)
    * `extraction_script.py` (the python script used to extract the data and format excel file)
* I ensured that the repository was well-organized.
  
