#!/bin/bash

serial_number=$(system_profiler SPHardwareDataType |
    grep "Serial" | awk '/Serial/ { print $4 }')

model_name=$(
    apple_url='http://support-sp.apple.com/sp/product/?cc='
    curl -s "$apple_url$(echo "$serial_number" | cut -c 9-)" |
    sed 's|.*<configCode>\(.*\)</configCode>.*|\1|')

echo $serial_number
echo $model_name
