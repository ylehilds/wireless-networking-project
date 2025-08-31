# Wireless Networking Project — ESP32 ↔ Windows Bluetooth Audio

A portfolio-ready wireless networking build that connects an **ESP32** to a **Windows host** over **Bluetooth** to stream and control audio (`.wav` files). Physical buttons on the ESP32 send commands (play/pause, next, previous) to the Windows client, which streams audio back to the ESP32. This repo includes the embedded firmware, the Windows Python client, documentation (report & slides), schematics, and example sounds.

## Overview
- **Goal:** Demonstrate end-to-end Bluetooth communication between a microcontroller (ESP32) and a desktop host (Windows), including command/control and audio streaming.
- **How it works:**
    1) ESP32 firmware exposes a Bluetooth device and reads button presses.
    2) Button presses send short command bytes (`'p'`, `'n'`, `'q'`) to the host.
    3) The Windows Python client receives commands and streams `.wav` audio back to the ESP32.
- **Why it’s cool:** It blends embedded development, Bluetooth networking, Python scripting, and basic audio handling—plus real hardware wiring with a documented schematic.

## Features
- **ESP32 firmware** (`.ino`): Bluetooth setup, command transmission on button presses, receive audio stream.
- **Windows Python client** (`wav_bt.py`): Connects to the ESP32 via Bluetooth (PyBluez), interprets commands, and streams `.wav` clips (loop or playlist).
- **Hardware buttons** → **Host actions** mapping:
    - GPIO 22 → `'p'` → Play/Pause
    - GPIO 23 → `'n'` → Next track
    - GPIO 21 → `'q'` → Previous track
- **Documentation & assets:**
    - Hardware and design docs: `BluetoothProjectReport.pdf`, `FinalProjectSlides.pdf`
    - Schematic: `breadboardSchematic.png` and `schematic/`
    - Media: `sounds/` (sample clips) and `sorry_dave.wav` (example)

## Tech Stack
- **Microcontroller:** ESP32 (Arduino framework)
- **Host:** Windows 11+ with Python 3.x
- **Bluetooth library:** PyBluez (Windows build may require Visual Studio Build Tools)
- **Audio format:** `.wav` (PCM WAV files tested)
- **Optional helpers:** Additional Python modules as needed (see `requirements.txt`)

## Repository Structure (key items)
- `bt/ESP32BluetoothReceivingData/ESP32BluetoothReceivingData.ino` — ESP32 Arduino sketch (Bluetooth + buttons + stream handling)
- `bt/wav_bt.py` — Windows Python Bluetooth client (command handler + WAV streaming)
- `sounds/` — example `.wav` audio clips
- `sorry_dave.wav` — sample audio file
- `BluetoothProjectReport.pdf`, `FinalProjectSlides.pdf` — project documentation
- `breadboardSchematic.png`, `schematic/` — hardware schematic & tool files
- `digital_pot/`, `speaker_test/`, `wav_echo/` — supporting experiments/utilities
- `wav.py` — helper script for WAV handling (if used by client)
- `requirements.txt` — Python deps (ensure PyBluez is installed on Windows)

## Getting Started

### 1) Clone the repository
    git clone https://github.com/ylehilds/wireless-networking-project.git
    cd wireless-networking-project

### 2) Flash the ESP32
- Open **Arduino IDE** and load:
  bt/ESP32BluetoothReceivingData/ESP32BluetoothReceivingData.ino
- Select the correct **ESP32 board** and COM port, then **Upload**.
- Wire three momentary buttons to the ESP32 pins with appropriate pull-ups/pull-downs:
    - Play/Pause → **GPIO 22**
    - Next → **GPIO 23**
    - Previous → **GPIO 21**
- After flashing, the ESP32 should advertise a Bluetooth device (default name often **ESP32test**).

### 3) Prepare the Windows Host (Python)
- Install **Python 3.x** (add to PATH).
- **Install PyBluez**. On Windows, you may need build tools:
    - Install **Visual Studio Build Tools 2017** with **Visual C++ build tools** and **UWP build tools**.
    - Then install PyBluez (try `pip` first; if needed, build from source):
      pip install pybluez
      or
      git clone https://github.com/pybluez/pybluez
      cd pybluez
      python setup.py install --user
- If present, install any additional requirements:
  pip install -r requirements.txt

### 4) Pair Windows with the ESP32
- In Windows **Bluetooth settings**, pair with the device (e.g., **ESP32test**).
- Confirm the COM port or BLE handle is accessible (depending on your PyBluez usage).

