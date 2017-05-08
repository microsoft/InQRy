from inqry.system_specs import windows_system_profiler


def test_getting_memory_in_gigabytes():
    assert windows_system_profiler.WindowsProfile.get_memory_in_gigabytes(34271739904) == "32 GB"


def test_getting_speed_only_from_wmi32_processor():
    assert windows_system_profiler.WindowsProfile.get_cpu_speed(
        'Intel(R) Xeon(R) CPU E5-1650 v3 @ 3.50GHz') == '3.50GHz'


def test_getting_name_only_from_wmi32_processor():
    assert windows_system_profiler.WindowsProfile.get_cpu_name(
        'Intel(R) Xeon(R) CPU E5-1650 v3 @ 3.50GHz') == 'Intel Xeon CPU E5-1650 v3'
