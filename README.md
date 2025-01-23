# encoded_csv_combine
## Overview
This Python script processes and combines multiple text files containing data from Flanker tasks. The script handles files with different encodings (UTF-8, UTF-16 LE, and UTF-16 BE) and combines them into a single output file. It ensures that data headers are correctly identified and avoids duplication during the merge process. Additionally, the script appends combined results into a final output file.
<p></p>

*The script requires the following Python libraries:*

`os`
`codecs`
`pandas`
`glob`

## File Structure
Make sure your directory contains input text files for Flanker task data in various encodings (e.g., UTF-8, UTF-16).

## How to Use
1. Clone the Repository: `git clone <repository-url>`
`cd <repository-directory>`
2. Set Up Input Files: Place your input text files in the specified directory
3. Run the Script: open the script in Spyder and run the script
