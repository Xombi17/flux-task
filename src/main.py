import argparse
import sys
from pathlib import Path
from .organizer import Organizer
from .ui import UI

def main():
    ui = UI()
    
    parser = argparse.ArgumentParser(
        description="Flux: Intelligent Directory Organizer",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Organize Command
    org_parser = subparsers.add_parser("organize", help="Organize a directory")
    org_parser.add_argument("path", help="Path to the directory to organize")
    org_parser.add_argument("--dry-run", action="store_true", help="Simulate without moving files")

    # Undo Command
    undo_parser = subparsers.add_parser("undo", help="Undo the last operation")
    undo_parser.add_argument("path", help="Path to the directory to undo organization for")

    args = parser.parse_args()

    if not args.command:
        ui.print_banner()
        parser.print_help()
        sys.exit(0)

    target_path = Path(args.path).resolve()

    if not target_path.exists():
        ui.print_error(f"Directory '{target_path}' does not exist.")
        sys.exit(1)

    if args.command == "organize":
        ui.print_banner()
        ui.print_info(f"Scanning: {target_path}")

        organizer = Organizer(target_path)
        moves = organizer.scan()

        if not moves:
            ui.print_warning("No files to organize.")
            sys.exit(0)

        # Prepare table data
        rows = []
        for move in moves:
            rows.append([
                Path(move.src).name,
                move.category,
                str(Path(move.dest).relative_to(target_path))
            ])

        ui.print_table(f"Proposed Moves ({len(moves)} files)", ["File", "Category", "Destination"], rows)

        if args.dry_run:
            ui.print_warning("DRY RUN ACTIVE: No files were moved.")
            return

        print(f"{ui.BOLD}Do you want to proceed? [y/N] {ui.RESET}", end="")
        if input().lower() == 'y':
            organizer.execute(moves)
            ui.print_success(f"Organized {len(moves)} files.")
        else:
            ui.print_error("Aborted.")

    elif args.command == "undo":
        ui.print_banner()
        ui.print_info(f"Attempting undo for: {target_path}")
        
        organizer = Organizer(target_path)
        messages = organizer.undo()

        for msg in messages:
            if "Restored" in msg or "Removed" in msg:
                ui.print_success(msg)
            elif "Failed" in msg or "not find" in msg:
                ui.print_error(msg)
            else:
                ui.print_info(msg)

if __name__ == "__main__":
    main()
