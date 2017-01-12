#!/bin/bash
echo  "Medical Data ProProcess"     
echo  "By LanqingYang,2016-12-25 To 2017-01-03"   
echo  "Start..."        
echo  "Now Correcting the wrong data"  
iconv -f GBK -t utf-16LE ../DATA/2015-3-16--修改.csv > ../DATA/tmp.csv
iconv -f utf-16LE -t utf-8 ../DATA/tmp.csv  > ../DATA/2015-3-16--修改.csv
rmr ../DATA/tmp.csv
python process_false_data.py 1
echo  "Correct_data Finished"       
echo  "Converting and Getting useful data"   
python trans_time.py 1
echo  "Convert_info finished"     
echo  "Start Feather Extraction"
#octave Test.m
#octave FeatherExtraction.m
python Trial.py 1
pause