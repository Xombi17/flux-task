# Flux ⚡
> Intelligent Directory Organizer for busy developers.

## 1. The Problem
We've all been there: a `Downloads` folder with thousands of mixed files—images, PDF receipts, installation binaries, and random Python scripts. Finding anything is a nightmare. Manual sorting is tedious and error-prone.

## 2. The Solution: Flux
**Flux** is a command-line utility that brings order to chaos. It scans a directory, identifies file types, and sorts them into a clean `Category/File` structure.
Key features:
- **🛡️ Safe by Default**: Always preview moves with `--dry-run`.
- **↩️ Undo Capability**: Made a mistake? `flux undo` reverses the last operation instantly.
- **🎨 Beautiful UI**: Rich terminal output makes the process satisfying.

## 3. How to Run

### Prerequisites
- Python 3.8+ (Standard Library only)

### Installation
No external dependencies required!
```bash
git clone <repo_url>
cd flux
```

### Usage

**1. Organize a directory (Preview mode)**
```bash
python -m src.main organize /path/to/folder --dry-run
```

**2. Execute the organization**
```bash
python -m src.main organize /path/to/folder
```

**3. Undo the last change**
```bash
python -m src.main undo /path/to/folder
```

## 4. Design Decisions

### **Robust Classification**
Instead of simple MIME types which can be slow or inaccurate for dev files, I used an **Extension-based Strategy Pattern**. This allows precise grouping of developer-specific formats (e.g., grouping `.ts`, `.py`, `.rs` into `Code`).

### **Transaction-Based Undo**
To handle the risk of data loss or "I didn't mean to do that," Flux implements a **Transaction Log**.
- Before any move, a JSON manifest of `{src, dest}` is recorded.
- `Undo` reads this log in reverse order to restore files to their exact original paths.
- Handles atomic moves to prevent partial states.

### **User Experience (UX)**
Command-line tools shouldn't be ugly. I used the `rich` library to provide semantic coloring and tables, making the "Before vs After" visualization clear before the user commits to changes.

## 5. Sample Output
![Sample Output](output_screenshot.png)

## 6. Video Demo
[Watch the Demo on YouTube](https://youtube.com/placeholder_demo_link)
*Note: This is a placeholder link for the assignment.*
