# LLAMA3 Chatbot

## Overview
This project is a chatbot powered by the LLAMA3 language model using Streamlit and LangChain. The chatbot can provide responses to user queries based on predefined prompts and conversation history.

## Features
- Utilizes **LLAMA3** for natural language processing.
- Interactive **chat interface** using **Streamlit**.
- Maintains **conversation history** within a session.
- Supports **prompt templates** for structured responses.
- Provides **real-time streaming responses**.

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed along with `pip`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/llama3-chatbot.git
   cd llama3-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the chatbot application:
   ```bash
   streamlit run app.py
   ```

## Usage
- Open the **Streamlit web interface** in your browser.
- Start typing in the chat input box to interact with the chatbot.
- The chatbot will generate responses in real-time.

## File Structure
```
llama3-chatbot/
│── app.py       # Main chatbot interface
│── new.py       # Chat prompt and response processing
│── requirements.txt  # Required dependencies
│── README.md    # Project documentation
```

## Dependencies
- **Streamlit**: For web-based chatbot UI.
- **LangChain**: Framework for prompt chaining and response parsing.
- **Ollama**: Integration with LLAMA3 model.

## Customization
- Modify `new.py` to **update the prompt template** and system instructions.
- Edit `app.py` to **customize the UI** and response handling.

## License
This project is licensed under the MIT License.

## Contributors
- **Swathiga S** (swathiga22@gmail.com)

## Acknowledgments
Special thanks to the developers of **LangChain**, **Streamlit**, and **Ollama** for making this project possible.

