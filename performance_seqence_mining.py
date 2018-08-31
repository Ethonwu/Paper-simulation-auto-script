#!/usr/bin/env python
import sys
import os
os.system("rm ~/spmf.jar ;rm ~/seq_mining.jar ; wget 140.125.32.24/spmf.jar ; wget 140.125.32.24/seq_mining.jar")
print "Clean file!!"
clean='echo "===" > ~/map7_output.txt'
os.system(clean)
print "Now Doing mushrooms dataset!!"
os.system('echo "Now Doing mushrooms dataset!!" >> ~/map7_output.txt')
os.system('echo "===============" >> ~/map7_output.txt')
for i in range(15,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/map7_output.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/map7_output.txt')
    
    fk_get="java -jar spmf.jar run FPGrowth_itemsets mushrooms.txt ddd " + str(min_sup)
    os.system(fk_get)
    prune_fk = 'sed -i "s/ #SUP: /,/g" ddd'
    os.system(prune_fk)
    os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /hadoop/ddd")
    os.system("./hadoop-1.2.1/bin/hadoop dfs -put ~/ddd /hadoop")
    
    #for maps in range(1,7,2):
    maps = 7
    os.system('echo "=======" >> ~/map7_output.txt')
    now_sta = " echo "+"'" +"Map is" + str(maps) +"'"+ " >> ~/map7_output.txt"
    os.system(now_sta)
    my_mothed = "./hadoop-1.2.1/bin/hadoop jar ~/seq_mining.jar " 
    para = "/hadoop/mushroom0" + str(i) + "/prune_output/part-r-00000 " + "/hadoop/mushroom0"+str(i)+"_seqOutput/ " \
           + "/hadoop/ddd " + str(i) + " 8416 " + str(maps)
    write_file = " >> ~/map7_output.txt"
    os.system(my_mothed+para+write_file)
    os.system('echo "-----------------" >> ~/map7_output.txt')


print "Now Doing c20d10k dataset!!"
os.system('echo "Now Doing c20d10k dataset!!" >> ~/map7_output.txt')
os.system('echo "===============" >> ~/map7_output.txt')
for i in range(15,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/map7_output.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/map7_output.txt')
    
    fk_get="java -jar spmf.jar run FPGrowth_itemsets c20d10k.txt ddd " + str(min_sup)
    os.system(fk_get)
    prune_fk = 'sed -i "s/ #SUP: /,/g" ddd'
    os.system(prune_fk)
    os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /hadoop/ddd")
    os.system("./hadoop-1.2.1/bin/hadoop dfs -put ~/ddd /hadoop")
    os.system('echo "-----------------" >> ~/map7_output.txt')


    #for maps in range(1,7,2):
    maps=7
    os.system('echo "=======" >> ~/map7_output.txt')
    now_sta = " echo "+"'" +"Map is" + str(maps) +"'"+ " >> ~/map7_output.txt"
    os.system(now_sta)
    my_mothed = "./hadoop-1.2.1/bin/hadoop jar ~/seq_mining.jar " 
    para = "/hadoop/c20d10k0" + str(i) + "/prune_output/part-r-00000 " + "/hadoop/c20d10k0"+str(i)+"_seqOutput/ " \
           + "/hadoop/ddd " + str(i) + " 10000 " + str(maps)
    write_file = " >> ~/map7_output.txt"
    os.system(my_mothed+para+write_file)
    os.system('echo "-----------------" >> ~/map7_output.txt')


print "Now Doing chess dataset!!"
os.system('echo "Now Doing chess dataset!!" >> ~/map7_output.txt')
os.system('echo "===============" >> ~/map7_output.txt')
for i in range(55,95,5):

    min_sup  = "0." + str(i)
    print "Now Run Min_Sup is:" + min_sup
    min_sup_info = " echo " + '"' + "Now Run Min_Sup is:" + min_sup + '"' + " >> ~/map7_output.txt" 
    os.system(min_sup_info)
    os.system('echo "-----------------" >> ~/map7_output.txt')

    fk_get="java -jar spmf.jar run FPGrowth_itemsets chess.txt ddd " + str(min_sup)
    os.system(fk_get)
    prune_fk = 'sed -i "s/ #SUP: /,/g" ddd'
    os.system(prune_fk)
    os.system("./hadoop-1.2.1/bin/hadoop dfs -rmr /hadoop/ddd")
    os.system("./hadoop-1.2.1/bin/hadoop dfs -put ~/ddd /hadoop")
    os.system('echo "-----------------" >> ~/map7_output.txt')


    #for maps in range(1,7,2):
    maps=7
    os.system('echo "=======" >> ~/map7_output.txt')
    now_sta = " echo "+"'" +"Map is" + str(maps) +"'"+ " >> ~/map7_output.txt"
    os.system(now_sta)
    my_mothed = "./hadoop-1.2.1/bin/hadoop jar ~/seq_mining.jar " 
    para = "/hadoop/chess0" + str(i) + "/prune_output/part-r-00000 " + "/hadoop/chess0"+str(i)+"_seqOutput/ " \
           + "/hadoop/ddd " + str(i) + " 3196 " + str(maps)
    write_file = " >> ~/map7_output.txt"
    os.system(my_mothed+para+write_file)

    os.system('echo "-----------------" >> ~/map7_output.txt')

os.system("scp ~/map7_output.txt es602@140.125.32.24:/var/www/html/")
print "Done"

