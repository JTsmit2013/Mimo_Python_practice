# Mimo Python Practice

I have completed the Mimo Python Developer certification, and the projects from this certificate are included in this repository. Below is a brief explanation of each project and its topic:

---

### 1. **Intro to Python** | `using_input.py`

This beginner-friendly Python script practices user input by simulating a short conversation with a chatbot.

**Features:**
- Greets the user by name  
- Asks for their age and compares it to the bot's (age 3)  
- Asks for the user's favorite color and compliments it  

---

### 2. **Flow Control** | `rock_paper_scissors.py`

A simple command-line rock-paper-scissors game where a player competes against the computer.

**Features:**
- Best-of-three format (first to 2 wins)  
- User inputs move; computer selects randomly  
- Round-by-round results and score updates  
- Final message declares the overall winner  

---

### 2. **Lists** | `todo_list.py`

This Python script is a basic command-line To-Do list manager.

**Features:**
- View current tasks  
- Add new tasks  
- Remove the last task  
- Exit the program  
- Dynamic display of tasks and numbered menu interaction  

---

### 4. **Functions** | `food_ordering_func.py`

A basic food ordering system that lets users interactively place an order.

**Features:**
- Choose between Italian and Indian cuisine  
- View available meals by cuisine  
- Select a meal and quantity  
- Order validation and summary display  

---

### 5. **Tuples, Dictionaries, & Sets** | `digital_card_drawing.py`

This Python script simulates drawing cards from a standard 52-card deck.

**Features:**
- Creates and shuffles a digital deck (suits and ranks)  
- Prompts the user to draw a number of cards  
- Prevents overdrawing and handles invalid input  
- Continues until all cards are drawn  

---

### 6. **Modules & APIs** | `star_wars_api.py`

This Python script allows users to fetch and display information from a public Star Wars API (swapi.mimo.dev) by selecting one of several data categories.

**Features:**
- Prompts the user to choose a category: "people", "planets", "starships", "vehicles", "species", or "films".
- Sends a GET request to the Star Wars API using the requests library.
- Parses and prints the name of each entity returned by the API.
- Gracefully handles HTTP errors and invalid requests.

---

### 7. **Strings & List Operations** | `transaction_analyzer.py`

This Python program manages a list of financial transactions (deposits and withdrawals) and provides options to:

**Features:**
- Print a summary of total deposits, withdrawals, and current balance.
- Analyze transactions to find largest deposits/withdrawals and calculate average amounts.
- Stop the program gracefully.

---

### 8. **Object-Oriented Programming** | `library_system.py`

This Python script defines a basic object-oriented library system using two classes: `Book` and `Library`. It allows for managing a collection of books, checking books in and out, and displaying book information.

**Features:**
- Define individual books with title, author, and availability status
- Add books to a library collection
- Retrieve books by title (case-insensitive)
- Display all books in the collection with their current status
- Supports checking out and returning books

---

### 9. **Working With Private APIs** | `openai_chat_cli.py`

This Python script is a command-line interface for chatting with OpenAI's API via Mimo's endpoint. It supports threaded conversations, allowing users to continue or start new conversations easily.

**Features:**
- Start and continue threaded conversations
- Use exit to quit, and new to start a new thread
- Keeps track of unique thread IDs
- Uses environment variable MIMO_OPENAI_API_KEY for secure API access

---
