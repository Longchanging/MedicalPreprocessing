# MedicalPreprocessing
Store scripts used for medical csv table analysis
--------------------------------------------------------------------------------------------------
##  Scripts for Data Preprocessing and Feather Extraction                                   
##  2017/1/4,By LanqingYang,STJU,Mapleylq@gmail.com
--------------------------------------------------------------------------------------------------

####  Main Function

  ·This folder used for processing original data and get useful feathers.

#Environment:

  ·Windows2007,x64bit
  ·Python 2.7.10
  ·Octave 3.6.4

#Necessary settings before start:

  ·Please ensure the original data written in UTF8 with BOM
      To satisfy this requirment,you can save the input csv file with"save as utf8" in windows 
      Sorry,but now i cannot conquer it.

  ·Please install octave and add the path of BAT file in its environment.
      You can use addpath in Octave.

   And also it's disgusting that it cannot  run all automatically,but it may come true in the future.
  ·If you want to run your file ,you should replace the CSV file in DATA path with your file .
      And then,i am sorry to say that you should also change the code :)


--------------------------------------------------------------------------------------------------

##Useage of the folder:
  ·After finishing the environment issue,you can just double click the BAT file.

--------------------------------------------------------------------------------------------------

##Description of Process Scripts:
  ·"start.bat"
    The executable file.You can excute the scripts just with it.  
    [Input]
        input_dir = "../DATA/"
        input_filename  = filename
    [Output]
        output_dir= "../DATA/Processing/"
        output_filename="Extracted_feather_" + file_name

  ."process_false_data.py"
    It deals with originally false columns and some missing UserID rows.
    [Input]
        input_dir = "../DATA/"
        input_filename  = filename
    [Output]
        output_dir= "../DATA/Processing/"
        output_filename="FalseCorrected_" + file_name

  ."trans_time.py"
    It digests useful information with right time and  numeric data transformed from various characters.
    [Input]
        input_dir = "../DATA/Processing/"
        input_filename  = "FalseCorrected_" + file_name
    [Output]
        output_dir= "../DATA/Processing/"
        output_filename="TimeTransformed_" + file_name

  ."Trial.py"
    It provides a bridge to excute file "FeatherDigest.m".
    It is realized by means of Oct2py(in Python) and Octave.

  ·"FeatherDigest.m"
    It generates feathers that can be used for Machine Learning from transformed information.
    [Input]
        input_dir = "../DATA/Processing/"
        input_filename  = "TimeTransformed_" + file_name
    [Output]
        output_dir= "../DATA/Processing/"
        output_filename="Extracted_feather_" + file_name

--------------------------------------------------------------------------------------------------

##OutputFiles:
  ·After running the BAT，3 CSV files generated in folder '/DATA/Processing'.
   The following is a brief description of these 3 files:

  ."FalseCorrected_ + filename"
   It stores preprocessed data with originally false columns corrected and some missing UserID filled.

  ."TimeTransformed_ + filename"
   It stores useful information with right time and  numeric data transformed from characters.

  ."Extracted_feather_ + filename"
   It stores feathers that can be used for MachileLearning generated from transformed information.
   This file can be used directly in Weka as CSV source file.

##Others:
  ·"Pay attention to the encoding,my child!"(Just adapted from a novel of my favorite science fiction writer ,CixinLiu) 
  ·It is just a homework for me,so there must be many bugs inside.It will be my great honor if you can report it to me.Thanks!
