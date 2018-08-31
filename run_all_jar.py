#!/usr/bin/env python
import sys
import os
print "Clean file!!"
clean='echo "===" > ~/chess_by_maps.txt'
os.system(clean)
"""
mushroom = ["15","15","11","9","7","6","6","5","5","5","5","5","4","4","4","3"]
maps = ["14","7","1"]
flag = 0
print "Remove temp from HDFS"
print "Now Doing mushroom dataset!!"
os.system('echo "Now Doing mushroom dataset!!" >> ~/chess_by_maps.txt')
#os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
# Min_Sup = 0.15~0.5
for i in range(15,95,5):
    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/chess_by_maps.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/chess_by_maps.txt')
    
    for map_num in maps:
        #print map_num
        now_sta = " echo "+"'" +"Map is" + map_num +"'"+ " >> ~/chess_by_maps.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar "
        para="/hadoop/mushroom0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/mushroom0" + str(i) + "_apriori_output/ " \
            + "/hadoop/mushroom0" + str(i) + "/T_Bit_Map_Candidates/ " + min_sup + " " + str(mushroom[flag]) + " 8416 " + str(map_num) 
        write_file = " >> ~/chess_by_maps.txt"
        #os.system(my_method+para+write_file)
        #os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/chess_by_maps.txt')
    flag = flag + 1

flag=0
print "Now Doing c20d10k dataset!!"
os.system('echo "Now Doing c20d10k dataset!!" >> ~/chess_by_maps.txt')
os.system('echo "===============" >> ~/chess_by_maps.txt')
c20d10k = ["13","13","12","11","11","11","11","10","10","9","8","8","7","7","6","6"]
for i in range(15,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/chess_by_maps.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/chess_by_maps.txt')
    
    for map_num in maps:
        #print map_num
        now_sta = " echo "+"'" +"Map is" + map_num +"'"+ " >> ~/chess_by_maps.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar "
        para="/hadoop/c20d10k0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/c20d10k0" + str(i) + "_apriori_output/ " \
            + "/hadoop/c20d10k0" + str(i) + "/T_Bit_Map_Candidates/ " + min_sup + " " + str(c20d10k[flag]) + " 10000 " + str(map_num) 
        write_file = " >> ~/chess_by_maps.txt"
        #os.system(my_method+para+write_file)
        #os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/chess_by_maps.txt')
    flag = flag + 1

"""
flag=0
print "Now Doing chess dataset!!"
os.system('echo "Now Doing chess dataset!!" >> ~/chess_by_maps.txt')
os.system('echo "===============" >> ~/chess_by_maps.txt')
maps = ["1","3","5","7"]
chess=["15","14","13","11","11","10","8","7"]
for i in range(55,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/chess_by_maps.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/chess_by_maps.txt')
    
    for map_num in maps:
        #print map_num
        now_sta = " echo "+"'" +"Map is" + map_num +"'"+ " >> ~/chess_by_maps.txt"
        os.system(now_sta)
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar "
        para="/hadoop/chess0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/chess0" + str(i) + "_apriori_output/ " \
            + "/hadoop/chess0" + str(i) + "/T_Bit_Map_Candidates/ " + min_sup + " " + str(chess[flag]) + " 3196 " + str(map_num) 
        write_file = " >> ~/chess_by_maps.txt"
        os.system(my_method+para+write_file)
        os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
    os.system('echo "-----------------" >> ~/chess_by_maps.txt')
    flag = flag + 1
print "Done"

