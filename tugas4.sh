#!/bin/bash

echo -n "Input bilangan ganjil: ";
read odd;

a=0

until [ ! $odd -gt $a ]
do
   echo $odd
   odd=$((odd-2))
done
