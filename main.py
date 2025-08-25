import ollama
import sys

def main():
    # Set UTF-8 encoding for output
    sys.stdout.reconfigure(encoding='utf-8')
    
    client = ollama.Client(host='192.168.1.23:11434')
    
    # Get user input
    user_input = input("Enter your message: ")
    
    response = client.chat(model='gpt-oss:20b', messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    print(response['message']['content'])


if __name__ == "__main__":
    main()
