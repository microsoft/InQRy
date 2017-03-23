from inqry.system_specs import get_physicaldisk

UNIQUE_ID_OUTPUT = """
UniqueId
--------
{256a2559-ce63-5434-1bee-3ff629daa3a7}
{4069d186-f178-856e-cff3-ba250c28446d}
{4da19f06-2e28-2722-a0fb-33c02696abcd}
50014EE20D887D66
"""


def test_creating_list_of_unique_disk_ids():
    expected_physical_disks = ['{256a2559-ce63-5434-1bee-3ff629daa3a7}',
                               '{4069d186-f178-856e-cff3-ba250c28446d}',
                               '{4da19f06-2e28-2722-a0fb-33c02696abcd}',
                               '50014EE20D887D66']
    assert expected_physical_disks == get_physicaldisk.get_physical_disk_identifiers(UNIQUE_ID_OUTPUT)
