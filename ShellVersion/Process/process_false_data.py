#coding:utf-8
#20161229,by LanqingYang
#Func: process_false_data,preprocess medical data
# coding: UTF-8
import re
import os
import csv
import io
import codecs
from time import clock
from subprocess import call

M = 40

def remove_uni(s):
    s2 = ''
    #print "in"
    if s.startswith("'"):
        s2 = s.replace("'", "", 1)
        s2 = s2.replace("'", "", 1)
    elif s.startswith('"'):
        s2 = s.replace('"', '', 1)
        s2 = s2.replace('"', '', 1)
    return s2

def process_false_data(file_name,input_dir,output_dir):
    circle_control = 1
    file_read =  input_dir  + file_name
    file_write = output_dir  + "FalseCorrected_" + file_name 
    f2read1 = open(file_read,'rU')
    f2read = csv.reader(f2read1, delimiter=',', quotechar='|')
    if os.path.exists(file_write):
        os.remove(file_write) 
    f2write = open(file_write, 'w')
    prior_user = 1
    cnt_into = 1
    for line in f2read:
        line = ','.join(line)
        circle_control=circle_control+1
        reDiv=re.compile(r'[,]')
        Components=reDiv.split(line)
        User = Components[2]
        m = re.match(r'(\d+)/(\d+)/(\d+)', User)
        
        if m:
            if cnt_into % M == 1 :
                User = str( int(prior_user) + 1 )
            else:
                User = prior_user
            cnt_into = cnt_into + 1
            Real_data = [Components[0],Components[1],User,Components[2],Components[3],Components[4],Components[5],Components[6],Components[7],Components[8],Components[9],Components[10],Components[11]]
        else:
            cnt_into = 1
            Real_data = Components
        prior_user=User
        
        for item in Real_data:
            f2write.writelines(item)
            f2write.write(",")
        f2write.write("\n")
            
    f2write.close()
   
def main():

    start=clock()

    #call('iconv -f GBK -t utf-16LE ../DATA/2015-3-16--修改.csv > ../DATA/fix.csv', shell=True)
    #call('iconv -f utf-16LE -t utf-8 ../DATA/fix.csv  > ../DATA/fixed.csv', shell=True)
    file_half_name = u"2015-3-16--修改.csv"
    input_dir = "../DATA/"
    output_dir= "../DATA/Processing/"
    process_false_data(file_half_name,input_dir,output_dir)

    finish=clock()
    print "#####Total Time Cost:  %s second #####"%(finish-start)
    return

if __name__ == "__main__":
    main()
