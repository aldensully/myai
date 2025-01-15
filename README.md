to run, just create a .env file and add:
ANTHROPIC_API_KEY=<YOUR_KEY>

To make the program runnable anywhere do the following:
1. Create a ~/bin folder to hold the script if it doesnt already exist
2. Create a blank file name called myai or whatever command you want to type to run it
3. add the following to the file:
#!/bin/bash
# Absolute path to your virtual environment
VENV_PATH="/home/user/local-ai/local-ai-venv"

# Absolute path to your Python script
SCRIPT_PATH="/home/user/local-ai/main.py"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Run the Python script
python "$SCRIPT_PATH"

4. Make executable: chmod +x ~/bin/myai
5. Make sure ~/bin is in PATH.
   If its not edit ~/.bashrc
   add: export PATH="$HOME/bin:$PATH"
6. Reload shell with: source ~/.bashrc  # Or source ~/.zshrc
7. Then you can just run myai and youre good to go
