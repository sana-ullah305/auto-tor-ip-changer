# auto-tor-ip-changer
Python tool for seamless IP changes using Tor on Linux and simulated Tor-like behavior on Windows. User-friendly, dependency-aware, with installation options.


Certainly! Below is the README.md content with GitHub styling and headings:

```markdown
# AutoTor IP Changer

## Overview

The AutoTor IP Changer is a Python script designed to automate the process of IP address rotation utilizing the Tor network. By seamlessly integrating with Tor, this script facilitates anonymized web interactions, enhancing privacy and security during online activities.

## Prerequisites

1. **Python 3.x:** Ensure that Python 3.x is installed on your system.
2. **Tor Browser:** Install the Tor Browser to leverage the Tor network for IP anonymization.
3. **Tor (if not using Tor Browser):** If the Tor Browser is not installed, download and install the Tor Browser or the standalone Tor software from the [official Tor Project website](https://www.torproject.org/).

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sana-ullah305/auto-tor-ip-changer.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd auto-tor-ip-changer
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The AutoTor script provides an interactive configuration process to tailor its behavior to specific requirements.

### 1. Tor Proxy Configuration

- When prompted, specify the Tor proxy. The default is `socks5://127.0.0.1:9050`.
- Example: `socks5://127.0.0.1:9050`

### 2. IP Change Settings

- Define the time interval between IP changes in seconds. The default is 60 seconds.
- Specify the number of times to change your IP. Enter `0` for infinite IP changes.

## Browser Configuration

### Firefox

To use the script with Firefox:

1. **Install Firefox:**
   Ensure that Firefox is installed on your machine. If not, download it from the [official Firefox website](https://www.mozilla.org/firefox/).

2. **Configure Firefox Proxy Settings:**
   - Open Firefox.
   - Navigate to the menu (three horizontal lines in the upper right corner) and select "Options" or "Preferences."
   - Scroll down to the "Network Settings" section.
   - Click on the "Settings" button.
   - Choose "Manual proxy configuration."
   - Set the SOCKS Host to `127.0.0.1` and the Port to `9050`. Make sure to select SOCKS v5.
   - Click "OK" to save the settings.

### Other Browsers

For browsers other than Firefox, you can use the Tor Browser itself, which comes pre-configured with Tor. Alternatively, manually configure the proxy settings of the respective browser to use the Tor proxy (`127.0.0.1:9050`).

## Usage

Execute the script with the following command:

```bash
python auto_tor.py
```

Follow the prompts to configure the Tor proxy and IP change settings according to your preferences.

## Example

```bash
[+] Enter the Tor proxy (default: socks5://127.0.0.1:9050):
[+] Time to change IP in seconds [type=60] >> 60
[+] How many times do you want to change your IP [type=1000] for infinite IP change type [0] >> 0
```

## Notes

- The script utilizes the `requests` library for making requests through the Tor network. It will be automatically installed during the first run if not present.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project acknowledges the contributions of the Tor Project for providing the Tor Browser and network infrastructure for anonymous communication.

## Troubleshooting

If you encounter issues or require further assistance, please open an issue on the [GitHub repository](https://github.com/sana-ullah305/auto-tor-ip-changer/issues).

## Contributing

Contributions are welcome. For improvement ideas or bug reports, please submit a pull request or open an issue on GitHub.

## Author

Sanaullah

## Version

1.0.0 (January 2024)

---

**Disclaimer:** This script is intended for educational purposes only. Users are advised to employ this tool responsibly and be mindful of legal considerations related to network activities in their respective regions.
```

Feel free to copy and paste this content into your README.md file on GitHub.