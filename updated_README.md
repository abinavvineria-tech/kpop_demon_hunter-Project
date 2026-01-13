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
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project

# Install Python dependencies
pip install -r requirement.txt

# (Optional) Run the Termux installer for additional tools
chmod +x termux_installer/termux-installer.sh
bash termux_installer/termux-installer.sh
```

### Linux (Debian/Ubuntu)

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python and Git
sudo apt install python3 python3-pip git -y

# Clone the repository
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
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
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
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
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
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
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
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
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install -r requirement.txt
```

#### Option 2: Using PowerShell
```powershell
# Install Python from Microsoft Store or python.org
# Then run:
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
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
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip3 install -r requirement.txt
```

### Windows 8/8.1

1. Download and install [Python 3.8](https://www.python.org/downloads/release/python-3810/) (check "Add Python to PATH")
2. Download and install [Git for Windows](https://git-scm.com/download/win)
3. Open Command Prompt or Git Bash:
```cmd
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install -r requirement.txt
```

### Windows 7

1. Download and install [Python 3.8](https://www.python.org/downloads/release/python-3810/) (last version supporting Windows 7)
2. Download and install [Git for Windows](https://git-scm.com/download/win)
3. Open Command Prompt or Git Bash:
```cmd
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
cd kpop_demon_hunter-Project
pip install -r requirement.txt
```

### Windows XP/Vista (Legacy)

> **Note:** These versions are no longer supported. Use at your own risk.

1. Download [Python 3.4](https://www.python.org/downloads/release/python-344/) (last version for XP/Vista)
2. Download [Git for Windows (older version)](https://github.com/git-for-windows/git/releases/tag/v2.10.0.windows.1)
3. Open Command Prompt:
```cmd
git clone https://github.com/abinavvineria-tech/kpop_demon_hunter-Project.git
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

## KPop Demon Hunters Website

This repository also includes a fan website for KPop Demon Hunters. To view the website:

1. Locate the `kpop_demon_hunters_website.html` file in the repository
2. Double-click the file to open it in your default web browser
3. Alternatively, you can open it with any web browser by right-clicking and selecting "Open with"

The website features:
- Character profiles for Huntrix (Rumi, Mira, Zoey) and Saja Boys (Jinu, Baby Saja, Mystery Saja, Romance Saja, Abby Saja)
- Plot summary of the KPop Demon Hunters story
- Success metrics and awards information
- Games and merchandise sections

## Publishing to GitHub Pages

To publish the KPop Demon Hunters website to GitHub Pages:

1. Push the `kpop_demon_hunters_website.html` file to your repository
2. Go to your repository settings on GitHub
3. Scroll down to the "Pages" section
4. Under "Source", select "Deploy from a branch"
5. Select the branch (usually main) and save
6. Your website will be available at `https://[username].github.io/kpop_demon_hunter-Project/kpop_demon_hunters_website.html`

## License

This project is open source.