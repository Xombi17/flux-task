import sys
import os

class UI:
    """
    Zero-dependency UI helper for beautiful CLI output using ANSI codes.
    """
    
    # ANSI Colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    
    # Icons
    ICON_FLUX = "⚡"
    ICON_SUCCESS = "✔"
    ICON_ERROR = "✖"
    ICON_WARN = "⚠"
    ICON_INFO = "ℹ"
    ICON_FOLDER = "📂"
    ICON_FILE = "📄"
    ICON_ARROW = "➜"

    def __init__(self):
        # Enable ANSI support on Windows if needed
        if sys.platform == "win32":
            os.system('color')

    def print_banner(self):
        print(f"\n{self.BOLD}{self.BLUE}Flux {self.ICON_FLUX}{self.RESET}  {self.CYAN}Intelligent Directory Organizer{self.RESET}\n")

    def print_success(self, message: str):
        print(f"{self.GREEN}{self.ICON_SUCCESS} {message}{self.RESET}")

    def print_error(self, message: str):
        print(f"{self.RED}{self.ICON_ERROR} {message}{self.RESET}")

    def print_warning(self, message: str):
        print(f"{self.YELLOW}{self.ICON_WARN} {message}{self.RESET}")

    def print_info(self, message: str):
        print(f"{self.BLUE}{self.ICON_INFO} {message}{self.RESET}")

    def print_table(self, title: str, headers: list, rows: list):
        """
        Prints a nicely formatted table without external constraints.
        """
        if not rows:
            return

        print(f"\n{self.BOLD}{title}{self.RESET}")
        
        # Calculate column widths
        widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))
        
        # Add padding
        widths = [w + 2 for w in widths]
        
        # Print Header
        header_str = "".join(h.ljust(w) for h, w in zip(headers, widths))
        print(f"{self.CYAN}{header_str}{self.RESET}")
        print("-" * sum(widths))
        
        # Print Rows
        for row in rows:
            row_str = "".join(str(cell).ljust(w) for cell, w in zip(row, widths))
            print(row_str)
        print()
