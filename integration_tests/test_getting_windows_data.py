from inqry.system_specs import windows_system_profiler


def test_hardware_function_returns_dictionary():
    result = windows_system_profiler.hardware()
    assert isinstance(result, dict)


def test_human_readable_functionality():
    win = windows_system_profiler.WindowsProfile()
    assert win.human_readable(46523456754) == "47 GB"


def test_username_parses_correctly():
    win = windows_system_profiler.WindowsProfile()
    assert win.split_name("APEX35-2345\\Bob Saget") == "Bob Saget"
