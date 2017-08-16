import sys
import pytest
if sys.platform == "win32":
    from inqry.system_specs import windows_system_profiler
    windows_profile = windows_system_profiler.WindowsProfile()
else:
    pass


@pytest.mark.win32
def test_getting_memory_in_gigabytes():
    assert windows_system_profiler.WindowsProfile.get_memory_in_gigabytes(34271739904) == "32 GB"


@pytest.mark.win32
def test_getting_speed_only_from_wmi32_processor():
    assert windows_system_profiler.WindowsProfile.get_processor_speed(
        'Intel(R) Xeon(R) CPU E5-1650 v3 @ 3.50GHz') == '3.50GHz'


@pytest.mark.win32
def test_getting_name_only_from_wmi32_processor():
    assert windows_system_profiler.WindowsProfile.get_processor_name(
        'Intel(R) Xeon(R) CPU E5-1650 v3 @ 3.50GHz') == 'Intel Xeon CPU E5-1650 v3'


@pytest.mark.win32
def test_instantiating_a_windows_profiler():
    assert windows_profile
