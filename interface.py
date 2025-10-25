from model_loader import load_model

def main():
    print(" Q&A Chatbot (type /exit to quit)")
    model = load_model()

    context = """
    France is a country located in Western Europe.
    The capital of France is Paris.

    Italy is a country located in Southern Europe.
    The capital of Italy is Rome.

    Germany is a country located in Central Europe.
    The capital of Germany is Berlin.

    Spain is a country located in Southwestern Europe.
    The capital of Spain is Madrid.

    The United Kingdom is made up of England, Scotland, Wales, and Northern Ireland.
    The capital of the United Kingdom (and England) is London.
    """

    previous_country = None  # store last country asked

    while True:
        question = input("User: ")
        if question.strip().lower() == "/exit":
            print("Exiting Chatbot. Goodbye!")
            break

        q_lower = question.lower().strip(" ?.")

        # Detect follow-up question
        if q_lower.startswith("and what about") or q_lower.startswith("what about"):
            country = q_lower.split("about")[-1].strip().capitalize()
        elif "capital of" in q_lower:
            country = question.split("of")[-1].strip(" ?.")
        else:
            country = previous_country

        result = model(question=f"What is the capital of {country}?", context=context)
        answer = result["answer"]

        if country and "capital" in question.lower():
            print(f"Bot: The capital of {country} is {answer}.")
        elif country:
            print(f"Bot: The capital of {country} is {answer}.")
        else:
            print(f"Bot: {answer}")

        previous_country = country

if __name__ == "__main__":
    main()

