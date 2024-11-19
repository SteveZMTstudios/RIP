# This script reads input from the user, splits it by newlines,
# and formats each line into a div with class "keybox".

def format_input_to_divs(input_text):
    lines = input_text.strip().split('\n')
    formatted_lines = [f'<div class="keybox">{line}</div>' for line in lines]
    return '\n'.join(formatted_lines)

if __name__ == "__main__":
    import sys
    input_text = sys.stdin.read()
    result = format_input_to_divs(input_text)
    print(result)