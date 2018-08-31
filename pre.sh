#!/bin/bash
cd ~
#wget http://www.philippe-fournier-viger.com/spmf/datasets/c20d10k.txt .
#./hadoop-1.2.1/bin/hadoop jar -put c20d10k.txt /hadoop
echo "Now Test!!"
echo "===" > ~/pre_c20d10k.txt
echo "Now Doing c20d10k dataset"
echo "Now Doing c20d10k" >> ~/pre_c20d10k.txt

for i in $(seq 15 5 90)
do
  echo "pre MinSup = 0.$i"
  echo "pre MinSup = 0.$i" >> ~/pre_c20d10k.txt
  ./hadoop-1.2.1/bin/hadoop jar ~/F1_T_Bit_Map_Count_Key_value_task.jar /hadoop/c20d10k.txt /hadoop/c20d10k0$i/ 0.$i 2 >> ~/pre_c20d10k.txt
  echo "======================" >> ~/pre_c20d10k.txt
done

echo "===" > ~/pre_chess.txt
echo "Now Doing chess dataset"
echo "Now Doing chess" >> ~/pre_chess.txt
./hadoop-1.2.1/bin/hadoop dfs -rmr /hadoop/chess0*

for i in $(seq 15 5 90)
do
  
  echo "pre MinSup = 0.$i"
  echo "pre MinSup = 0.$i" >> ~/pre_chess.txt
  ./hadoop-1.2.1/bin/hadoop jar ~/F1_T_Bit_Map_Count_Key_value_task.jar /hadoop/chess.txt /hadoop/chess0$i/ 0.$i 2 >> ~/pre_chess.txt
  echo "======================" >> ~/pre_chess.txt
   	
done


#echo "===" > ~/pre_time.txt
#echo "Now Doing mushroom dataset"
#echo "Now Doing mushroom" >> ~/pre_time.txt
#./hadoop-1.2.1/bin/hadoop dfs -rmr /hadoop/m*0*

#for i in $(seq 15 5 90)
#do
  
#  echo "pre MinSup = 0.$i"
#  echo "pre MinSup = 0.$i" >> ~/pre_time.txt
#  ./hadoop-1.2.1/bin/hadoop jar ~/F1_T_Bit_Map_Count_Key_value_task.jar /hadoop/mushrooms.txt /hadoop/mushroom0$i/ 0.$i 2 >> ~/pre_time.txt
#  echo "======================" >> ~/pre_time.txt
   	
#done
