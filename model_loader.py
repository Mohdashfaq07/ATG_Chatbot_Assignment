# model_loader.py
# Load a Hugging Face model for question answering

from transformers import pipeline

def load_model():
    # Use a pre-trained Q&A model
    qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")
    return qa_model

if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully!")
