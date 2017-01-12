# coding: UTF-8
import re
import os
import io
from time import clock
from subprocess import call
#Used for pre-processing
#By LanqingYang,20161229

def remove_uni(s):
    s2 = ''
    #print "in"
    if s.startswith("u'"):
        s2 = s.replace("u'", "", 1)
        s2 = s2.replace("'", "", 1)
    elif s.startswith('u"'):
        s2 = s.replace('u"', '', 1)
        s2 = s2.replace('"', '', 1)
    return s2

def trans_time(file_half_name,input_dir,output_dir):
    file_read = input_dir  + "FalseCorrected_" + file_half_name 
    file_write = output_dir  + "TimeTransformed_" + file_half_name 
    f2read = io.open(file_read, "r", encoding="utf-8") 
    if os.path.exists(file_write):
        os.remove(file_write) 
    f2write = open(file_write, 'a')
    true_data = []
    loop_num = 1
    loop_num1 = 1
    loop_num2 = 1
    prior_string_list = []
    prior_string_list1 = []
    prior_string_list2 = []
    count_match_num = 0
    count_match_num2= 0
    count_match_num3 = 0
    count_m8_match = 0
    count_m3_match = 0
    
    #Strip used for delete \n,always with split,on a string
    #Now here clear all related data
    for line in f2read:
        #print line
        line = line.strip()
        reDiv=re.compile(r'[,]')
        Components=reDiv.split(line)
       
        userid = Components[2]
        disease = Components[4]
        examination_class=Components[5]
        examination_item=Components[6]
        examination_item_result=Components[7]
        examination_item_discription=Components[9]
        examination_item_judgement=Components[10]
        org_time = Components[11]
        register_num=Components[12]
        
        (temp,loop_num) = column_classify(examination_item,prior_string_list,loop_num)
        examination_item = str(temp)
             
        (temp,loop_num1) = column_classify(disease,prior_string_list1,loop_num1)
        disease = str(temp)
        
        (temp,loop_num2) = column_classify(examination_item_judgement,prior_string_list2,loop_num2)
        examination_item_judgement = str(temp)
           
        m0 = re.match((r'\[(\d+.?\d*)\+?\]'), examination_item_result)
        if   m0 :
            examination_item_result =m0.group(1)

        m1 = re.match((r'(\d+\.?\d*)\+'), examination_item_result)
        m2 = re.match(r'<(\d+\.?\d*)', examination_item_result)
        m4 = re.match(r'(\d+\.?\d*)\s?-\s?(\d+\.?\d*)', examination_item_result)
        m5 = re.match(r'\W*(\d+\.?\d*)\s?:\s?(\d+\.?\d*)\W*', examination_item_result)
        m5_1 = re.match(r'\W*(\d+\.?\d*)\s?：\s?(\d+\.?\d*)\W*', examination_item_result)
        m6 = re.match(r'>(\d+\.?\d*)', examination_item_result)
        m7 = re.match(r'%', examination_item_result)
        re_info8 = r'\d+\\u6708\d+\\u65e5'
        examination_item_result = repr(examination_item_result)
        m81 = re.findall(re_info8, examination_item_result)
        m9 = re.match(r'\W*\(?\+?\)?\W*', examination_item_result)
        re_info3 = r'\\u3008(\d+\.?\d*)'
        m31 = re.findall(re_info3, examination_item_result)
        re_info = r"\\u9634\\u6027\s*"
        m9_21 = re.findall(re_info, examination_item_result)
        re_info1 = r"(.*\\u9633.*)|(.*\\u65e0.*)|(.*\\u672a.*)|(.*\u53EF\u7591.*)|(.*\\u6709.*)"
        m9_22 = re.findall(re_info1, examination_item_result)
        m10 = re.match(r'\W*(\d+\.?\d*)\W*', examination_item_result)

        if m1 :
            examination_item_result =float(m1.group(1))+0.5
        elif m2 :
            examination_item_result =float(m2.group(1))/2
        elif m31 :
            examination_item_result =float(m31[0])/2 
            count_m3_match = count_m3_match +1
        elif m4 :
            examination_item_result = ( float(m4.group(2)) + float(m4.group(1))  ) /2  
        elif m5 :
            examination_item_result =  float( m5.group(2) )  
        elif m5_1 :
            examination_item_result =  float( m5_1.group(2) )  
        elif m6 :
            examination_item_result = float( m6.group(1) ) + 5  
        elif m81 :
            count_m8_match = count_m8_match +1
            examination_item_result = 0
        elif m10 :
            examination_item_result = float( m10.group(1) ) 
        elif m9:
            count_match_num = count_match_num+1
            examination_item_result = remove_uni(examination_item_result)
            if m9_21:
                examination_item_result = 0;
                count_match_num2 = count_match_num2+1
            elif  m9_22:
                examination_item_result = 1;
                count_match_num3 = count_match_num3 +1
                
        m = re.match(r'(\d+)/(\d+)/(\d+) (\d+):(\d+)', org_time)
        if m:
            if int(m.group(1))<1970:
                if int(m.group(1))<10:
                    m1 = "0"+m.group(1)
                else:
                    m1 = m.group(1)
                if int(m.group(2))<10:
                    m2 = "0"+m.group(2)
                else:
                    m2 = m.group(2)
                org_time = "20" +m.group(3)  + str(m1) + str(m2)

            else:
                if int(m.group(2))<10:
                    m2 = "0"+m.group(2)
                else:
                    m2 = m.group(2)
                if int(m.group(3))<10:
                    m3 = "0"+m.group(3)
                else:
                    m3 = m.group(3)
                org_time = m.group(1) + str(m2) + str(m3)
        true_data = [userid,disease,examination_class,examination_item,examination_item_result,examination_item_judgement,org_time,register_num]
        for item in true_data:
            f2write.write(unicode(item))
            f2write.write(unicode(','))
        f2write.write(unicode("\n"))
    f2write.close()

#Used for classifying a column into class number
# plus 1 to ensure no "0"
def column_classify(examination_item,prior_string_list,loop_num):      
        #m = re.match(r白细胞酯酶'', examination_item)  
        if examination_item not in prior_string_list:   
            prior_string_list.append(examination_item)
            examination_item=str(loop_num)
            loop_num = loop_num+1
            #print loop_num
        else:
            examination_item=str( prior_string_list.index(examination_item)+1 )
        true_loop_num=loop_num
        return (examination_item,true_loop_num)
    
def main():
    #Should be changed
    file_half_name = u"2015-3-16--修改.csv"
    input_dir = "../DATA/Processing/"
    output_dir= "../DATA/Processing/"
    start=clock()
    trans_time(file_half_name,input_dir,output_dir)
    finish=clock()
    #t1=Timer("trans_time(file_name,input_dir,output_dir)","from __main__ import trans_time")    
    print "#######Total Time Cost:  %s seconds #######"%(finish-start)
    return

if __name__ == "__main__":
    main()
