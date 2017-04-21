from inqry.system_specs import windows_system_profiler


def test_human_readable_functionality():
    assert windows_system_profiler.WindowsProfile.get_memory_in_gigabytes(46523456754) == "47 GB"


def test_getting_speed_only_from_wmi32_processor():
    assert windows_system_profiler.WindowsProfile.get_cpu_speed(
            'Intel(R) Xeon(R) CPU E5-1650 v3 @ 3.50GHz') == '3.50GHz'


def test_getting_name_only_from_wmi32_processor():
    assert windows_system_profiler.WindowsProfile.get_cpu_name(
            'Intel(R) Xeon(R) CPU E5-1650 v3 @ 3.50GHz') == 'Intel(R) Xeon(R) CPU E5-1650 v3'
