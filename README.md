#  Local Command-Line Chatbot using Hugging Face

### Overview
This project is a simple CLI chatbot built using a Hugging Face text generation model. It runs locally and maintains a short conversation memory to respond coherently.

---

###  Features
- Built using Hugging Face `transformers`
- Maintains short-term memory of previous turns
- Modular design (`model_loader.py`, `chat_memory.py`, `interface.py`)
- Simple command-line interface

---

###  Setup
### 1. Extract or clone the project
```bash
cd ATG_Chatbot_Assignment
```

### 2. Create a virtual environment 
```bash
python -m venv venv
venv\Scripts\activate  
```

### 3. Install dependencies
```bash
pip install transformers torch
```

### 4. Run the chatbot
```bash
python interface.py
```

---

###  Example
```
User: What is the capital of France?
Bot: The capital of France is Paris.

User: And what about Italy?
Bot: The capital of Italy is Rome.

User: /exit
Exiting chatbot. Goodbye!
```

---

###  Folder Structure
```
ATG_Chatbot_Assignment/
│
├── model_loader.py | Loads the Hugging Face model |
├── chat_memory.py | Stores last country for follow-up questions |
├── interface.py | Main chatbot loop |
└── README.md | Setup and demo guide |
```

---

### Demo video link
https://drive.google.com/file/d/1Ndma_0SDAeYPeNZXKoA7Y7RNUo_nFPL8/view?usp=drivesdk

###  Credits
Assignment for ATG Machine Learning Intern role.
