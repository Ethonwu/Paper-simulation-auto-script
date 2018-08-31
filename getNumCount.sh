#!/bin/bash
for file in `ls`
do
cd $file
for j in `seq 0 9`
    do
	name="part-r-0000$j"
        if [ -s  $name ]; then
	  echo $name 
	  #one=`cat $name | awk {'print $1'}`
	  #two=`cat $name | awk {'print $2'}`
	  #echo "`cat $name | awk {'print $1'}` `cat $name | awk {'print $2'}`"
	  cat $name >> ../../YYYYY.txt
	else
         echo "$name is empty" 
	fi
    done
cd ..

done
