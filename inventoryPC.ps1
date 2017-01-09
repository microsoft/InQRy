clear
$alias = $asset = $null
while ($alias -eq $null -or $alias -eq ''){
    $alias = Read-Host -Prompt "Input End-User's Alias"
}
while ($asset -eq $null -or $asset -eq ''){
    $asset = Read-Host -Prompt "Input Machine's Asset Tag #"
}

$assetCompare = Get-WmiObject Win32_SystemEnclosure | Select-object SMBIOSAssetTag
If ($asset -ne $assetCompare){
    $compare = read-host "Manually entered asset number does not match asset number contained in BIOS.  Which to keep - BIOS (B(DEFAULT)) or Manual (M)"
    if ($compare -eq "M"){
        $asset = $asset
        write-host "Keeping manually entered Asset Number"
    }else{
        $asset = $assetCompare.SMBIOSAssetTag
        write-host "Keeping BIOS contained Asset Number"
    }
}

$serialNumber = get-ciminstance win32_bios | Select-object serialnumber
write-host "Collecting Serial Number"
$manufacturer = get-ciminstance win32_bios | Select-object manufacturer
write-host "Collecting Manufacturer"
$model = Get-WmiObject -Class Win32_computersystem | Select-Object model
write-host "Collecting Model"
$numberOfCores = Get-WmiObject -class win32_processor | Select-Object numberOfCores
write-host "Collecting Number Of Cores"
$physicalMemory = [math]::ceiling(((Get-WmiObject -Class Win32_ComputerSystem).totalphysicalmemory)/1GB)
write-host "Collecting Physical Memory total"
$drives = Get-WmiObject -Class win32_diskdrive
write-host "Collecting Hard Drive(s) model(s) and size(s)"
$hdd = @('','','','','')
$size = @('','','','','')
$i = 0
$drives.model | ForEach-Object {
    if ($_ -gt 0){
        $hdd[$i] = $_.ToString()
    }else{
        $hdd[$i] = ''
    }
    $i ++
}
$i= 0
$drives.size | ForEach-Object {
    if ($_ -gt 0){
        $size[$i] = ([math]::Ceiling($_/1gb)).tostring() + "GB"
    }else{
        $size[$i] = ''
    }
    $i ++
}


$pc = [pscustomobject][ordered]@{
    "alias" = $alias
    "asset" = $asset
    "serialNumber" = $serialNumber.serialNumber
    "manufacturer" = $manufacturer.manufacturer
    "model" = $model.model
    "numberOfCores" = $numberOfCores.numberOfCores
    "physicalMemory" = (($physicalMemory).ToString() + "GB")
    "harddriveCount" = $drives.Count
    "hddModel0" = $hdd[0]
    "hddSize0" = $size[0]
    "hddModel1" = $hdd[1]
    "hddSize1" = $size[1]
    "hddModel2" = $hdd[2]
    "hddSize2" = $size[2]
    "hddModel3" = $hdd[3]
    "hddSize3" = $size[3]
    "hddModel4" = $hdd[4]
    "hddSize4" = $size[4]
}

write-host "Confirm collected data:"
$pc
Function Ask-YesOrNo{
    param([string]$title="Confirm",[string]$message= "Data is correct?")
	$choiceYes = New-Object System.Management.Automation.Host.ChoiceDescription "&Yes", "Answer Yes."
	$choiceNo = New-Object System.Management.Automation.Host.ChoiceDescription "&No", "Answer No."
	$options = [System.Management.Automation.Host.ChoiceDescription[]]($choiceYes, $choiceNo)
	$result = $host.ui.PromptForChoice($title, $message, $options, 1)
		switch ($result)
    	{
			0
			{
                $path = '\\apex35supr3arch\F$\INVENTORY\DESKTOP\' + $asset + '.csv'
			    write-host "Saving data to $path"
                $pc | convertto-csv -NoTypeInformation | out-file $path
			}

			1
			{
			    Write-Host "Please run script again to recollect data"
			}
		}
}

Ask-YesOrNo
