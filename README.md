# Broncohacks-openAI-Hackathon

# Chatbot with OpenAI Readme

## Overview

This Python script implements a simple chatbot using the OpenAI language model. The chatbot engages in conversation with the user, utilizing the OpenAI API to generate responses. The graphical user interface (GUI) is built using the Tkinter library.

## Prerequisites

Before running the script, ensure that you have the following:

- Python installed on your machine.
- An OpenAI API key. You can obtain one by signing up on the OpenAI platform.

## Getting Started

1. Clone the repository or download the script.
2. Set your OpenAI API key as an environment variable. You can do this by adding the following line to your environment variables or directly in the script:

   ```python
   os.environ["OPENAI_API_KEY"] = "your-api-key"
   ```

3. Run the script:

   ```bash
   python chatbot_with_openai.py
   ```

## Usage

- The GUI window will appear with a chat log, user input box, and a "Send" button.
- Enter your message in the user input box and click "Send" to interact with the chatbot.
- The chatbot response will be displayed in the chat log.

**Note:** You can exit the chatbot by typing "exit," "quit," or "bye" in the user input box.

## Dependencies

- Python 3.x
- Tkinter
- OpenAI Python library

## Acknowledgments

- This script was created by Kevin Wong.
- OpenAI for providing the language model and API.
