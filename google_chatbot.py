import pickle
import os
import google.generativeai as genai
import tkinter as tk
from tkinter import messagebox

# Function to get API key, store it in a binary file, and set it up for Google Generative AI usage
def get_api_key():
    # Check if key.dat exists
    if os.path.exists("key.dat"):
        # Load the key from the file
        with open("key.dat", "rb") as f:
            api_key = pickle.load(f)
    else:
        # Show instructions and prompt for API key if key.dat does not exist
        def prompt_for_api_key():
            api_key = api_key_entry.get()
            if api_key:
                # Save the key in a binary file using pickle
                with open("key.dat", "wb") as f:
                    pickle.dump(api_key, f)
                messagebox.showinfo("Success", "API key saved successfully!")
                root.destroy()
            else:
                messagebox.showerror("Error", "API key cannot be empty.")

        # Instructions for generating an API key
        def show_instructions():
            instruction_text = (
                "To use this chatbot, you'll need a Google Generative AI API key. Please visit:\n\n"
                "https://console.cloud.google.com/apis\n\n"
                "Enable the PaLM API and create a new API key."
            )
            messagebox.showinfo("Generate API Key", instruction_text)

        # Set up the Tkinter window for user input
        root = tk.Tk()
        root.title("API Key Setup")

        instruction_label = tk.Label(root, text="Enter your Google API Key:", font=("Arial", 12))
        instruction_label.pack(pady=10)

        api_key_entry = tk.Entry(root, show="*", width=40)
        api_key_entry.pack(pady=5)

        submit_button = tk.Button(root, text="Save Key", command=prompt_for_api_key)
        submit_button.pack(pady=5)

        instruction_button = tk.Button(root, text="How to Generate an API Key", command=show_instructions)
        instruction_button.pack(pady=5)

        root.mainloop()

        # Reopen and load the saved key
        with open("key.dat", "rb") as f:
            api_key = pickle.load(f)

    # Configure the API key
    genai.configure(api_key=api_key)
    return api_key

# Function to initialize the generative model and generate a response
def chat_with_google(prompt, model_name="gemini-1.5-flash"):
    try:
        # Initialize the generative model
        model = genai.GenerativeModel(model_name)
        # Generate content with the user's prompt
        response = model.generate_content(prompt)
        return response.text  # Returns the generated text response
    except Exception as e:
        return f"An error occurred: {e}"

# Main loop to interact with the chatbot
def main():
    api_key = get_api_key()
    print("Google Chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        reply = chat_with_google(user_input)
        print(f"Chatbot: {reply}")

# Run the main function
if __name__ == "__main__":
    main()
