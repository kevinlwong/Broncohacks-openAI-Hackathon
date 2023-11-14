# Broncohacks-openAI-Hackathon

# Chatbot with OpenAI chatbot_gui.py

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
____________________________________________________________________________________________________________________________________________________________________________________________


# Chatbot openai-test.py

## Overview

This Python script utilizes the OpenAI GPT-3.5-turbo model to create a conversational chatbot. The chatbot engages in a dynamic conversation with the user, responding to questions and prompts. The script is designed to run in a loop, allowing users to interact with the chatbot until they choose to exit.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your machine (recommended version 3.6 or higher).
- OpenAI Python library (`openai`) installed. You can install it using the following command:
  ```
  pip install openai
  ```

## Usage

1. Open the script in a text editor or an integrated development environment (IDE) of your choice.

2. Replace the placeholder API key in the `openai.api_key` variable with your actual OpenAI API key.

3. Run the script in your terminal or command prompt:
   ```
   python chatbot_script.py
   ```

4. The chatbot will prompt you to enter a question. Type your question and press Enter.

5. The chatbot will respond with an AI-generated answer.

6. Continue the conversation by responding to the prompt: "Would you like to continue? y|n."

7. To end the conversation and exit the script, type "quit" when prompted for a question.

## Important Note

- Ensure that you use the OpenAI API key responsibly and in compliance with OpenAI's use case policies.

## Customization

Feel free to customize the script to better suit your needs. You can modify the conversation initialization, change the system message, or add additional functionality based on the requirements of your project.

## Disclaimer

This script is a basic implementation and may require further refinement based on your specific use case and requirements. OpenAI's use case policies should be adhered to when using the GPT-3.5-turbo model. Refer to OpenAI's documentation for more details: [OpenAI API Documentation](https://beta.openai.com/docs/).
