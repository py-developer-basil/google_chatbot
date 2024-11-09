# Google Generative AI Chatbot

This project is a simple chatbot interface using Google Generative AI. It includes a `Tkinter` interface to help the user set up and save their API key for use with the Google Generative AI API.

## Features
- **API Key Setup**: A Tkinter-based GUI to help users securely save their Google Generative AI API key.
- **Chatbot Interaction**: Interact with Google’s Generative AI models using simple prompts.
- **Error Handling**: Basic error handling to guide the user in case of any issues.

## Prerequisites
1. Python 3.6 or higher.
2. Google Generative AI API key.
3. Required libraries: `pickle`, `google-generativeai`, `tkinter`.

## Installation
1. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
   
2. **Run the chatbot**:
    ```bash
    python google_chatbot.py
    ```

## Usage

### Setting up the API Key
The first time you run the chatbot, a Tkinter window will prompt you to enter your API key. If you don’t have an API key, follow the instructions in the application to obtain one from Google.

### Starting a Chat
Once the API key is set, you can interact with the chatbot directly from the command line. Type in your prompt, and the chatbot will respond.

Type `exit` to end the chat.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Feel free to submit pull requests or open issues if you encounter bugs or have suggestions for improvement.

## Repository
- GitHub: [https://github.com/py-developer-basil/google_chatbot.git](https://github.com/py-developer-basil/google_chatbot.git)
