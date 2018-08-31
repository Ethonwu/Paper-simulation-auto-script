#!/bin/bash
wget 140.125.32.24/kddcup99_100k.txt
wget 140.125.32.24/kddcup99_200k.txt
wget 140.125.32.24/kddcup99_50k.txt
wget 140.125.32.24/kddcup99_10k.txt
echo "==" > ~/a.txt
for i in `seq 1 7 ` 
do
	echo "slave"$i >> ~/slaves
done
./hadoop-1.2.1/bin/stop-all.sh
cp ~/slaves ~/hadoop-1.2.1/conf/slaves
rm -r hadoop-1.2.1/logs/ ; rm -r /home/root/
sh small-script-for-hadoop/sendcommand.sh "rm -r hadoop-1.2.1/logs/ ; rm -r /home/root/"
./hadoop-1.2.1/bin/hadoop namenode -format
./hadoop-1.2.1/bin/start-all.sh
./hadoop-1.2.1/bin/hadoop dfs -put ~/hadoop /
./hadoop-1.2.1/bin/hadoop dfs -put ~/kddcup99_100k.txt /hadoop
./hadoop-1.2.1/bin/hadoop dfs -put ~/kddcup99_200k.txt /hadoop
./hadoop-1.2.1/bin/hadoop dfs -put ~/kddcup99_50k.txt /hadoop
./hadoop-1.2.1/bin/hadoop dfs -put ~/kddcup99_10k.txt /hadoop
echo "=========================================="
echo "Now Doing Pre "
echo "=========================================="
./hadoop-1.2.1/bin/hadoop jar ~/F1_T_Bit_Map_Count_Key_value_task.jar /hadoop/kddcup99_100k.txt /hadoop/kddcup99_100k040/ 0.4 2
./hadoop-1.2.1/bin/hadoop jar ~/F1_T_Bit_Map_Count_Key_value_task.jar /hadoop/kddcup99_200k.txt /hadoop/kddcup99_200k040/ 0.4 2
./hadoop-1.2.1/bin/hadoop jar ~/F1_T_Bit_Map_Count_Key_value_task.jar /hadoop/kddcup99_50k.txt /hadoop/kddcup99_50k040/ 0.4 2
./hadoop-1.2.1/bin/hadoop jar ~/F1_T_Bit_Map_Count_Key_value_task.jar /hadoop/kddcup99_10k.txt /hadoop/kddcup99_10k040/ 0.4 2
echo "=========================================="
echo "Finish Doing Pre "
echo "=========================================="



echo "=========================================="
echo "Now Doing Candidate-Itemset " >> ~/a.txt
echo "Now Doing Candidate-Itemset "
echo "=========================================="


echo "Now Doing 100K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/kddcup99_100k040/T_Bit_Map/part-r-00000 /hadoop/c20d10k_output/ /hadoop/kddcup99_100k040/T_Bit_Map_Candidates/ 0.4 17 1000000 7 >> ~/a.txt
./hadoop-1.2.1/bin/hadoop dfs -rmr /temp
echo "Now Doing 200K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/kddcup99_200k040/T_Bit_Map/part-r-00000 /hadoop/c20d10k_output/ /hadoop/kddcup99_200k040/T_Bit_Map_Candidates/ 0.4 17 2000000 7 >> ~/a.txt
./hadoop-1.2.1/bin/hadoop dfs -rmr /temp
echo "Now Doing 50K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/kddcup99_50k040/T_Bit_Map/part-r-00000 /hadoop/c20d10k_output/ /hadoop/kddcup99_50k040/T_Bit_Map_Candidates/ 0.4 17 500000 7 >> ~/a.txt
./hadoop-1.2.1/bin/hadoop dfs -rmr /temp
echo "Now Doing 10K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/kddcup99_10k040/T_Bit_Map/part-r-00000 /hadoop/c20d10k_output/ /hadoop/kddcup99_10k040/T_Bit_Map_Candidates/ 0.4 17 100000 7 >> ~/a.txt
./hadoop-1.2.1/bin/hadoop dfs -rmr /temp



echo "=========================================="
echo "Now Doing Big Fim " >> ~/a.txt
echo "Now Doing Big Fim "
echo "=========================================="


echo "Now Doing 100K Dataset" >> ~/a.txt
for i in `seq 1 15`
do
./hadoop-1.2.1/bin/hadoop jar ~/bigfim-sa-1.0-jar-with-dependencies.jar be.uantwerpen.adrem.disteclat.DistEclatDriver -i /hadoop/kddcup99_100k.txt -o /hadoop/big_fim_output/ -s 400000 -m 7 -p $i >> ~/a.txt
done

echo "Now Doing 200K Dataset" >> ~/a.txt
for i in `seq 1 15`
do
./hadoop-1.2.1/bin/hadoop jar ~/bigfim-sa-1.0-jar-with-dependencies.jar be.uantwerpen.adrem.disteclat.DistEclatDriver -i /hadoop/kddcup99_200k.txt -o /hadoop/big_fim_output/ -s 800000 -m 7 -p $i >> ~/a.txt
done

echo "Now Doing 50K Dataset" >> ~/a.txt
for i in `seq 1 15`
do
./hadoop-1.2.1/bin/hadoop jar ~/bigfim-sa-1.0-jar-with-dependencies.jar be.uantwerpen.adrem.disteclat.DistEclatDriver -i /hadoop/kddcup99_50k.txt -o /hadoop/big_fim_output/ -s 200000 -m 7 -p $i >> ~/a.txt
done

echo "Now Doing 10K Dataset" >> ~/a.txt
for i in `seq 1 15`
do
./hadoop-1.2.1/bin/hadoop jar ~/bigfim-sa-1.0-jar-with-dependencies.jar be.uantwerpen.adrem.disteclat.DistEclatDriver -i /hadoop/kddcup99_10k.txt -o /hadoop/big_fim_output/ -s 40000 -m 7 -p $i >> ~/a.txt
done


echo "=========================================="
echo "Now Doing Brute Force " >> ~/a.txt
echo "Now Doing Brute Force "
echo "=========================================="

echo "Now Doing 100K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_by_Brute_force.jar /hadoop/kddcup99_100k040/T_Bit_Map/part-r-00000 /hadoop/Brute_100output/ 1000000 0.4 17 >> ~/a.txt

echo "Now Doing 200K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_by_Brute_force.jar /hadoop/kddcup99_200k040/T_Bit_Map/part-r-00000 /hadoop/Brute_200output/ 2000000 0.4 17 >> ~/a.txt

echo "Now Doing 50K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_by_Brute_force.jar /hadoop/kddcup99_50k040/T_Bit_Map/part-r-00000 /hadoop/Brute_50output/ 500000 0.4 16 >> ~/a.txt

echo "Now Doing 10K Dataset" >> ~/a.txt
./hadoop-1.2.1/bin/hadoop jar ~/T_Bit_Map_Mining_by_Brute_force.jar /hadoop/kddcup99_10k040/T_Bit_Map/part-r-00000 /hadoop/Brute_10output/ 100000 0.4 16 >> ~/a.txt
echo "Done!!"
scp ~/a.txt es602@140.125.32.24:/var/www/html/ 
