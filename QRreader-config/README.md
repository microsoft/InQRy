# QR Code Reader Configuration

## Requirements
- CR1400 series QR code reader by Code Corp.
- [CortexTools](http://www.codecorp.com/assets/download/D009015-CortexTools-2-5-26-Software.zip) (Windows only)
- rules.js file specific to InQRy (included in this repository)
- QR config codes specific to InQRy (included, also available from [Code Corp Support](http://www.codecorp.com/ConfigGuide/?product=CR1400-XHD))

## Configuration
1. Launch the CortexTools software and connect the reader via USB
2. Upon recognizing the reader, CortexTools will ask to switch it into "USB HID mode", choose yes as this is required to upload the rules file.
3. After the reader finishes switching, navigate to the file using "Open File". The rules.js is prefixed with a `.` (rendering it invisible), so you may find it easier to enter the path directly.
4. Once the rules.js file is displayed in the "Files to download to the reader" bar, click "Download File" and wait for the reader to complete the process.
5. Before closing CortexTools, click the keyboard icon to switch the reader back into "USB Keyboard mode" to prepare for the config codes in the next step.
6. Scan the config QR codes in the following order:
  1. **A4 - Alternative Operating System (Linux/Mac) On**
  2. **A2 - Suffix Tab (USB Keyboard Mode Only)**
  3. **B3 - Reboot Reader**
  4. **B2 - Save All Reader Settings - Default**
7. Test that the reader properly scans an InQRy QR code into the New Asset page of Snipe-IT. If it does not, start by scanning the Reboot Reader code and apply the four codes in the A4-A2-B3-B2 order.
8. Test that the reader maintains the configuration and properly scans InQRy codes after moving it to a new host machine.
