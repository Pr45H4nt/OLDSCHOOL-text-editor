
# OldSchool Text Editor

**OldSchool Text Editor** is a terminal-based text editor with a classic, typewriter-inspired interface. Built from scratch, this editor provides essential functionalities such as file opening, editing, saving, and features like undo and redo—all without the use of external libraries or resources.

## Features

- **Undo & Redo**: Easily revert or redo your recent changes.
- **File Operations**: Open existing files or create new ones directly from the terminal.
- **Text Editing**: Type, edit, and modify text with keyboard shortcuts.
- **File Saving**: Save your work with a single command.
- **Clear Screen**: Quickly clear the screen to focus on your content.
- **Special Commands**: Includes specific commands to streamline text management.

## Special Commands

- `//undo` - Undo the last action.
- `//redo` - Redo the last undone action.
- `//save <filename>` - Save the current text to the specified filename. If no filename is given, the editor will save to the current file path.
- `//open <filename>` - Open an existing file for editing.
- `//del` - Clear all content.
- `//dc <num>` - Delete a specified number of characters, functioning like a backspace.
- `//br` - Insert a new line.
- `//help` - Display a help message with a list of available commands.

## Getting Started

### Prerequisites

- **Python 3.x**

### Installation

1. Clone the repository (if applicable) or copy the script to your local machine.
2. Make sure you have Python 3 installed on your machine.

### Running the Editor

1. Open a terminal.
2. Run the script with the following command:

   ```bash
   python oldschool_text_editor.py
   ```

3. Start typing and use the available commands to interact with the editor.

## Usage

Simply follow the prompts within the editor and use the listed commands to manage your text. The editor automatically maintains a small state history to enable undo and redo functionality.

## Example

```
$ python oldschool_text_editor.py
OldSchool NOTEPAD BY PRASH

use '//help' for info about functions
----------------------------

->> Hello, world!
->> //save my_file.txt
```


---

Enjoy the nostalgia and efficiency of the OldSchool Text Editor, bringing the typewriter feel to your terminal!
