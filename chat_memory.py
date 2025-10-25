# chat_memory.py
# Manage short-term chat history using a sliding window mechanism.

class ChatMemory:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.history = []

    def add(self, user_input, bot_response):
        self.history.append((user_input, bot_response))
        if len(self.history) > self.window_size:
            self.history.pop(0)

    def get_context(self):
        return '\n'.join([f'User: {u}\nBot: {b}' for u, b in self.history])
