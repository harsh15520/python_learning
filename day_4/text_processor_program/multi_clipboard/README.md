The **Multi-Clipboard Automatic Messages** programs, `mclip.py` and `mcb.pyw`, are Python text processing scripts designed to streamline repetitive typing by managing and copying predefined or user-saved text phrases to the clipboard.

### `mclip.py`: Basic Multi-Clipboard Program

The original `mclip.py` program is a straightforward tool that stores multiple text phrases, each associated with a short keyword, within its source code.

**Purpose and Functionality:**
*   It allows users to quickly copy a specific, pre-defined message to their computer's clipboard by running the script with a corresponding keyword as a command-line argument (e.g., `python mclip.py agree`). This eliminates the need to manually type or copy from a separate document.
*   The program is designed to use the `pyperclip` module for interacting with the clipboard, specifically `pyperclip.copy()` to send text to it.
*   **Data Structure:** The key phrases and their associated messages are stored in a Python dictionary named `TEXT` directly within the script's source code.
*   **Command-Line Argument Handling:** It uses the `sys` module to process command-line arguments. `sys.argv` is the script's filename, and `sys.argv` is expected to be the key phrase. If no key phrase is provided, it prints a usage message and exits.
*   **Logic:** The script checks if the provided key phrase exists as a key in the `TEXT` dictionary. If found, the corresponding message is copied to the clipboard, and a confirmation message is printed. If not found, a message indicating no text for that key phrase is displayed.
*   **Updatability:** To add or change messages, a user must manually modify the `TEXT` dictionary in the `mclip.py` source code.
*   **Execution (Windows):** On Windows, a batch file (`mclip.bat`) can be created in the `C:\Windows` folder to allow convenient execution from the Run window (Win-R) by typing `mclip <keyphrase>`.

### `mcb.pyw`: Updatable Multi-Clipboard

The `mcb.pyw` program is an enhanced version of the multi-clipboard concept, offering greater flexibility by allowing users to save and manage text phrases without altering the script's code.

**Improvements and Key Features:**
*   **Persistence:** This version utilizes the `shelve` module to persistently save and load clipboard content, associating each piece of text with a keyword. This means saved phrases remain available even after the program closes.
*   **No Terminal Window:** The `.pyw` file extension on Windows ensures that Python runs the script without displaying a Terminal window, making it less intrusive for background operations.
*   **Usage Modes:** `mcb.pyw` supports multiple modes of operation through command-line arguments:
    *   `py mcb.pyw save <keyword>`: Saves the current content of the clipboard to the shelf file, associated with the specified `<keyword>`.
    *   `py mcb.pyw <keyword>`: Loads the text associated with the given `<keyword>` from the shelf file back into the clipboard.
    *   `py mcb.pyw list`: Copies a string representation of all saved keywords to the clipboard, which the user can then paste into a text editor to view.
*   **Modules Used:** It imports `shelve`, `pyperclip`, and `sys` modules to handle persistent storage, clipboard operations, and command-line arguments, respectively.
*   **Execution (Windows):** Similar to `mclip.py`, a batch file (`mcb.bat`) can be set up on Windows to run `mcb.pyw` easily from the Run... window.