### 5) Run the Python Client
- From the repo root (or provide absolute paths), run:
  python bt/wav_bt.py sounds/
- The client will connect to the paired ESP32 and prepare to stream `.wav` files found in `sounds/`.
- Press the ESP32 buttons to control playback:
    - GPIO 22 → `'p'` → Play/Pause
    - GPIO 23 → `'n'` → Next track
    - GPIO 21 → `'q'` → Previous track

## Audio Files & Formats
- Place additional `.wav` files in the `sounds/` directory to expand your playlist.
- For testing, short PCM WAV files work best. A public source with small clips (e.g., movie quotes) can be handy.
- Large or compressed formats are not recommended for the first pass.

## Troubleshooting
- **PyBluez install fails on Windows:**
    - Ensure **Visual Studio Build Tools 2017** (C++ + UWP) are installed.
    - Try `pip install pybluez` first; if it fails, build from source as shown above.
- **Cannot find ESP32 device:**
    - Reboot the ESP32 and re-open the Arduino Serial Monitor to ensure it’s running.
    - Remove and re-pair the device in Windows Bluetooth settings.
- **No audio / choppy audio:**
    - Try shorter/lower sample rate WAV files.
    - Check buffer sizes and latency in the Python script (and any serial/BT throughput limitations).
- **Buttons not registering:**
    - Verify wiring and pull-up/down configuration.
    - Confirm pin numbers match the firmware (22, 23, 21).
- **Permission/port errors:**
    - Run the Python terminal as Administrator if necessary.
    - Verify the correct adapter/service is used by PyBluez on your system.

## Hardware & Documentation
- **Schematic:** `breadboardSchematic.png` (and detailed files in `schematic/`).
- **Photo:** `breadboardPic.jpg` shows the physical assembly.
- **Write-up:** `BluetoothProjectReport.pdf` explains the architecture, rationale, and challenges.
- **Slides:** `FinalProjectSlides.pdf` summarizes the project visually for presentations.

## Why It’s Portfolio-Worthy
- **Full-stack embedded networking:** Integrates microcontroller firmware, desktop scripting, and Bluetooth transport.
- **Real hardware + real constraints:** Debugging pairing, throughput, and latency mirrors industry scenarios.
- **Clear artifacts:** Schematics, photos, report, and slides make the project easy to understand and demo.
- **Extendable:** Swap audio formats, add OLED status, rework to BLE GATT, port client to Linux/macOS, or add a mobile app.

# Notes

1. The file to push to ESP32 is located at: wireless-networking-project/bt/ESP32BluetoothReceivingData/ESP32BluetoothReceivingData.ino
2. The file to be running on a Windows 11 + is located at: wireless-networking-project/bt/wav_bt.py. You need python 3 and bluetooth library, follow these steps to make sure you have the correct python libraries:

3. Download and run "Visual Studio Installer": https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
4. Install "Visual Studio Build Tools 2017", check "Visual C++ build tools" and "Universal Windows Platform build tools"
5. ```git clone https://github.com/pybluez/pybluez```
6. ```cd pybluez```
7. ```python setup.py install``` you may need to add --user flag at the end for this to work

8. once all libraries are installed correctly, then run the python file like this:</p>
9. on Windows connect to ESP32 bluetooth by name, which should be: "ESP32test" then run the below python script (python <full_path_for_wav_bt.py> <full_path_for_sounds_folder>):
10. ```python C:\Users\lehid\OneDrive\Documents\repos\wireless-networking-project\bt\wav_bt.py C:\Users\lehid\OneDrive\Documents\repos\wireless-networking-project\sounds\```

11. now there should be a complete bluetooth interaction between ESP32 and Windows python script, where ESP32 buttons sends commands like "p,n,q" and the python script sends wav files data on an infinite loop:
```
    ESP32: pin playPause = 22; Python: 'p'
    ESP32: pin next = 23; Python: 'n'
    ESP32: pin prev = 21; Python: 'q'
```
PS: Schematic and discussion how this project came to be is found in the BluetoothProjectReport.pdf / FinalProjectSlides.pdf / breadboardSchematic.png file or look at schematic folder which contain the schematic and software to see it.
<p>PS2: add more wav clip sounds from here: https://www.wavsource.com/movies/movies1.htm I have found that it works well with this project.</p>

## License & Author
- **License:** MIT — see `LICENSE`
- **Author:** Lehi Alcantara — https://www.lehi.dev — lehi@lehi.dev
