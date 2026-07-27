# SSH Server Check

A lightweight SSH diagnostics utility for Linux servers.

## Features

- SSH connectivity
- CPU information
- CPU load
- RAM usage
- Disk usage
- Public IP detection
- Hostname
- Kernel version
- Operating System
- Python version
- Server time
- Running processes
- JSON export

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Interactive mode:

```bash
python3 main.py
```

Command line:

```bash
python3 main.py --host 192.168.1.10 --user root --password secret
```

JSON reports are saved to:

```text
output/report.json
```

## License

MIT