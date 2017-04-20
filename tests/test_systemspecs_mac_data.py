from inqry.system_specs import systemspecs

DATA = {'Model Name': 'Mac Pro',
        'Model Identifier': 'MacPro6,1',
        'Processor Name': 'Quad-Core Intel Xeon E5',
        'Processor Speed': '3.7 GHz',
        'Number of Processors': 1,
        'Total Number of Cores': 4,
        'L2 Cache (per Core)': '256 KB',
        'L3 Cache': '10 MB',
        'Memory': '32 GB',
        'Boot ROM Version': 'MP61.0116.B21',
        'SMC Version (system)': '2.20f18',
        'Illumination Version': '1.4a6',
        'Serial Number (system)': 'F5KQH0P9F9VN',
        'Hardware UUID': '4D4C19C7-19C4-5678-A936-A419C4609AFD'}

SYSTEM_SPECS = systemspecs.SystemSpecs(DATA)
