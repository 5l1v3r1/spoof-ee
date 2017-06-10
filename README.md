# Spoofee - Spoof your MAC address

 a node.js port of this package.*

### For OS X, Windows, and Linux (most flavors)

 Python script and change your MAC address
in one command. *Now for Windows and Linux, too!*

## Installation




If you're not using the system Python (because you use Homebrew, for example), make sure you add '/usr/local/share/python/' (or equivalent) to your path.



SpoofMAC installs a command-line script called `spoofee.py`. You can always
see up-to-date usage instructions by typing `spoofee.py --help`.

### Examples

Some short usage examples.

#### List available devices:

```bash
spoof-mac.py list
- "Ethernet" on device "en0" with MAC address 70:56:51:BE:B3:00
- "Wi-Fi" on device "en1" with MAC address 70:56:51:BE:B3:01 currently set to 70:56:51:BE:B3:02
- "Bluetooth PAN" on device "en1"
```

#### List available devices, but only those on wifi:

```bash
spoof-mac.py list --wifi
- "Wi-Fi" on device "en0" with MAC address 70:56:51:BE:B3:6F
```

#### Randomize MAC address *(requires root)*

You can use the hardware port name, such as:

```bash
spoof-mac.py randomize wi-fi
```

or the device name, such as:

```bash
spoof-mac.py randomize en0
```

#### Set device MAC address to something specific *(requires root)*

```bash
spoof-mac.py set 00:00:00:00:00:00 en0
```

#### Reset device to its original MAC address *(requires root)*

While not always possible (because the original physical MAC isn't
available), you can try setting the MAC address of a device back
to its burned-in address using `reset`:

```bash
spoof-mac.py reset wi-fi
```

(older versions of OS X may call it "airport" instead of "wi-fi")

Another option to reset your MAC address is to simply restart your computer.
OS X doesn't store changes to your MAC address between restarts. If you want
to make change your MAC address and have it persist between restarts, read
the next section.


## Optional: Run automatically at startup

OS X doesn't let you permanently change your MAC address. Every time you restart your computer, your address gets reset back to whatever it was before. Fortunately, SpoofMAC can easily be set to run at startup time so your computer will always have the MAC address you want.

### Startup Installation Instructions

 run the following commands in Terminal:


# Customize location of `spoofee.py` to match your system
cat local.macspoof.plist | sed "s|/usr/local/bin/spoofee.py|`which spoofee.py`|" | tee local.macspoof.plist

# Copy file to the OS X launchd folder
sudo cp local.macspoof.plist /Library/LaunchDaemons

# Set file permissions
cd /Library/LaunchDaemons
sudo chown root:wheel local.macspoof.plist
sudo chmod 0644 local.macspoof.plist
```

By default, the above will randomize your MAC address on computer startup. You can change the command that gets run at startup by editing the `local.macspoof.plist` file.

```bash
sudo vim /Library/LaunchDaemons/local.macspoof.plist
```

## Changelog

- 2.1.1 - Use `ip` command when available, in more situations
- 2.1.0 - Use `ip` command when available; `ifconfig` is deprecated on Arch Linux
- 2.0.6 - Increase MAC address randomness
- 2.0.5 - Allow 2nd character in MAC address to be a letter 
- 2.0.4 - Warn when trying to use a multicast address
- 2.0.3 - More Python 2.7 compatibility fixes
- 2.0.2 - Python 2.7 compatibility fixes
- **2.0.0 - Python 3 support**
- 1.2.2 - Fix for Ubuntu 14.04
- 1.2.1 - Fix line endings (dos2unix)
- **1.2.0 - Add Windows and Linux support (thanks CJ!)**
- 1.1.1 - Fix "ValueError: too many values to unpack" error
- 1.1.0 - Fix regression: List command now shows current MAC address
- **0.0.0 - Original version (r0otz-ee)**



*Improvements welcome! (please add yourself to the list)*

