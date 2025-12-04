# kpop_demon_hunter-Project

A collection of Python and Bash tools including a Huntrix game, cube timer, typing test, and more.

## Requirements

- Python 3.6+
- `rich` library

## Installation

### Termux (Android)

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and Git
pkg install python git -y

# Clone the repository
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project

# Install Python dependencies
pip install -r requirement.txt

# (Optional) Run the Termux installer for additional tools
bash termux-installer.sh
```

### Linux (Debian/Ubuntu)

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python and Git
sudo apt install python3 python3-pip git -y

# Clone the repository
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project

# Install Python dependencies
pip3 install -r requirement.txt
```

### Linux (Fedora/RHEL/CentOS)

```bash
# Update packages
sudo dnf update -y

# Install Python and Git
sudo dnf install python3 python3-pip git -y

# Clone the repository
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project

# Install Python dependencies
pip3 install -r requirement.txt
```

### Linux (Arch Linux)

```bash
# Update packages
sudo pacman -Syu

# Install Python and Git
sudo pacman -S python python-pip git

# Clone the repository
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project

# Install Python dependencies
pip install -r requirement.txt
```

### macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and Git
brew install python git

# Clone the repository
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project

# Install Python dependencies
pip3 install -r requirement.txt
```

### Windows 10/11

#### Option 1: Using Git Bash
1. Download and install [Git for Windows](https://git-scm.com/download/win)
2. Download and install [Python](https://www.python.org/downloads/windows/) (check "Add Python to PATH")
3. Open Git Bash and run:
```bash
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install -r requirement.txt
```

#### Option 2: Using PowerShell
```powershell
# Install Python from Microsoft Store or python.org
# Then run:
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install -r requirement.txt
```

#### Option 3: Using WSL (Windows Subsystem for Linux)
```bash
# Install WSL (run in PowerShell as Administrator)
wsl --install

# After restart, open Ubuntu terminal and run:
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip3 install -r requirement.txt
```

### Windows 8/8.1

1. Download and install [Python 3.8](https://www.python.org/downloads/release/python-3810/) (check "Add Python to PATH")
2. Download and install [Git for Windows](https://git-scm.com/download/win)
3. Open Command Prompt or Git Bash:
```cmd
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install -r requirement.txt
```

### Windows 7

1. Download and install [Python 3.8](https://www.python.org/downloads/release/python-3810/) (last version supporting Windows 7)
2. Download and install [Git for Windows](https://git-scm.com/download/win)
3. Open Command Prompt or Git Bash:
```cmd
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install -r requirement.txt
```

### Windows XP/Vista (Legacy)

> **Note:** These versions are no longer supported. Use at your own risk.

1. Download [Python 3.4](https://www.python.org/downloads/release/python-344/) (last version for XP/Vista)
2. Download [Git for Windows (older version)](https://github.com/git-for-windows/git/releases/tag/v2.10.0.windows.1)
3. Open Command Prompt:
```cmd
git clone https://github.com/YOUR_USERNAME/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install rich
```

## Usage

To run these tools using Python and Bash:
```bash
# Run Python scripts
python3 yourcode.py

# Run Bash scripts
bash yourcode.sh
```

### Examples:
```bash
# Hunter CLI
python3 hunter-cli.py

# Huntrix Game
python3 huntrix_game.py

# Cube Timer
python3 advanced-cube-timer.py
# or
bash cube-timer.sh

# Typing Test
bash typing_test.sh
```

## License

This project is open source.
