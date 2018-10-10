from inqry.system_specs import windisk

GET_PHYSICALDISK_OUTPUT = '''

ClassName                        : MSFT_PhysicalDisk
Usage                            : Auto-Select
OperationalStatus                : OK
UniqueIdFormat                   : SCSI Name String
HealthStatus                     : Healthy
BusType                          : NVMe
CannotPoolReason                 : Insufficient Capacity
SupportedUsages                  : {Auto-Select, Manual-Select, Hot Spare, Retired...}
MediaType                        : SSD
SpindleSpeed                     : 0
ObjectId                         : {1}\\MININT-MSGHJGV\root/Microsoft/Windows/Storage/Providers_v2
\SPACES_PhysicalDisk.ObjectId="{7869a9f6-d79a-11e6-84dd-806e6f6e6963}:PD:{ed172607-d72a-1b5a-f
                                   367-403fe45ca8d5}"
PassThroughClass                 :
PassThroughIds                   :
PassThroughNamespace             :
PassThroughServer                :
UniqueId                         : eui.0025384161B6798A
Description                      :
FriendlyName                     : SAMSUNG MZFLV256HCHP-000MV
Manufacturer                     :
Model                            : SAMSUNG MZFLV256HCHP-000MV
OperationalDetails               :
PhysicalLocation                 : PCI Slot 4 : Adapter 0
SerialNumber                     : 0025_3841_61B6_798A.
AdapterSerialNumber              : S245NXCH108281      
AllocatedSize                    : 256060514304
CanPool                          : False
DeviceId                         : 0
EnclosureNumber                  :
FirmwareVersion                  : BXV75M0Q
IsIndicationEnabled              :
IsPartial                        : True
LogicalSectorSize                : 512
OtherCannotPoolReasonDescription :
PartNumber                       :
PhysicalSectorSize               : 512
Size                             : 256060514304
SlotNumber                       :
SoftwareVersion                  :
VirtualDiskFootprint             : 0
PSComputerName                   :
CimClass                         : root/microsoft/windows/storage:MSFT_PhysicalDisk
CimInstanceProperties            : {ObjectId, PassThroughClass, PassThroughIds, PassThroughNamespace...}
CimSystemProperties              : Microsoft.Management.Infrastructure.CimSystemProperties



'''

test_disk = windisk.Disk(GET_PHYSICALDISK_OUTPUT)


def test_creating_a_disk_from_get_physical_disk_output():
    assert windisk.Disk(GET_PHYSICALDISK_OUTPUT)


def test_getting_bus_type_from_a_windows_disk():
    assert test_disk.bustype == 'NVMe'


def test_differentiating_between_internal_and_external_drives():
    assert test_disk.is_internal


def test_is_external_drive_returns_false():
    assert not test_disk.is_external


def test_readability_for_storage_property():
    assert test_disk.size == '256 GB'


def test_whether_a_drive_is_solid_state_or_spinner():
    assert test_disk.type == 'SSD'


def test_is_ssd_returns_true():
    assert test_disk.is_ssd


def test_getting_the_friendly_name_of_a_device():
    assert test_disk.device_name == 'SAMSUNG MZFLV256HCHP-000MV'


def test_device_location_property_returns_correctly():
    assert test_disk.device_location == 'Internal'
