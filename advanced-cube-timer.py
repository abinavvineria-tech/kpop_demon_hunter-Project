#!/usr/bin/env python3
"""
Advanced Rubik's Cube Timer for Termux using termux-dialog.
Features: Inspection time, solve timing, session stats, best/average.
Requires: pkg install termux-api python [memory:2][web:27]
"""

import subprocess
import json
import time
import os
from datetime import datetime

TIMES_FILE = os.path.expanduser("~/.cube_times.json")
SESSION = []

def run_dialog(widget, **kwargs):
    """Run termux-dialog and parse JSON output."""
    cmd = ["termux-dialog", widget]
    for k, v in kwargs.items():
        cmd.extend([f"-{k}", str(v)])
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    return None

def load_times():
    """Load solve times from file."""
    if os.path.exists(TIMES_FILE):
        with open(TIMES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_times(times):
    """Save solve times to file."""
    with open(TIMES_FILE, 'w') as f:
        json.dump(times, f)

def format_time(seconds):
    """Format seconds to mm:ss.fff."""
    mins = int(seconds // 60)
    secs = seconds % 60
    return f"{mins:02d}:{secs:05.2f}" if mins else f"{secs:06.3f}"

def show_stats(times):
    """Show session stats via dialog."""
    if not times:
        run_dialog("alert", title="Stats", text="No solves yet!")
        return
    
    best = min(times)
    avg = sum(times[-12:]) / min(12, len(times))  # Ao12
    ao5 = sum(times[-5:]) / min(5, len(times))
    
    stats = f"Best: {format_time(best)}\nAo5: {format_time(ao5)}\nAo12: {format_time(avg)}\nTotal: {len(times)}"
    run_dialog("alert", title="Session Stats", text=stats)

def main_menu():
    """Main menu loop."""
    global SESSION
    all_times = load_times()
    
    while True:
        SESSION.append(None)  # Placeholder for new solve
        
        # Inspection timer (15s countdown)
        inspect_start = time.time()
        while time.time() - inspect_start < 15:
            remaining = 15 - (time.time() - inspect_start)
            if remaining <= 0:
                break
            print(f"\rInspection: {remaining:04.1f}s", end="", flush=True)
            time.sleep(0.1)
        print("\n" + " "*20)  # Clear line
        
        # Ready? confirmation
        ready = run_dialog("confirm", title="Ready?", text="Hold SPACE when ready!")
        if not ready or not ready.get("text") == "yes":
            continue
        
        # Start timer on space-like input (using text input as proxy)
        start_input = run_dialog("text", title="SPACE to START", text="Press enter to start", t="Timer Ready")
        start_time = time.time()
        
        # Solve input dialog blocks until done
        solve_input = run_dialog("text", title="SOLVING...", text="Enter when done!", t="Stop Timer")
        solve_time = time.time()
        
        solve_duration = solve_time - start_time
        SESSION[-1] = solve_duration
        all_times.extend([t for t in SESSION if t is not None])
        save_times(all_times)
        
        print(f"Solve: {format_time(solve_duration)}")
        
        # Quick stats menu
        choice = run_dialog("radio", title="Next?", 
                           items=["Solve Again", "Show Stats", "Quit"],
                           value="Solve Again")
        if choice and choice.get("index") == 2:
            break
        elif choice and choice.get("index") == 1:
            show_stats(all_times)

if __name__ == "__main__":
    print("Advanced Cube Timer v1.0 [memory:2]")
    print("Install: pkg install termux-api")
    main_menu()

