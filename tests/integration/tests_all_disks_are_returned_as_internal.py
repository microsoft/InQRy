from inqry.system_specs import macdisk


def test_all_disks_return_as_internal():
    for disk in macdisk.get_internal_storage():
        assert disk.is_internal
