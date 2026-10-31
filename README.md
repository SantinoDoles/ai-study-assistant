# AI Study Assistant

A Python-powered AI Study Assistant that helps beginners learn programming through interactive explanations, multiple-choice quizzes, study tips, and score tracking.

This project uses the OpenAI API to generate educational content and demonstrate how artificial intelligence can be integrated into a Python application.

## Features

- **AI-Powered Explanations:** Enter a Python programming topic and receive a beginner-friendly explanation.
- **Interactive Quizzes:** Generate multiple-choice Python questions using AI.
- **Answer Validation:** Submit answers using A, B, C, or D and receive immediate feedback.
- **Quiz Explanations:** Review the correct answer and an explanation after submitting your response.
- **Score Tracking:** Track correct answers, total questions, and overall quiz percentage.
- **Score Reset:** Reset quiz statistics without restarting the application.
- **Study Tips:** Receive helpful study tips for supported Python topics.
- **Interactive Menu:** Navigate the application using simple text commands.

## Technologies Used

- Python 3
- OpenAI API
- OpenAI Python SDK
- python-dotenv
- Visual Studio Code
- Git and GitHub

## How It Works

The application runs in the terminal and allows users to interact with an AI-powered programming tutor.

Users can enter Python topics to receive explanations or use the following commands:

| Command | Description |
|---|---|
| `quiz` | Generate a multiple-choice Python quiz question |
| `score` | Display current quiz statistics |
| `reset` | Reset quiz scores |
| `quit` | Exit the application |

After answering a quiz question, the application checks the response, displays feedback, and updates the user's score.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SantinoDoles/ai-study-assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd ai-study-assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install openai python-dotenv
```

### 5. Configure Your OpenAI API Key

Create a `.env` file in the project's root directory.

Add the following line:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own OpenAI API key.

**Security Note:** The `.env` file is excluded from version control using `.gitignore` to prevent accidental exposure of API credentials.

### 6. Run the Application

```bash
python main.py
```

An internet connection and access to the OpenAI API are required. API usage may incur charges.

## Skills Demonstrated

This project demonstrates practical experience with:

- Python functions and dictionaries
- Conditional statements and loops
- User input and input validation
- Variables and score calculations
- API integration
- Working with AI-generated responses
- Environment variables and API key security
- Virtual environments and dependency management
- Git version control and GitHub repositories

## Future Improvements

Potential enhancements include:

- Saving quiz scores between sessions
- Adding difficulty levels for quiz questions
- Supporting additional programming languages
- Tracking learning progress over time
- Creating a graphical user interface
- Expanding the study tip library

## Project Purpose

I developed this project to strengthen my Python programming skills while exploring how artificial intelligence can be used to create interactive educational tools.

As an aspiring software developer, I wanted to build an application that combines traditional programming concepts with modern AI technology.

This project represents another step in my software development journey and will continue to evolve as I learn new skills.

## Author

**Santino Doles**

Aspiring Software Developer | Python | SQL | AI Development

GitHub: https://github.com/SantinoDoles