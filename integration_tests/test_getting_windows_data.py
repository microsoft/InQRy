from inqry.system_specs import windows_system_profiler as wsp


def test_hardware_function_returns_dictionary():
    assert isinstance(wsp.collector(), dict)


def test_human_readable_functionality():
    assert wsp.WindowsProfile().human_readable(46523456754) == "47 GB"


def test_username_parses_correctly():
    assert wsp.WindowsProfile().split_name("APEX35-2345\\Johnny Appleseed") == "Johnny Appleseed"
