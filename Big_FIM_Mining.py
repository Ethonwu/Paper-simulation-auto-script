#!/usr/bin/env python
import sys
import os

print "Clean file!!"
clean='echo "===" > ~/BigFim_mushroom_15_90.txt'
os.system(clean)
mushroom = ["15","15","11","9","7","6","6","5","5","5","5","5","4","4","4","3"]
flag = 0
print "Remove temp from HDFS"
print "Now Doing mushroom dataset!! Using Big Fim"
os.system('echo "Now Doing mushroom dataset!! Using Big_Fim" >> ~/BigFim_mushroom_15_90.txt')
# Min_Sup = 0.15~0.5
for i in range(15,95,5):
    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/BigFim_mushroom_15_90.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/BigFim_mushroom_15_90.txt')
    max_len = mushroom[flag]
    support_count = int(float(min_sup)*8416)
    print "Now Support count is:"+str(support_count)
    for j in range(1,int(max_len)+1,1):
        #print "Now is:"+str(j)
        now_sta = " echo "+"'" +"Now k is" + str(j) +"'"+ " >> ~/BigFim_mushroom_15_90.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/bigfim-sa-1.0-jar-with-dependencies.jar be.uantwerpen.adrem.disteclat.DistEclatDriver "
        para="-i /hadoop/mushrooms.txt -o /hadoop/BigFim_output/ -s " + str(support_count) + " -m 7 -p " + str(j) 
        write_file = " >> ~/BigFim_mushroom_15_90.txt"
        os.system(my_method+para+write_file)
    os.system('echo "-----------------" >> ~/BigFim_mushroom_15_90.txt')
    flag = flag + 1

os.system("scp ~/BigFim_mushroom_15_90.txt es602@140.125.32.24:/var/www/html/")
"""
os.system("wget 140.125.32.24/bigfim-sa-1.0-jar-with-dependencies.jar")

flag=0
print "Now Doing c20d10k dataset!!"
os.system('echo "Now Doing c20d10k dataset!!" >> ~/BigFIM_BigFIM_compare.txt')
os.system('echo "===============" >> ~/BigFIM_compare.txt')
c20d10k = ["13","13","12","11","11","11","11","10","10","9","8","8","7","7","6","6"]
for i in range(15,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/BigFIM_compare.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/BigFIM_compare.txt')
    max_len = c20d10k[flag]
    support_count = int(float(min_sup)*10000)
    print "Now Support count is:"+str(support_count)
    for j in range(1,int(max_len)+1,1):
        #print "Now is:"+str(j)
        now_sta = " echo "+"'" +"Now k is" + str(j) +"'"+ " >> ~/BigFIM_compare.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/bigfim-sa-1.0-jar-with-dependencies.jar be.uantwerpen.adrem.disteclat.DistEclatDriver "
        para="-i /hadoop/c20d10k0" + str(i) + "/prune_output/part-r-00000 -o /hadoop/BigFim_output/ -s " + str(support_count) + " -m 7 -p " + str(j) 
        write_file = " >> ~/BigFIM_compare.txt"
        os.system(my_method+para+write_file)
    os.system('echo "-----------------" >> ~/BigFIM_compare.txt')
    flag = flag + 1


flag=0
print "Now Doing chess dataset!!"
os.system('echo "Now Doing chess dataset!!" >> ~/BigFIM_compare.txt')
os.system('echo "===============" >> ~/BigFIM_compare.txt')
chess=["15","14","13","11","11","10","8","7"]
for i in range(55,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/BigFIM_compare.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/BigFIM_compare.txt')
    max_len = chess[flag]
    support_count = int(float(min_sup)*3196)
    print "Now Support count is:"+str(support_count)
    for j in range(1,int(max_len)+1,1):
        #print map_num
        now_sta = " echo "+"'" +"Now k is" + str(j) +"'"+ " >> ~/BigFIM_compare.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/bigfim-sa-1.0-jar-with-dependencies.jar be.uantwerpen.adrem.disteclat.DistEclatDriver "
        para="-i /hadoop/chess0" + str(i) + "/prune_output/part-r-00000 -o /hadoop/BigFim_output/ -s " + str(support_count) + " -m 7 -p " + str(j)
        write_file = " >> ~/BigFIM_compare.txt"
        os.system(my_method+para+write_file)
    os.system('echo "-----------------" >> ~/BigFIM_compare.txt')
    flag = flag + 1
"""
print "Done"

