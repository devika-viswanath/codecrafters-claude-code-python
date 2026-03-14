[![progress-banner](https://backend.codecrafters.io/progress/claude-code/3329b764-816c-4adb-95f1-8f2e7355ac76)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

# Build Your Own Claude Code (Python)

This repository contains my implementation of the **"Build Your Own Claude Code" challenge** from CodeCrafters.

Claude Code is an AI coding assistant that uses **Large Language Models (LLMs)** to understand code, reason about problems, and perform actions through tool calls. In this challenge, the goal is to build a simplified version of a coding assistant by implementing an **LLM-powered agent** from scratch.

This project demonstrates how modern AI coding assistants work internally by combining **LLM reasoning, tool calling, and an agent loop**.

---

## Project Overview

The agent built in this project can:

- Communicate with an LLM using an OpenAI-compatible API
- Detect tool calls requested by the LLM
- Execute tools such as reading files, writing files, and running shell commands
- Return tool results back to the LLM
- Continue reasoning until a final response is generated

This architecture is similar to modern AI developer tools like **Claude Code, Cursor, GitHub Copilot Workspace, and Devin AI**.

---

## Tools Implemented

### Read Tool

The **Read tool** allows the AI agent to read files from the filesystem.

Example:

```
Read("README.md")
```

This helps the LLM inspect project files and understand code.

---

### Write Tool

The **Write tool** allows the agent to create or modify files.

Example:

```
Write("config.py", "API_KEY=123")
```

This allows the LLM to generate or edit code automatically.

---

### Bash Tool

The **Bash tool** allows the agent to execute shell commands.

Example:

```
Bash("ls")
Bash("rm README_old.md")
```

This allows the AI to interact with the operating system.

---

## Agent Loop Architecture

The core concept implemented in this project is an **agent loop**.

The workflow looks like this:

```
User Prompt
      ↓
Python Agent Controller
      ↓
LLM (Claude via OpenRouter API)
      ↓
LLM decides whether to answer or call a tool
      ↓
Tool execution
 ├ Read
 ├ Write
 └ Bash
      ↓
Tool result returned to the LLM
      ↓
LLM continues reasoning
      ↓
Final answer returned to the user
```

This loop continues until the LLM produces a final response.

---

## Technologies Used

- Python
- OpenRouter API
- OpenAI-compatible tool calling
- subprocess module (for bash execution)
- agent loop architecture
- file system operations

---

## Project Structure

```
codecrafters-claude-code-python
│
├── app
│   └── main.py
│
├── your_program.sh
│
└── README.md
```

The main implementation of the Claude Code agent is located in:

```
app/main.py
```

---

## Running the Program

To run the program locally:

```
./your_program.sh
```

Or run directly using Python:

```
python app/main.py -p "your prompt"
```

Example:

```
python app/main.py -p "List files and delete README_old.md"
```

The agent will communicate with the LLM, detect tool calls, execute the tools, and return the final response.

---

## Passing the First Stage

The entry point for the Claude Code implementation is in `app/main.py`.

To submit your solution for the first stage run:

```
codecrafters submit
```

---

## Stage 2 & Beyond

For stages beyond the first:

1. Ensure you have `uv` installed locally.
2. Run the program locally:

```
./your_program.sh
```

3. Submit your solution:

```
codecrafters submit
```

Test output will be streamed to your terminal.

---

## What I Learned

Through this project I learned:

- How LLM APIs work
- How tool calling works in AI systems
- How to implement an agent loop
- File system operations using Python
- Running shell commands using subprocess
- The internal architecture of AI coding assistants

---

## Challenge Reference

This project is based on the CodeCrafters challenge:

https://codecrafters.io/challenges/claude-code

---

## Author

Devika Viswanath  
MCA Student | AI & Software Development
