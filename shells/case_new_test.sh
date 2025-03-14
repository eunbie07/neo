#!/bin/bash

if [ "$1" = "ko" ] || [ "$1" = "us" ] || [ "$1" = "cn" ] || [ "$1" = "jp" ]; then
    case "$1" in
        ko) echo "Seoul";;
        us) echo "Washington";;
        cn) echo "Beijing";;
        jp) echo "Tokyo";;
        *) echo "Enter the country name~!!";;
    esac
else
    echo "Your entry => "$1" is not in the list."
fi