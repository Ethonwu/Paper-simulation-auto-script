#!/usr/bin/env python
import sys
import os
def inti_hadoop(nums):
    os.system("rm ~/slaves")
    stop_hadoop = "./hadoop-1.2.1/bin/stop-all.sh"
    os.system(stop_hadoop)
    for i in range(1,int(nums)+1,1):
        write_command = 'echo "' + "slave"+str(i) +'" '+ '>> ~/slaves'
        print write_command
        os.system(write_command)
    os.system("cp ~/slaves hadoop-1.2.1/conf/slaves")
    #  clean log and single!
    os.system("rm -r hadoop-1.2.1/logs/ ; rm -r /home/root/")
    clean_file = "sh small-script-for-hadoop/sendcommand.sh " + '"rm -r hadoop-1.2.1/logs/ ; rm -r /home/root/"'
    os.system(clean_file)
    format_HDFS = "./hadoop-1.2.1/bin/hadoop namenode -format"
    os.system(format_HDFS)
    start_hadoop = "./hadoop-1.2.1/bin/start-all.sh"
    os.system(start_hadoop) 
    upload_file = "./hadoop-1.2.1/bin/hadoop dfs -put ~/hadoop /"
    os.system(upload_file)
    print "Done!!!"
    os.system("jps")



print "Clean file!!"
clean='echo "===" > ~/nodes_c10d20k.txt'
os.system(clean)

flag=0
print "Now Doing c20d10k dataset!!"
os.system('echo "Now Doing c20d10k dataset!!" >> ~/nodes_c10d20k.txt')
os.system('echo "===============" >> ~/nodes_c10d20k.txt')
c20d10k = ["13","13","12","11","11","11","11","10","10","9","8","8","7","7","6","6"]
for nodes in range(1,7,1):
    inti_hadoop(nodes)
    print "Now Run Nodes is:" + str(nodes)
    node_info = " echo " + '"' + "Now Run Nodes is:" + str(nodes) + '"' + " >> ~/nodes_c10d20k.txt" 
    os.system(node_info)
    os.system('echo "-----------------" >> ~/nodes_c10d20k.txt')
    
    for i in range(15,95,5):
        #print map_num
        min_sup  = "0." + str(i)
        print "Now Run Min_Sup is:" + min_sup
        min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/nodes_c10d20k.txt" 
        os.system(min_sup_info)
        os.system('echo "-----------------" >> ~/nodes_c10d20k.txt')
        my_method="./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar "
        para="/hadoop/c20d10k0" + str(i) + "/T_Bit_Map/part-r-00000" + " /hadoop/c20d10k0" + str(i) + "_apriori_output/ " \
            + "/hadoop/c20d10k0" + str(i) + "/T_Bit_Map_Candidates/ " + min_sup + " " + str(c20d10k[flag]) + " 10000 " + 7
        write_file = " >> ~/nodes_c10d20k.txt"
        os.system(my_method+para+write_file)
        os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /temp")
        flag = flag + 1
    os.system('echo "-----------------" >> ~/nodes_c10d20k.txt')
    flag = 0
print "Done!!"
os.system("scp ~/nodes_c10d20k.txt es602@140.125.32.24:/var/www/html/")
