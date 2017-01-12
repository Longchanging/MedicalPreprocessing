%% FeatherExtraction
%% LanqingYangï¼?0161227,20161228,20170102
function time=FeatherDigest()

clear;clc;
start=clock;

%% File Process
datapath = '../DATA/Processing/TimeTransformed_';
outputpath='../DATA/Processing/Extracted_feather_';
output_data=[outputpath  '2015-3-16--ÐÞ¸Ä.csv'];
fid1 = fopen(output_data, 'w');  

org_data=csvread([datapath  '2015-3-16--ÐÞ¸Ä.csv']);
[m,n]=size(org_data);
org_data=org_data(:,1:n-1);
try_cnv=org_data';

%% Start Extraction

%Sort By User and Time
Sorted_data = sortrows(org_data,[1,7]);

%Var Define
User = Sorted_data(:,1);
Disease=Sorted_data(:,2);
Item = Sorted_data(:,4);
Result =Sorted_data(:,5);
Judge =Sorted_data(:,6);
Time = Sorted_data(:,7);
user_list =[];
time_list =[];
cnt_group =0;
Prior_user=User(1);
Prior_time=Time(1);
Item_feather=zeros(1,2*max(Item));
Feather_all=[];
loop_j=0;
Not_NM_cnt=0;
Length_stay=0;
Cnt_one_month=0;

%Fetch Feather and Loop 
for i=1:length(Sorted_data)
    if User(i)==Prior_user
        if floor(Time(i)/100)==floor(Prior_time/100)
            Cnt_one_month=Cnt_one_month+1;
            Item_feather(:,Item(i))=Result(i);
            Item_feather(:,2*Item(i))=Judge(i);
            if Judge(i)~=1
                Not_NM_cnt=Not_NM_cnt+1;
            end
        end
    else
        Cnt_one_month=0;
    end
    
    if i<m &&(floor(Time(i+1)/100)~=floor(Time(i)/100) || User(i+1)~=User(i))
       if Not_NM_cnt==0
           Is_NM=1;
       else
           Is_NM=0;
       end
       Feather_each=[User(i),Disease(i),floor(Time(i)/100),Item_feather,Is_NM,Cnt_one_month];
       Feather_all=[Feather_all;Feather_each];
    end
    Prior_user = User(i);
    Prior_time = Time(i);
end

%% Result Store

item_feather_name='';
a=max(Sorted_data(:,4));
for cnt=1:2*a
    s = sprintf('%d', int8(cnt));
    temp=['feather',s,','];
    item_feather_name=[item_feather_name,temp];
end
feather_name=['user,','disease,month_time,',item_feather_name,'is_nm,','cnt_one_month,','NULL'];

%csvwrite(output_data,'feather_name');
%csvwrite(output_data,Feather_all);
fprintf(fid1,'%s',feather_name);
fprintf(fid1,'\n');
%disp('yes');
 for i = 1:length(Feather_all)   
     fprintf(fid1,'%f,',Feather_all(i,:));
     fprintf(fid1,'\n');
 end
 
%% Time Used
%disp 'total time consumed by FeatherExtraction:'
finish=clock;
time=finish(6)-start(6);

end