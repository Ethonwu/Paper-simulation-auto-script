#!/usr/bin/env python
import sys
import os
"""
print "Clean file!!"
clean='echo "===" > ~/One_phase_c20d10k.txt'
os.system(clean)
maps = ["14","7","1"]
flag = 0
print "Remove temp from HDFS"
print "Now Doing c20d10k dataset!! Using One_Phase"
os.system('echo "Now Doing c20d10k dataset!! Using One_Phase" >> ~/One_phase_c20d10k.txt')
os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
# Min_Sup = 0.15~0.5
for i in range(15,95,5):
    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/One_phase_c20d10k.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/One_phase_c20d10k.txt')
    
    for map_num in maps:
        #print map_num
        now_sta = " echo "+"'" +"Map is" + map_num +"'"+ " >> ~/One_phase_c20d10k.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/One_phase.jar "
        para="/hadoop/c20d10k0" + str(i) + "/prune_output/part-r-00000" + " /hadoop/c20d10k0" + str(i) + "_OnePhase_output/ " \
             + min_sup + " 10000 " + str(map_num) 
        write_file = " >> ~/One_phase_c20d10k.txt"
        os.system(my_method+para+write_file)
        os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/One_phase_c20d10k.txt')
    flag = flag + 1

os.system("scp ~/One_phase_c20d10k.txt es602@140.125.32.24:/var/www/html/")
"""
"""
print "Clean file!!"
clean='echo "===" > ~/One_phase_chess.txt'
os.system(clean)
maps = ["14","7","1"]
flag = 0
print "Remove temp from HDFS"
print "Now Doing chess dataset!! Using One_Phase"
os.system('echo "Now Doing chess dataset!! Using One_Phase" >> ~/One_phase_chess.txt')
os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
# Min_Sup = 0.15~0.5
for i in range(90,65,-5):
    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/One_phase_chess.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/One_phase_chess.txt')
    
    for map_num in maps:
        #print map_num
        now_sta = " echo "+"'" +"Map is" + map_num +"'"+ " >> ~/One_phase_chess.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/One_phase.jar "
        para="/hadoop/chess0" + str(i) + "/prune_output/part-r-00000" + " /hadoop/chess0" + str(i) + "_OnePhase_output/ " \
             + min_sup + " 3196 " + str(map_num) 
        write_file = " >> ~/One_phase_chess.txt"
        os.system(my_method+para+write_file)
        os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/One_phase_chess.txt')
    flag = flag + 1

os.system("scp ~/Brute_Force_c20d10k.txt es602@140.125.32.24:/var/www/html/")
"""
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

####  Doing chess Brute Force
"""
len_list= []
for i in range(90,70,-5):
    read_T_Bit_Map= "./hadoop-1.2.1/bin/hadoop dfs -cat /hadoop/chess0" + str(i) + "/T_Bit_Map/part-r-00000 | head -n 1 | awk {'print $1'} > ~/T_Bit_Map.tmp"
    os.system(read_T_Bit_Map)
    cmd = "cat ~/T_Bit_Map.tmp | head -n 2"
    s=(os.popen(cmd).read())
    len_list.append(len(s)-1)
print "Final is:"
print len_list
sys.exit()
flag=0
print "Now Doing chess dataset!!"
os.system('echo "Now Doing chess dataset!! Using Brute Force" > ~/Btute_Force_chess.txt')
os.system('echo "===============" >> ~/Btute_Force_chess.txt')
for i in range(90,70,-5):
    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/Btute_Force_chess.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/Btute_Force_chess.txt')
    my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_by_Brute_force.jar "
    para="/hadoop/chess0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/chess0" + str(i) + "_Brute_output/ " \
        + " 3196 " + min_sup +" "+ str(len_list[flag])
    write_file = " >> ~/Btute_Force_chess.txt"
    os.system(my_method+para+write_file)
    os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/Btute_Force_chess.txt')
    flag = flag + 1

os.system("scp ~/Btute_Force_chess.txt es602@140.125.32.24:/var/www/html/")
"""
len_listc20= []
for i in range(90,20,-5):
    read_T_Bit_Map= "./hadoop-1.2.1/bin/hadoop dfs -cat /hadoop/c20d10k0" + str(i) + "/T_Bit_Map/part-r-00000 | head -n 1 | awk {'print $1'} > ~/T_Bit_Map.tmp"
    os.system(read_T_Bit_Map)
    cmd = "cat ~/T_Bit_Map.tmp | head -n 2"
    s=(os.popen(cmd).read())
    len_listc20.append(len(s)-1)
