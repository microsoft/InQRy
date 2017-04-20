from inqry.system_specs import windows_system_profiler


def test_human_readable_functionality():
    assert windows_system_profiler.human_readable(46523456754) == "47 GB"


def test_username_parses_correctly():
    assert windows_system_profiler.split_name("APEX35-2345\\Johnny Appleseed") == "Johnny Appleseed"
