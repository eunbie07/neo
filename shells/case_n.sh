#!/bin/bash
case "$1" in
        ko) echo "Seoul";;
        us) echo "Washington";;
        cn) echo "Beijing";;
        jp) echo "Tokyo";;
        "") echo "Enter the country name~!!";;
        *) echo "Your entry => "$1" is not in the list.";;

esac