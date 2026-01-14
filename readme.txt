# HIT137 Group Assignment 2

This repository contains three Python-based projects developed collaboratively by a team of four members. The projects demonstrate practical applications in text encryption/decryption, data analysis, and graphical pattern generation.

## Project Overview
The assignment consists of three questions, each implemented in Python as detailed below.

### Question 1: Text Encryption and Decryption
This program reads the contents of "raw_text.txt", applies a custom encryption algorithm based on user-provided shift values (shift1 and shift2), and writes the encrypted output to "encrypted_text.txt". The encryption rules differentiate between lowercase and uppercase letters, with specific shift calculations for each half of the alphabet. Non-alphabetic characters remain unchanged. A decryption function reverses the process, writing to "decrypted_text.txt", and a verification function compares the original and decrypted files to confirm accuracy. Upon execution, the program prompts for shift values, performs encryption and decryption, and verifies the results.

### Question 2: Temperature Data Analysis
This program processes temperature data from multiple CSV files in the "temperatures" folder, each representing one year of data from Australian weather stations. Missing values (NaN) are ignored in calculations. Key functionalities include:
- Computing average temperatures for each Australian season (Summer: Dec-Feb, Autumn: Mar-May, Winter: Jun-Aug, Spring: Sep-Nov) across all stations and years, with results saved to "average_temp.txt".
- Identifying station(s) with the largest temperature range (maximum minus minimum), with output saved to "largest_temp_range_station.txt". Multiple stations are listed in case of ties.
- Determining station(s) with the most stable temperatures (smallest standard deviation) and most variable temperatures (largest standard deviation), with results saved to "temperature_stability_stations.txt". Ties are handled by listing all relevant stations.

The implementation utilizes libraries such as pandas for efficient data handling.

### Question 3: Geometric Pattern Generation with Turtle Graphics
This program uses Python's turtle module to generate a recursive geometric pattern starting from a regular polygon. The pattern applies indentation rules to each edge: dividing it into three segments, replacing the middle with an inward-pointing equilateral triangle, and recursing to the specified depth. The program prompts the user for the number of sides, side length (in pixels), and recursion depth. For example, inputs of 4 sides, 300 pixels, and depth 3 produce an intricate design.

## Contributors
- Fuad Ahmed Ananta - S399378
- Prabesh Tamang - S398925
- Pramisha Shrestha - S399137
- Sushil Dhungana- S399406

## Setup and Execution
1. Clone the repository: git clone [repository-url]
2. Ensure Python 3.x is installed, along with required libraries (e.g., pandas, numpy, turtle). Install via pip if necessary: pip install pandas numpy turtle .
3. Extract "assignment2.zip" to access input files such as "raw_text.txt" and the "temperatures" folder.
4. Execute Question 1: Run the corresponding script `question1.py` and provide shift values when prompted.
5. Execute Question 2: Run the script `question2.py` to process CSVs and generate output files.
6. Execute Question 3: Run the script `question3.py` and enter the prompted values to display the pattern.

Generated files will be created in the repository directory. Verify file paths if issues arise.

## Additional Notes
- The repository is public as per assignment requirements.
- All code is original and adheres to the provided guidelines.
- This repository may serve as a reference, but users are encouraged to develop their own solutions. 

For any inquiries, please open an issue in the repository.