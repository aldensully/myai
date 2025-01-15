import anthropic
from dotenv import load_dotenv
import os
import re

load_dotenv()  # Load .env file
api_key = os.getenv('ANTHROPIC_API_KEY')
client = anthropic.Anthropic()

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

def format_markdown(text):
    # Format inline code
    text = re.sub(r'`(.*?)`', f'{Colors.GREEN}\\1{Colors.RESET}', text)

    #bold
    text = re.sub(r'\*\*(.*?)\*\*', f'{Colors.BOLD}\\1{Colors.RESET}', text)
    text = re.sub(r'__(.*?)__', f'{Colors.BOLD}\\1{Colors.RESET}', text)

    # Format italic text
    text = re.sub(r'\*(.*?)\*', f'{Colors.ITALIC}\\1{Colors.RESET}', text)
    text = re.sub(r'_(.*?)_', f'{Colors.ITALIC}\\1{Colors.RESET}', text)

    # Format inline code
    text = re.sub(r'`(.*?)`', f'{Colors.GREEN}\\1{Colors.RESET}', text)

    # Format code blocks (for simplicity, we will just print them as is)
    text = re.sub(r'```(.*?)```', lambda m: f'{Colors.YELLOW}Code Block:\n{m.group(1)}{Colors.RESET}', text, flags=re.DOTALL)

    return text


def sendMessage(messages):
    response_content = ""

    with client.messages.stream(
        max_tokens=1024,
	    system="You are an AI programming assistant. You MUST answer concisely.",
        messages=messages,  # Use user input here
        model="claude-3-5-sonnet-20241022",
    ) as stream:
        for text in stream.text_stream:
            formatted_text = format_markdown(text)  # Format the streamed text
            print(formatted_text, end="", flush=True)
            response_content += text  # Capture the response content
    return response_content


def main():

    conversation_history = []

    while True:
        user_input = input(f"\n{Colors.BLUE}Ask: {Colors.RESET}")

        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break

        conversation_history.append({"role": "user", "content": user_input})

        print(f"{Colors.CYAN}Myai: {Colors.RESET}", end="")
        # sendMessage(user_input)
        assistant_response = sendMessage(conversation_history)
        conversation_history.append({"role": "assistant", "content": assistant_response})


if __name__ == "__main__":
    main()
