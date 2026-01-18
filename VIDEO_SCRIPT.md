# Flux CLI - Demo Script
**Approximate Duration: 3-5 Minutes**

## 0:00 - 0:45: The Problem
*Show the "Downloads" folder on your desktop. It is messy, filled with random images, executables, and PDFs.*
**Narration**: "Hi, I'm [Your Name]. We all face the same problem: digital clutter. My 'Downloads' folder is a graveyard of files that I'm too lazy to sort manually. Today I want to show you 'Flux', a tool I built to solve this exact problem."

## 0:45 - 2:00: Organization & Features
*Switch to the Terminal.*
**Narration**: "Flux is a Python-based CLI utility. Let's see it in action."
*Type command:* `python -m src.main organize /path/to/downloads --dry-run`
**Narration**: "First, I run it with the dry-run flag. Safety is key. I don't want to move files without knowing where they go. Flux scans the directory and presents a beautiful table using the 'Rich' library, showing me exactly what will happen."

*Type command:* `python -m src.main organize /path/to/downloads`
*Accept the prompt (y).*
*Switch back to File Explorer.*
**Narration**: "Now I execute it. Instantly, all my files are sorted into 'Images', 'Documents', and 'Code'. It handles naming collisions automatically."

## 2:00 - 3:00: The Undo Feature
**Narration**: "But what if I made a mistake? Flux has a built-in transaction system."
*Switch to Terminal.*
*Type command:* `python -m src.main undo /path/to/downloads`
**Narration**: "I simply run the undo command. It reads the transaction log and restores every file to its original location. It even cleans up the empty directories it created."
*Show File Explorer again (files are back).*

## 3:00 - 4:00: Code Walkthrough & Design
*Open VS Code showing `src/organizer.py`.*
**Narration**: "I designed Flux with modularity in mind. The `Organizer` class separates the scanning logic from execution. I used a Strategy-like pattern for the `Classifier` to easily extend file types. And crucially, every 'execute' action writes a JSON log, which allows the reliable undo functionality you just saw."

## 4:00 - End: Conclusion
**Narration**: "Flux transforms a tedious chore into a one-second command. It's safe, reliable, and aesthetically pleasing. Thank you for watching."
