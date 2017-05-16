## InQRy
Obtains machine hardware specifications and generates a QR code containing the data.

##### macOS: ![macOS](https://office.visualstudio.com/_apis/public/build/definitions/59d72877-1cea-4eb6-9d06-66716573631a/1174/badge)
##### Windows: ![Windows](https://office.visualstudio.com/_apis/public/build/definitions/59d72877-1cea-4eb6-9d06-66716573631a/1167/badge)

### Install (run from the command line)
 
##### Requirements
- Python 3.4.4 or later
- Note: If you are using the ([Homebrew](https://brew.sh/)-installed version of Python, the Python commands below will need to be appended with `3`. For example, `python` is `python3`, `pip` is `pip3`, etc.

##### Instructions
- clone the repository
- `cd InQRy`
- `pip install .`
- Run: `python InQRy.py`
- Use the InQRy API from the Python interpreter with `import inqry`

###### Example API usage:
```
>>> from inqry.system_specs import systemspecs
>>> ss = systemspecs.SystemSpecs()
>>> ss.os_type
'Darwin'
>>> ss.memory
'8 GB'
>>> ss.storage
{'Drive 1': '251.0 GB SSD (APPLE SSD AP0256J)'}
```

### Build (run as compiled binary)
#### Mac
##### Requirements
- ([Homebrew](https://brew.sh/)-installed version of Python 3 (`brew install python3`)
- OS X 10.10 or later (OS X 10.10 is recommended for forward compatibility)
- Xcode Command Line Tools (7.2.0)
- py2app (0.12) (`pip install py2app`)

##### Instructions
- clone the repository
- `python setup.py py2app --iconfile icon/inqry.icns`
- **InQRy.app** is in `dist/`

#### Windows
##### Requirements
- Windows 10
- Python 3.4 or 3.5 (32-bit)
    - **Note**: InQRy will **not** build on Python 3.6 or later)
- pyinstaller (3.2.1 or later)

##### Instructions
- clone the repository
- `pyinstaller --onefile --icon icon/inqry.ico InQRy.py`
- **InQRy.exe** is in `dist/`

### Description
InQRy is a cross-platform application that generates a single QR code containing the machine's hardware
specifications. This application is designed primarily to be used during a physical inventory procedure.

The QR code contains detailed information about the client machine or device,
which can then be scanned it quickly add assets into a [Snipe-IT](https://github.com/snipe/snipe-it) database.

### How It Works

InQRy obtains hardware specs using shell commands and parses the output for
the desired information. It then takes that information, processes it and
instructs [python-qrcode](https://github.com/lincolnloop/python-qrcode) to create a QR code, which is displayed
on the screen for scanning.

InQRy determines which instructions to follow based on the
machine itself. Those instructions contain other necessary information that
allow it to move fluidly through different types of fields in the [Snipe-IT](https://github.com/snipe/snipe-it) asset
entry form.

InQRy was written to obtain asset information quickly and accurately for both
an initial physical inventory procedure, as well as subsequent hardware audits.

### Currently Supported Platforms
- OS X 10.10 or later
- Windows 10

#### Issues? Suggestions? Questions?
- Submit a bug: [aka.ms/hubenglabsr](https://office.visualstudio.com/DefaultCollection/APEX/Lab-Support/_dashboards?activeDashboardId=88948f37-eb9b-4b40-a59a-b615aff02d4d)
- Email: [apxlab@microsoft.com](mailto:apxlab@microsoft.com)
- Slack (apex-autoinfra.slack.com): **#inqry**

###### For bug submission or emails
- Title should be formatted as "**InQRy:** _short description here_"
- Body should contain a longer description with steps to reproduce, screen shots, etc.

