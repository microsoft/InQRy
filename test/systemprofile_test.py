import pytest
from pybar.system_profiler import SystemProfile


class TestSystemProfile:
    def test_empty_profile_instantiation_works(self):
        SystemProfile()
