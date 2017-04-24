## InQRy
Obtains machine hardware specifications and generates a QR code containing the data.

### Requirements
- Python 3.4.4 or later ([Homebrew](https://brew.sh/) installed version of Python 3 is recommended)

#### Install
- clone the repository
- `cd InQRy`
- `pip3 install .`
- `python3 InQRy.py`

Once InQRy is installed, you can then access the InQRy API from the Python interpreter with `import inqry`

#### Build
##### Mac
###### Requirements
- OS X 10.10 or later (OS X 10.10 is recommended for forward compatibility)
- Xcode Command Line Tools (7.2.0)
- py2app (0.12) (`pip3 install py2app`)

###### Instructions
- clone the repository
- `python3 setup.py py2app --iconfile inqry.icns`
- **InQRy.app** is in `dist/`

##### Windows
###### Requirements
- Windows 10
- Python 3.4.4 (required)
- pyinstaller (3.3dev)

###### Instructions
- clone the repository
- `pyinstaller --onefile --windowed --icon inqry.ico InQRy.py`
- **InQRy.exe** is in `dist/`

#### Description
InQRy is a cross-platform application that generates a single QR code containing the machine's hardware
specifications. This application is designed primarily to be used during a physical inventory procedure.

The QR code contains detailed information about the client machine or device,
which can then be scanned it quickly add assets into a Snipe-IT database.

##### How It Works

InQRy obtains hardware specs using shell commands and parses the output for
the desired information. It then takes that information, processes it and
instructs the `qrcode` Python module to create a QR code, which is displayed
on the screen for scanning.

InQRy determines which instructions to follow based on the
machine itself. Those instructions contain other necessary information that
allow it to move fluidly through different types of fields in the Snipe-IT asset
entry form.

InQRy was written to obtain asset information quickly and accurately for both
an initial physical inventory procedure, as well as subsequent hardware audits.

#### Currently Supported Platforms
- OS X 10.10 or later
- Windows 10

##### Issues? Suggestions? Questions?
- Submit a bug: [aka.ms/hubenglabsr](https://office.visualstudio.com/DefaultCollection/APEX/Lab-Support/_dashboards?activeDashboardId=88948f37-eb9b-4b40-a59a-b615aff02d4d)
- Email: [apxlab@microsoft.com](mailto:apxlab@microsoft.com)
- Slack (apex-autoinfra.slack.com): **#inqry**

###### For bug submission or emails
- Title should be formatted as "**InQRy:** _short description here_"
- Body should contain a longer description with steps to reproduce, screen shots, etc.

