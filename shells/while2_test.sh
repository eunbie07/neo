#!/bin/bash

a=2

while [ $a != "1" ]; do
    echo -n "Input(1:Exit) : "
    read a

    if [ $a -ge 2 -a $a -le 9 ]; then
            for ((k=1;k<=9;k++)) 
        do
            echo "$a * $k = `expr $a \* $k `"
        done
    else
        echo "The number of inputs must be between 2 and 9."
    fi
done
echo Exit
