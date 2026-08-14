# Day 77: argparse (Command Line Tools)

## Concept
The `argparse` module allows you to create **command-line interfaces (CLI)** for your Python programs.  
It helps your program accept arguments and options from the terminal.

## Why argparse?
- Make Python scripts configurable from terminal  
- Automate tasks with different input options  
- Avoid hardcoding values inside scripts  

## Basic Steps
1. Import `argparse`  
2. Create `ArgumentParser` object  
3. Add arguments (`add_argument`)  
4. Parse arguments (`parse_args`)  
5. Use arguments in your program  

## Example Arguments
- Positional arguments → required  
- Optional arguments → start with `-` or `--`  

## Use Cases
- File management tools  
- Automation scripts  
- Data processing pipelines  
- Task runners  

## Why Learn argparse?
- CLI tools are widely used by developers  
- Makes scripts reusable and flexible  
- Essential for **real-world Python projects**