from inqry import form_instructions
from tests.generic.test_systemspecs_mac_data import MAC_SYSTEM_SPECS


def test_form_instructions_object_instantiates():
    assert form_instructions.FormInstructions(MAC_SYSTEM_SPECS)


def test_get_instructions_method():
    instructions = form_instructions.FormInstructions(MAC_SYSTEM_SPECS)
    assert instructions.new_asset('1234567', 'admin',
                                  'Desktop') == '~d1234567~d~t~d ~dMacPro6,1~d~e~d~t~d3.7 GHz Quad-Core Intel Xeon E5~d~t~d32 GB~d~t~d3.0 TB HDD (APPLE HDD ST3000DM001)~d~t~d121.3 GB SSD (APPLE SSD SM0128G)~d~t~d~t~d~t~d ~dReady~d~e~d~t~d ~d(admin)~d~e~d~t~dF5KQH0P9F9VN'
