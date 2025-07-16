import gradio as gr
from ollama import Client
import requests

client = Client(host='http://localhost:11434')

def chat(message, history):
    try:
        # Try with different model name variations if needed
        response = client.generate(model='llama3', prompt=message)
        return response['response']
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Is 'ollama serve' running?"
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as app:
    gr.Markdown("## Local Llama 3 Chat")
    # Updated Chatbot with proper type specification
    chatbot = gr.Chatbot(type="messages")  # Fixes the deprecation warning
    msg = gr.Textbox(label="Type your message")
    clear = gr.Button("Clear Chat")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

app.launch()