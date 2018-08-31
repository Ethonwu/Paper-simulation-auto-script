#!/bin/bash
cd ~
map14="14"
map7="7"
map1="1"
basePath="~/mush_apriori_result.txt"
echo "===" > basePath
echo "Now Doing mushroom dataset"
echo "Now Doing mushroom" >> basePath

  echo "pre MinSup = 0.15 and map is 14"
  echo "pre MinSup = 0.15 and map is 14" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom015/T_Bit_Map/part-r-00000 /hadoop/mushroom015_output_no_prune/  /hadoop/mushroom015/T_Bit_Map_Candidates/ 0.15 15 8416 $map14 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 
  
  echo "pre MinSup = 0.15 and map is 7"
  echo "pre MinSup = 0.15 and map is 7" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom015/T_Bit_Map/part-r-00000 /hadoop/mushroom015_output_no_prune/  /hadoop/mushroom015/T_Bit_Map_Candidates/ 0.15 15 8416 $map7 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 

  echo "pre MinSup = 0.15 and map is 1"
  echo "pre MinSup = 0.15 and map is 1" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom015/T_Bit_Map/part-r-00000 /hadoop/mushroom015_output_no_prune/  /hadoop/mushroom015/T_Bit_Map_Candidates/ 0.15 15 8416 $map1 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 

  echo "pre MinSup = 0.2 and map is 14"
  echo "pre MinSup = 0.2 and map is 14" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom020/T_Bit_Map/part-r-00000 /hadoop/mushroom020_output_no_prune/  /hadoop/mushroom020/T_Bit_Map_Candidates/ 0.2 15 8416 $map14 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 

  echo "pre MinSup = 0.2 and map is 7"
  echo "pre MinSup = 0.2 and map is 7" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom020/T_Bit_Map/part-r-00000 /hadoop/mushroom020_output_no_prune/  /hadoop/mushroom020/T_Bit_Map_Candidates/ 0.2 15 8416 $map7 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 

  echo "pre MinSup = 0.2 and map is 1"
  echo "pre MinSup = 0.2 and map is 1" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom020/T_Bit_Map/part-r-00000 /hadoop/mushroom020_output_no_prune/  /hadoop/mushroom020/T_Bit_Map_Candidates/ 0.2 15 8416 $map1 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 

  echo "pre MinSup = 0.25 and map is 14"
  echo "pre MinSup = 0.25 and map is 14" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom025/T_Bit_Map/part-r-00000 /hadoop/mushroom025_output_no_prune/  /hadoop/mushroom025/T_Bit_Map_Candidates/ 0.25 11 8416 $map14 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 

  echo "pre MinSup = 0.25 and map is 7"
  echo "pre MinSup = 0.25 and map is 7" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom025/T_Bit_Map/part-r-00000 /hadoop/mushroom025_output_no_prune/  /hadoop/mushroom025/T_Bit_Map_Candidates/ 0.25 11 8416 $map7 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 


  echo "pre MinSup = 0.25 and map is 1"
  echo "pre MinSup = 0.25 and map is 1" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom025/T_Bit_Map/part-r-00000 /hadoop/mushroom025_output_no_prune/  /hadoop/mushroom025/T_Bit_Map_Candidates/ 0.25 11 8416 $map1 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 


  echo "pre MinSup = 0.3 and map is 14"
  echo "pre MinSup = 0.3 and map is 14" >> basePath
  ./hadoop jar ~/T_Bit_Map_Mining_using_down_to_top_disCache_usgin_apriori_gen_modify_map.jar /hadoop/mushroom025/T_Bit_Map/part-r-00000 /hadoop/mushroom025_output_no_prune/  /hadoop/mushroom025/T_Bit_Map_Candidates/ 0.25 11 8416 $map14 >> basePath 
  echo "======================" >> basePath
  ./hadoop-1.2.1/bin/hadoop dfs -rmr /temp 

