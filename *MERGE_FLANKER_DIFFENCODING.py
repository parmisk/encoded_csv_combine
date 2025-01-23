#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:00:47 2023

@author: khosravip2
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:48:01 2023

@author: khosravip2
"""


# Set the path to the directory containing the text files
import os
import codecs
import pandas as pd
import glob

path = '/Users/khosravip2/Downloads/flanker_data/NEW/'

# Set the output file name and encoding
output_file = "combined_file_new.txt"
output_encoding = "utf-8"
# Create an empty list to hold the data
data = []
# Get a list of file names with full path that match the pattern "*.txt"
files = glob.glob(path + "/*.txt")

header_added = False # flag to check if the header has been added

# Loop through each file in the directory
for filename in files:
    # Open the file in binary mode and read the contents
    with open(filename, "rb") as f:
        contents = f.read()
        # Check if the file is encoded in UTF-16 with a BOM
        if contents.startswith(codecs.BOM_UTF16_LE):
            # Decode the contents with UTF-16 Little Endian encoding
            decoded_text = contents.decode("utf-16-le")
        elif contents.startswith(codecs.BOM_UTF16_BE):
            # Decode the contents with UTF-16 Big Endian encoding
            decoded_text = contents.decode("utf-16-be")
        else:
            # Assume the file is encoded in UTF-8
            decoded_text = contents.decode("utf-8")
        
      # Split the file content into lines
        lines = decoded_text.split('\n')
      
      # Extract the header dynamically from the first file
        if not header_added:
            header = lines[0].strip()  # Take the first line as the header
            data.append(header)
            header_added = True
        
        # Append the rest of the data, skipping the header
        data.extend(line.strip() for line in lines[1:] if line.strip())

# Write the combined data to the output file
if data:
    with codecs.open(output_file, "w", encoding=output_encoding) as f:
        for line in data:
            f.write("\n".join(line) + "\n")

print(f"Data combined and saved to {output_file}")


