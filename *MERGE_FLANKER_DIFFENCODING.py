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

#
# Set the encoding for each file type
utf8_encoding = "utf-8"
utf16_encoding = "utf-16"

# Set the header row for each file type

utf8_header = ['ExperimentName', 'Subject',	'Session', 'Clock.Information',
               'DataFile.Basename', 'Display.RefreshRate', 'ExperimentVersion',
               'Group', 'RandomSeed', 'RuntimeCapabilities', 'RuntimeVersion',
               'RuntimeVersionExpected', 'SessionDate', 'SessionStartDateTimeUtc',
               'SessionTime', 'StudioVersion',	 'Block', 'GetReady.Duration',
               'GetReady.OffsetDelay',	'GetReady.OnsetDelay',	'GetReady.OnsetTime',
               'Procedure[Block]',	'RunList', 'RunList.Cycle',	 'RunList.Sample',
               'Running[Block]', 'RunNumber', 'Runrest.OffsetTime',
               'Runrest.OnsetTime', 'WaitingForScanner.OffsetTime',
               'Trial', 'Blankwait.OnsetTime',	 'FeedBackBlocks', 'FeedBackBlocks.Cycle'
               'FeedBackBlocks.Sample', 'Procedure[Trial]', 'Running[Trial]',
               'SubTrial',	'ArrowImage',	'CellNumber', 'CorrectAnswer',
               'Direction', 'Feed', 'FixationITI.OffsetDelay',
               'FixationITI.OffsetTime',	'FixationITI.OnsetDelay',
               'FixationITI.OnsetTime',	'FixationITI.TargetOffsetTime',
               'FixationITI.TargetOnsetTime',	'Flanker', 'FlankerImage.ACC',
               'FlankerImage.CRESP	', 'FlankerImage.Duration',
               'FlankerImage.OffsetDelay', 'FlankerImage.OffsetTime',
               'FlankerImage.OnsetDelay',	'FlankerImage.OnsetTime	',
               'FlankerImage.RESP',	'FlankerImage.RT',	'FlankerImage.RTTime',
               'FlankerImage.Tag', 'FlankerImage.TargetOffsetTime',
               'FlankerImage.TargetOnsetTime',	 'ITI',	'ITILIST', 'Procedure[SubTrial]',
               'RespType',	'RespWindow.Duration',	'RespWindow.OffsetDelay',
               'RespWindow.OffsetTime', 'RespWindow.OnsetDelay',
               'RespWindow.OnsetTime',	'RespWindow.TargetOffsetTime',
               'RespWindow.TargetOnsetTime', 'Running[SubTrial]',	'TotN',
               'TrialList',	'TrialList.Cycle',	'TrialList.Sample',
               'TrialNumber',	'TrialType']

utf16_header = ['ExperimentName', 'Subject',	'Session', 'Clock.Information',
                'DataFile.Basename', 'Display.RefreshRate', 'ExperimentVersion',
                'Group', 'RandomSeed', 'RuntimeCapabilities', 'RuntimeVersion',
                'RuntimeVersionExpected', 'SessionDate', 'SessionStartDateTimeUtc',
                'SessionTime', 'StudioVersion',	 'Block', 'GetReady.Duration',
                'GetReady.OffsetDelay',	'GetReady.OnsetDelay',	'GetReady.OnsetTime',
                'Procedure[Block]',	'RunList', 'RunList.Cycle',	 'RunList.Sample',
                'Running[Block]', 'RunNumber', 'Runrest.OffsetTime',
                'Runrest.OnsetTime', 'WaitingForScanner.OffsetTime',
                'Trial', 'Blankwait.OnsetTime',	 'FeedBackBlocks', 'FeedBackBlocks.Cycle'
                'FeedBackBlocks.Sample', 'Procedure[Trial]', 'Running[Trial]',
                'SubTrial',	'ArrowImage',	'CellNumber', 'CorrectAnswer',
                'Direction', 'Feed', 'FixationITI.OffsetDelay',
                'FixationITI.OffsetTime',	'FixationITI.OnsetDelay',
                'FixationITI.OnsetTime',	'FixationITI.TargetOffsetTime',
                'FixationITI.TargetOnsetTime',	'Flanker', 'FlankerImage.ACC',
                'FlankerImage.CRESP	', 'FlankerImage.Duration',
                'FlankerImage.OffsetDelay', 'FlankerImage.OffsetTime',
                'FlankerImage.OnsetDelay',	'FlankerImage.OnsetTime	',
                'FlankerImage.RESP',	'FlankerImage.RT',	'FlankerImage.RTTime',
                'FlankerImage.Tag', 'FlankerImage.TargetOffsetTime',
                'FlankerImage.TargetOnsetTime',	 'ITI',	'ITILIST', 'Procedure[SubTrial]',
                'RespType',	'RespWindow.Duration',	'RespWindow.OffsetDelay',
                'RespWindow.OffsetTime', 'RespWindow.OnsetDelay',
                'RespWindow.OnsetTime',	'RespWindow.TargetOffsetTime',
                'RespWindow.TargetOnsetTime', 'Running[SubTrial]', 'TotN',
                'TrialList',	'TrialList.Cycle',	'TrialList.Sample',
                'TrialNumber',	'TrialType']

# Set the output file name and encoding
output_file = "combined_file_new.txt"
output_encoding = "utf-8"
# Create an empty list to hold the data
data = []
# Get a list of file names with full path that match the pattern "*.txt"
files = glob.glob(path + "/*.txt")

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
            # Check if the header row has already been added
        if ''.join(utf16_header) in decoded_text and ''.join(utf16_header) not in data:
            data.append(list(utf16_header))
        elif ''.join(utf8_header) in decoded_text and ''.join(utf8_header) not in data:
            data.append(list(utf8_header))
            # Append the remaining lines to the data list
            data.extend(line.strip()
                        for line in decoded_text.split('\n') if line.strip())


# Write the combined data to the output file
if data:
    with codecs.open(output_file, "w", encoding=output_encoding) as f:
        for line in data:
            f.write("\n".join(line) + "\n")


with open('output.txt', 'w') as outfile:
    # Read the header from the first file
    with open('/Users/khosravip2/Downloads/flanker_data/combined_file_2.txt', 'r') as f:
        header = f.readline().strip()

    # Write the header to the output file
    outfile.write(header + '\n')

    # Append the contents of the first file to the output file
    with open('/Users/khosravip2/Downloads/flanker_data/combined_file_2.txt', 'r') as f:
        next(f)  # skip the header
        for line in f:
            outfile.write(line)

    # Append the contents of the second file to the output file, skipping the header
    with open('/Users/khosravip2/Downloads/flanker_data/combined_file_new.txt', 'r') as f:
        next(f)  # skip the header
        for line in f:
            outfile.write(line)
