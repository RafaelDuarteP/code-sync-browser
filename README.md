# Code Sync Browser

## Overview
This Python script provides a simple solution for automatically reloading a web page whenever specified file types within a monitored directory are modified. It utilizes the `watchdog` library to monitor file system events and the `selenium` library for browser automation.

## Features
- Supports various web browsers: Firefox, Chrome, Edge, and Safari.
- Monitors a specified folder for changes in specified file extensions.
- Reloads the web page upon detecting a file modification.

## Requirements
- Python 3.x
- Dependencies: `watchdog`, `selenium`

## Installation
1. Install the required dependencies:
    ```bash
    pip install watchdog selenium
    ```

2. Download the script `code_sync_browser.py`.

## Usage

### Command Line Options
- `--browser` (`-b`): Browser type. Choices: ['firefox', 'chrome', 'edge', 'safari'].
- `--path` (`-p`): Path to the folder to watch for changes.
- `--url` (`-u`): Page URL to open in the browser.
- `--extensions` (`-e`): Extensions to watch for changes.
- `--recursive` (`-r`): Watch subfolders recursively.

### Example
```bash
python code_sync_browser.py -b chrome -p /path/to/watch -u http://example.com -e .html .css -r
```

## License
This script is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting pull requests.

## Acknowledgments
- This script uses the `watchdog` and `selenium` libraries.

---

**Note:** Make sure to have the appropriate web driver executable for the chosen browser in your system's PATH.

**Disclaimer:** This script is provided as-is without any warranty. Use it responsibly and in compliance with the terms of service of the websites you are automating.