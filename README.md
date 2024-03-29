# Rukou: An AI Chatbot Assistant

Rukou is an AI chatbot designed to help users with various tasks and engage in meaningful conversations. Powered by OpenAI's GPT-4 language model, Rukou utilizes semantic search to dynamically insert relevant information from past conversations and knowledge bases, providing context-aware responses.

## Features

- Engages in interactive conversations to assist users with their queries and tasks
- Utilizes semantic search to retrieve relevant information from past conversations and knowledge bases
- Extracts keywords and generates summaries of conversations for improved context retention
- Stores conversation history and relevant knowledge for enhanced response generation
- Supports user commands for quitting, committing to memory, and seeking help

## Requirements

- Python 3.x
- OpenAI API key


## Usage

Run the script to start interacting with Rukou:

```
python main.py
```

Enter your name when prompted, and begin the conversation. Rukou will provide an initial greeting, and you can continue the conversation by entering your messages.

### Commands

- `/quit`: End the conversation, store the summary and keywords, and exit the program.
- `/quitns`: Quit the program without storing the summary and keywords.
- `/memory`: (TODO) Access stored memory.
- `/help`: (TODO) Display help information.
- `/commit`: Enter a mode to add information directly to Rukou's memory.

## How It Works

1. The script initializes the OpenAI API with the provided API key.

2. The `chat` function generates Rukou's responses based on the conversation history, user prompt, and relevant information retrieved through semantic search.

3. The `keywords` function extracts important keywords, repeated keywords, and synonyms from the conversation.

4. The `summary` function generates a concise summary of the conversation, including important details and context.

5. The `main` function handles the user interaction, manages the conversation flow, and processes user commands.

6. The conversation history, keywords, and summaries are stored in memory for future reference and context retention.

7. The script continues the conversation until the user enters the `/quit` command or Rukou decides to end the conversation.

## Rukou's Personality

Rukou is designed to have a Virtuoso (ISTP-A) personality type, characterized by the following traits:

- Introverted: Rukou is self-contained and enjoys working independently.
- Observant: Rukou is highly observant and focuses on the present moment.
- Thinking: Rukou approaches conversations logically and objectively.
- Prospecting: Rukou is adaptable and open to new possibilities.
- Assertive: Rukou is self-assured and confident in her abilities.

Rukou is also innovative and practical, able to experiment with different approaches and master various tools and skills to assist users effectively.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- OpenAI for providing the GPT-3 language model

If you have any questions or suggestions, please open an issue or submit a pull request.
