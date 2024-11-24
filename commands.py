import os
import webbrowser
import pywhatkit
from datetime import datetime

def execute_command(query):
    """Process and execute commands based on user input."""
    if "open notepad" in query:
        open_notepad()
    elif "open youtube" in query:
        open_youtube()
    elif "play" in query:
        play_on_youtube(query)
    elif "search" in query:
        search_google(query)
    elif "shutdown" in query or "restart" in query or "log off" in query:
        politely_decline_system_commands()
    elif "open vscode" in query or "open visual studio code" in query:
        open_vscode()
    elif "run server" in query:
        run_server()
    elif "check time" in query or "what time" in query:
        check_time()
    elif "open github" in query:
        open_github()
    elif "pull from git" in query:
        git_pull()
    elif "push to git" in query:
        git_push()
    elif "create branch" in query:
        git_create_branch(query)
    elif "open stack overflow" in query:
        open_stackoverflow()
    elif "open documentation" in query:
        open_documentation(query)
    elif "run script" in query:
        run_script(query)
    elif "list files" in query:
        list_files()
    elif "open browser" in query:
        open_browser()
    if "open jupyter" in query:
        open_jupyter_notebook()
    elif "load dataset" in query:
        load_dataset()
    elif "perform eda" in query:
        perform_eda()
    elif "generate plot" in query:
        generate_plot()
    elif "check time" in query or "what time" in query:
        check_time()
    elif "open kaggle" in query:
        open_kaggle()
    elif "run python script" in query:
        run_python_script(query)    
    else:
        speak("Sorry, I didn't understand the command.")

def open_notepad():
    """Open Notepad application."""
    speak("Opening Notepad.")
    os.system("notepad")

def open_youtube():
    """Open YouTube in a browser."""
    speak("Opening YouTube.")
    webbrowser.open("https://www.youtube.com")

def play_on_youtube(query):
    """Play a video on YouTube."""
    song = query.replace("play", "").strip()
    speak(f"Playing {song} on YouTube.")
    pywhatkit.playonyt(song)

def search_google(query):
    """Search Google for a query."""
    search_query = query.replace("search", "").strip()
    speak(f"Searching Google for {search_query}.")
    webbrowser.open(f"https://www.google.com/search?q={search_query}")

def politely_decline_system_commands():
    """Politely inform the user that system commands must be done manually."""
    speak("Sorry, I cannot help with that. Please perform this action manually.")

def open_vscode():
    """Open Visual Studio Code."""
    speak("Opening Visual Studio Code.")
    os.system("code")

def run_server():
    """Run a local development server."""
    speak("Starting the development server.")
    os.system("python -m http.server")

def check_time():
    """Check the current time."""
    current_time = datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}.")
    print(f"Current Time: {current_time}")

def open_github():
    """Open GitHub in a browser."""
    speak("Opening GitHub.")
    webbrowser.open("https://github.com")

def git_pull():
    """Perform a Git pull operation."""
    speak("Pulling latest changes from the repository.")
    os.system("git pull")

def git_push():
    """Perform a Git push operation."""
    speak("Pushing local changes to the repository.")
    os.system("git push")

def git_create_branch(query):
    """Create a new Git branch."""
    branch_name = query.replace("create branch", "").strip()
    if branch_name:
        speak(f"Creating a new branch named {branch_name}.")
        os.system(f"git checkout -b {branch_name}")
    else:
        speak("Please provide a branch name.")

def open_stackoverflow():
    """Open Stack Overflow in a browser."""
    speak("Opening Stack Overflow.")
    webbrowser.open("https://stackoverflow.com")

def open_documentation(query):
    """Open documentation for a programming language or framework."""
    framework = query.replace("open documentation", "").strip()
    speak(f"Searching for documentation on {framework}.")
    webbrowser.open(f"https://www.google.com/search?q={framework}+documentation")

def run_script(query):
    """Run a Python or other script."""
    script_name = query.replace("run script", "").strip()
    if script_name:
        speak(f"Running the script {script_name}.")
        os.system(f"python {script_name}")
    else:
        speak("Please specify the script name.")

def list_files():
    """List files in the current directory."""
    speak("Listing all files in the current directory.")
    files = os.listdir()
    for file in files:
        print(file)

def open_browser():
    """Open the default web browser."""
    speak("Opening the default web browser.")
    os.system("start chrome")

def open_jupyter_notebook():
    """Open Jupyter Notebook."""
    speak("Opening Jupyter Notebook.")
    os.system("jupyter notebook")

def load_dataset():
    """Load a dataset and display basic information."""
    file_path = input("Enter the full file path of the dataset: ")
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            speak("Dataset loaded successfully.")
            print(df.head())
            print("\nColumns:")
            print(df.columns)
            print("\nSummary:")
            print(df.describe())
        except Exception as e:
            speak("There was an error loading the dataset.")
            print(f"Error: {e}")
    else:
        speak("File not found. Please check the path and try again.")

def perform_eda():
    """Perform basic exploratory data analysis."""
    file_path = input("Enter the full file path of the dataset: ")
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            speak("Performing exploratory data analysis.")
            print("Dataset Information:")
            print(df.info())
            print("\nMissing Values:")
            print(df.isnull().sum())
            print("\nBasic Statistics:")
            print(df.describe())
        except Exception as e:
            speak("There was an error performing EDA.")
            print(f"Error: {e}")
    else:
        speak("File not found. Please check the path and try again.")

def generate_plot():
    """Generate a simple plot for data visualization."""
    file_path = input("Enter the full file path of the dataset: ")
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            speak("Generating a plot. Please wait.")
            sns.pairplot(df.select_dtypes(include=['float', 'int']).dropna())
            plt.show()
        except Exception as e:
            speak("There was an error generating the plot.")
            print(f"Error: {e}")
    else:
        speak("File not found. Please check the path and try again.")



def check_time():
    """Check the current time."""
    current_time = datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}.")
    print(f"Current Time: {current_time}")

def open_kaggle():
    """Open Kaggle in a browser."""
    speak("Opening Kaggle.")
    webbrowser.open("https://www.kaggle.com")

def run_python_script(query):
    """Run a Python script."""
    script_name = query.replace("run python script", "").strip()
    if script_name:
        speak(f"Running the script {script_name}.")
        try:
            os.system(f"python {script_name}")
        except Exception as e:
            speak("There was an error running the script.")
            print(f"Error: {e}")
    else:
        speak("Please specify the script name.")



def speak(text):
    """Convert text to speech for feedback."""
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)
    engine.say(text)
    engine.runAndWait()
