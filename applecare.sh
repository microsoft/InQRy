#!/bin/bash

serial_number=$(system_profiler SPHardwareDataType | awk ':' {print $2} )

model_name=$(
    apple_url='http://support-sp.apple.com/sp/product/?cc='
    curl "$apple_url$(echo "$serial_number" | cut -c 9-)" |
    sed 's|.*<configCode>\(.*\)</configCode>.*|\1|' |
    tr -d '()'
  )

echo $model_name
