#!/bin/zsh

# Deactivate any active virtual environment
if [[ -n "$VIRTUAL_ENV" ]]; then
    deactivate
fi


# Get script directory (works in zsh)
SCRIPT_DIR="${0:A:h}"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PREV_PWD="$PWD"

echo "Script dir: $SCRIPT_DIR"
echo "Project root: $PROJECT_ROOT"


# Change to project root
cd "$SCRIPT_DIR" || { echo "Error: Cannot change to project root directory"; exit 1; }

# Create virtual environment (in /src/ directory)
python3 -m venv venv_sitegen || { echo "Error: Failed to create virtual environment"; exit 1; }

# Activate virtual environment
source ./venv_sitegen/bin/activate || { echo "Error: Failed to activate virtual environment"; exit 1; }

# Install required packages
pip3 install pyyaml jinja2 markdown python-dotenv openai gradio || { echo "Error: Failed to install required packages"; exit 1; }

# Run sitegen
if [[ "$1" == "-w" ]]; then
    python3 sitegen.py -w || { echo "Error: Failed to run sitegen with web server"; exit 1; }
    echo "Success: Site generated and web server started"
else
    python3 sitegen.py || { echo "Error: Failed to run sitegen"; exit 1; }
    echo "Success: Site generated"
fi

# Change back to original directory
cd "$PREV_PWD" || { echo "Error: Cannot change to starting directory"; exit 1; }
