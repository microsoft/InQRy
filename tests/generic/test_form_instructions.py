from inqry import barcode, form_instructions

JSON_DATA = '{"os_type": "Darwin", "hardware": {"Model Name": "Mac Pro", "Model Identifier": "MacPro6,1", "Processor Name": "Quad-Core Intel Xeon E5", "Processor Speed": "3.7 GHz", "Number of Processors": 1, "Total Number of Cores": 4, "L2 Cache (per Core)": "256 KB", "L3 Cache": "10 MB", "Memory": "32 GB", "Boot ROM Version": "MP61.0116.B25", "SMC Version (system)": "2.20f18", "Illumination Version": "1.4a6", "Serial Number (system)": "F5KQH0P9F9VN", "Hardware UUID": "4D4C19C7-19C4-5678-A936-A419C4609AFD"}, "storage": {"Drive 1": "1.0 TB SSD (APPLE SSD SM1024G)"}}'

instructions = form_instructions.FormInstructions(JSON_DATA)


def test_barcode_data_delayify():
    assert barcode.delayify('foo') == '~dfoo'


def test_barcode_data_delayify_long():
    assert barcode.delayify('foo', 2) == '~d~dfoo'


def test_barcode_data_textify():
    assert barcode.textify('foo') == '~dfoo~d~t'


def test_barcode_data_listify():
    assert barcode.listify('foo') == '~d\x20~dfoo~d~e~d~t'


def test_form_instructions_object_instantiates():
    assert instructions


def test_get_instructions_method():
    assert instructions.new_asset('1234567', 'admin',
                                  'Desktop') == '~d1234567~d~t~d ~dMacPro6,1~d~e~d~t~d3.7 GHz Quad-Core Intel Xeon E5~d~t~d32 GB~d~t~d1.0 TB SSD (APPLE SSD SM1024G)~d~t~d~t~d~t~d~t~d ~dReady~d~e~d~t~d ~dadmin~d~e~d~t~dF5KQH0P9F9VN'
