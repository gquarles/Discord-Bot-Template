# Discord-Bot-Template
![Codebase](https://img.shields.io/badge/code-Python3.6-blue.svg) [![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://raw.githubusercontent.com/gquarles/Discord-Bot-Template/master/LICENSE)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/gquarles/Discord-Bot-Template.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/gquarles/Discord-Bot-Template/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/gquarles/Discord-Bot-Template.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/gquarles/Discord-Bot-Template/alerts/)


## Getting Started

### Prerequisites
> Python 3.6.0

### Installation
1. Clone the repo into a directory
2. `python -m pip install -r requirements.txt`
3. Edit token.json with your  bot token
4. Run the bot with `python bot.py`

## Usage
This bot is a template for anyone wanting to quickly prototype with custom commands using batch files and a discord bot. Place batch files for the commands inside the same directory as the bot.

#### Adding Commands
Making custom commands is very simple and requires 4 parameters.
1. The command itself
2. The Discord channel the command will be used in
3. The text the bot will say when the command is ran
4. The batch file the bot will run when the command is used

Inside the bot.py file under the line that says `# Add Commands Here` add commands using the following syntax

`Command('!test', 'discord-channel', 'The command works!', 'test.bat')`
