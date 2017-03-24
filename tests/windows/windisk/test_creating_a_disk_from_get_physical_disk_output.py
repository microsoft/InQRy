from inqry.system_specs import windisk

GET_PHYSICALDISK_OUTPUT = '''
ClassName                        : MSFT_PhysicalDisk
Usage                            : Auto-Select
OperationalStatus                : OK
UniqueIdFormat                   : Vendor Specific
HealthStatus                     : Healthy
BusType                          : SATA
CannotPoolReason                 : Insufficient Capacity
SupportedUsages                  : {Auto-Select, Manual-Select, Hot Spare, Retired...}
MediaType                        : SSD
SpindleSpeed                     : 0
ObjectId                         : {1}\\APEX35ERHANK-Z4\root/Microsoft/Windows/Storage/Providers_v2\SPACES_PhysicalD
                                   .ObjectId="{a1a1e9dc-31e4-11e6-ba8a-806e6f6e6963}:PD:{256a2559-ce63-5434-1bee-3ff
                                   daa3a7}"
PassThroughClass                 :
PassThroughIds                   :
PassThroughNamespace             :
PassThroughServer                :
UniqueId                         : {256a2559-ce63-5434-1bee-3ff629daa3a7}
Description                      :
FriendlyName                     : SAMSUNG MZHPV512HDGL-000H1
Manufacturer                     :
Model                            : SAMSUNG MZHPV512HDGL-000H1
OperationalDetails               :
PhysicalLocation                 : PCI Slot 4 : Adapter 0 : Port 0
SerialNumber                     : S1X0NYAGC03193
AdapterSerialNumber              :
AllocatedSize                    : 512110190592
CanPool                          : False
DeviceId                         : 0
EnclosureNumber                  :
FirmwareVersion                  : BXW24H0Q
IsIndicationEnabled              :
IsPartial                        : True
LogicalSectorSize                : 512
OtherCannotPoolReasonDescription :
PartNumber                       :
PhysicalSectorSize               : 512
Size                             : 512110190592
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
    assert test_disk.bustype == 'SATA'


def test_differentiating_between_internal_and_external_drives():
    assert test_disk.is_internal


def test_is_external_drive_returns_false():
    assert not test_disk.is_external


def test_readability_for_storage_property():
    assert test_disk.size == '512 GB'


def test_whether_a_drive_is_solid_state_or_spinner():
    assert test_disk.type == 'SSD'


def test_is_ssd_returns_true():
    assert test_disk.is_ssd


def test_getting_the_friendly_name_of_a_device():
    assert test_disk.device_name == 'SAMSUNG MZHPV512HDGL-000H1'


def test_device_location_property_returns_correctly():
    assert test_disk.device_location == 'Internal'
