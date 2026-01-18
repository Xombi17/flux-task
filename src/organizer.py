import json
import shutil
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional
from datetime import datetime

from .classifier import classify_file

@dataclass
class MoveOperation:
    src: str
    dest: str
    category: str

class Organizer:
    def __init__(self, target_dir: Path):
        self.target_dir = target_dir
        self.flux_dir = self.target_dir / ".flux"
        self.flux_dir.mkdir(exist_ok=True, parents=True)
        self.transactions_dir = self.flux_dir / "transactions"
        self.transactions_dir.mkdir(exist_ok=True)

    def scan(self) -> List[MoveOperation]:
        """
        Scans the directory and proposes moves.
        Ignores .flux directory and already categorized folders if possible (basic implementation: ignores hidden files).
        """
        moves = []
        for file_path in self.target_dir.iterdir():
            if file_path.is_file() and not file_path.name.startswith('.'):
                if file_path.name == 'main.py' or file_path.name == 'flux': 
                    # Use a simple heuristic to skip the script itself if running from same dir, though irrelevant if installed
                    continue
                
                category = classify_file(file_path)
                if category:
                    dest_folder = self.target_dir / category
                    dest_path = dest_folder / file_path.name
                    
                    # Avoid moving if already in place (not applicable for flat scan, but good for safety)
                    if file_path != dest_path:
                        moves.append(MoveOperation(
                            src=str(file_path),
                            dest=str(dest_path),
                            category=category
                        ))
        return moves

    def execute(self, moves: List[MoveOperation], dry_run: bool = False) -> bool:
        """
        Executes moves. Returns True if successful (or dry run finished).
        """
        if not moves:
            return False

        if dry_run:
            return True

        transaction_record = {
            "timestamp": datetime.now().isoformat(),
            "moves": []
        }

        for move in moves:
            src = Path(move.src)
            dest = Path(move.dest)
            
            # Ensure dest dir exists
            dest.parent.mkdir(exist_ok=True)

            # Handle collision: rename if exists
            if dest.exists():
                stem = dest.stem
                suffix = dest.suffix
                counter = 1
                while dest.exists():
                    dest = dest.with_name(f"{stem}_{counter}{suffix}")
                    counter += 1
            
            try:
                shutil.move(src, dest)
                transaction_record["moves"].append({
                    "src": str(src),
                    "dest": str(dest)
                })
            except Exception as e:
                print(f"Error moving {src} to {dest}: {e}")

        # Save transaction
        log_file = self.transactions_dir / f"trans_{int(time.time())}.json"
        with open(log_file, "w") as f:
            json.dump(transaction_record, f, indent=4)
            
        return True

    def undo(self) -> List[str]:
        """
        Undoes the last transaction. Returns list of messages describing actions.
        """
        logs = sorted(self.transactions_dir.glob("trans_*.json"), reverse=True)
        if not logs:
            return ["No history found to undo."]

        latest_log = logs[0]
        with open(latest_log, "r") as f:
            data = json.load(f)

        messages = []
        moves = data.get("moves", [])
        # Undo in reverse order
        for move in reversed(moves):
            src_orig = Path(move["src"]) # Where it was
            current_loc = Path(move["dest"]) # Where it is now

            if current_loc.exists():
                try:
                    shutil.move(current_loc, src_orig)
                    messages.append(f"Restored {src_orig.name}")
                    
                    # Clean up empty category dir
                    if current_loc.parent != self.target_dir and not any(current_loc.parent.iterdir()):
                        current_loc.parent.rmdir()
                        messages.append(f"Removed empty directory {current_loc.parent.name}")
                        
                except Exception as e:
                    messages.append(f"Failed to restore {current_loc.name}: {e}")
            else:
                messages.append(f"Could not find {current_loc.name} to restore.")

        # Remove log file
        latest_log.unlink()
        return messages