print "Final is:"
print len_listc20
flag=0
print "Now Doing c20d10k dataset!!"
os.system('echo "Now Doing chess dataset!! Using Brute Force" > ~/Btute_Force_c20d10k.txt')
os.system('echo "===============" >> ~/Btute_Force_c20d10k.txt')
for i in range(90,20,-5):
    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/Btute_Force_c20d10k.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/Btute_Force_c20d10k.txt')
    my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_by_Brute_force.jar "
    para="/hadoop/c20d10k0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/c20d10k0" + str(i) + "_Brute_output/ " \
        + " 10000 " + min_sup +" "+ str(len_listc20[flag])
    write_file = " >> ~/Btute_Force_c20d10k.txt"
    os.system(my_method+para+write_file)
    os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/Btute_Force_c20d10k.txt')
    flag = flag + 1
os.system("scp ~/Brute_Force_c20d10k.txt es602@140.125.32.24:/var/www/html/")
"""
T_Bit_Map_len = ["4","4","5","5","5","6","8","12","13","19","21"]
flag=0
print "Now Doing mushroom dataset!!"
os.system('echo "Now Doing mushroom dataset!! Using Brute Force" > ~/Btute_Force_compare.txt')
os.system('echo "===============" >> ~/Btute_Force_compare.txt')
for i in range(90,35,-5):
    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/Btute_Force_compare.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/Btute_Force_compare.txt')
    my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_by_Brute_force.jar "
    para="/hadoop/mushroom0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/mushroom0" + str(i) + "_Brute_output/ " \
        + " 8416 " + min_sup +" "+ str(T_Bit_Map_len[flag])
    write_file = " >> ~/Btute_Force_compare.txt"
    os.system(my_method+para+write_file)
    os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/Btute_Force_compare.txt')
    flag = flag + 1

#os.system("scp ~/Btute_Force_compare.txt es602@140.125.32.24:/var/www/html/")
"""
"""
flag=0
print "Now Doing c20d10k dataset!!"
os.system('echo "Now Doing c20d10k dataset!!" >> ~/compare.txt')
os.system('echo "===============" >> ~/compare.txt')
c20d10k = ["13","13","12","11","11","11","11","10","10","9","8","8","7","7","6","6"]
for i in range(15,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/compare.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/compare.txt')
    
    for map_num in maps:
        #print map_num
        now_sta = " echo "+"'" +"Map is" + map_num +"'"+ " >> ~/compare.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar "
        para="/hadoop/c20d10k0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/c20d10k0" + str(i) + "_apriori_output/ " \
            + "/hadoop/c20d10k0" + str(i) + "/T_Bit_Map_Candidates/ " + min_sup + " " + str(c20d10k[flag]) + " 10000 " + str(map_num) 
        write_file = " >> ~/compare.txt"
        #os.system(my_method+para+write_file)
        #os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/compare.txt')
    flag = flag + 1


flag=0
print "Now Doing chess dataset!!"
os.system('echo "Now Doing chess dataset!!" >> ~/compare.txt')
os.system('echo "===============" >> ~/compare.txt')
chess=["15","14","13","11","11","10","8","7"]
for i in range(55,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/compare.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/compare.txt')
    
    for map_num in maps:
        #print map_num
        now_sta = " echo "+"'" +"Map is" + map_num +"'"+ " >> ~/compare.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar "
        para="/hadoop/chess0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/chess0" + str(i) + "_apriori_output/ " \
            + "/hadoop/chess0" + str(i) + "/T_Bit_Map_Candidates/ " + min_sup + " " + str(chess[flag]) + " 3196 " + str(map_num) 
        write_file = " >> ~/compare.txt"
        #os.system(my_method+para+write_file)
        #os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/compare.txt')
    flag = flag + 1
print "Done"
"""
