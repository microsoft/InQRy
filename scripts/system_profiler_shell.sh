#!/bin/bash

name=$(system_profiler SPHardwareDataType | awk '/Model Name/ { print $2,$3 }')
memory=$(system_profiler SPHardwareDataType | awk '/Memory/ { print $2,$3 }')
serial=$(system_profiler SPHardwareDataType | awk '/Serial/ { print $4 }')
model=$(system_profiler SPHardwareDataType | awk '/Model Identifier/ { print $3 }')
p_speed=$(system_profiler SPHardwareDataType | awk '/Processor Speed/ { print $3,$4 }')
p_name=$(system_profiler SPHardwareDataType | awk '/Processor Name/ { print $3,$4,$5 }')






# serialata=$(system_profiler SPSerialATADataType)
# storage=$(system_profiler SPStorageDataType)

# $hardware | awk '/Memory/ { print $2, $3 }'

# hardware_xml=$(system_profiler -xml SPHardwareDataType)

# echo $hardware
echo $name
echo $serial
echo $memory
echo $model
echo $p_speed
echo $p_name
