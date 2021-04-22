# Bootstrapping the raspberry pi

```
sudo apt-get install git python3-venv python3-dev
```

# Set up a development environment

1. Clone the repo
2. `cd deadstream`
2. Run `python -m venv env` to create a python virtual environment
3. Activate the virtual environment by `source env/bin/activate`
4. Run `pip install -r requirements.txt` to install required packages (into the virtual environment)

# MPV (libmpv) on Fedora

Fedora's package repository does not have mpv, but it is in the RPM Fusion repository.

Follow the instructions at https://rpmfusion.org/Configuration/ to enable the RPM Fusion
repository.

```bash
dnf install \
    https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
    https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Once Fusion is enabled, install libmpv.

```bash
dnf install mpv-libs-devel
```

# Tox complaining about missing modules

If you make a change that requires re-building the tox virtual environment(s),
such as changing the `install_requires` in `setup.py`, use:

```
tox --recreate
```

This will force tox to rebuild its virtual environments.

# Pins

| Audio Label | Audio pin | RPi pin | GPIO | current use |
| --- | --- | --- | --- | --- |
| SDA | 1 | 3 | 2 (SDAI2C)| stop button|
| SCL | 2 | 5 | 3 (SCLI2C) | rewind button |
| TX | 3 | 8 | 14 (UART TX) |
| RX | 4 | 10 | 15 (UART RX) |
| 4 | 5 | 7 | 4 | select button |
| 17 | 6 | 11 | 17 | day dt |
| 18 | 7 | 12 | 18 (used by Audio Card!!!) |  |
| 27 | 8 | 13 | 27 | day sw |
| 22 | 9 | 15 | 22 | year dt |
| 23 | 10 | 16 | 23 | year sw |
| 23 | 11 | 18 | 24 (screen A0)| screen A0 |
| 25 | 12 | 22 | 25 (screen reset)| screen reset |
| MOS | 13 | 19 | 10 (MOSI) (screen SDA) | screen SDA |
| MIS | 14 | 21 | 9 (MISO) |
| CLK | 15 | 23 | 11 (SCLK) (screen SCK) | screen SCK |
| CE0 | 16 | 24 | 8 (CE0_N) (screen CS) | screen CS |
| CE1 | 17 | 26 | 7 (CE1_N) |
| 5 | 18 | 29 | 5 | month dt |
| 6 | 19 | 31 | 6 | month sw |
| 12 | 20 | 32 | 12 | month cl |
| 13 | 21 | 33 | 13 | day cl |
| 16 | 22 | 36 | 16 | year cl |
| 19 | 23 | 37 | 26 |  ffwd button |
| 20 | 24 | 38 | 20 |  play/pause button |
| 21 | 25 | 40 | 21 | (Used by Audio Card!!!) |