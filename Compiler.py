import re
import sys

TOKEN_SPECIFICATION = [
    ("PREPROCESSOR", r"#\s*\b(include|define|if|ifdef|ifndef|endif|else|elif)\b\s*(<[^>]+>|\"[^\"]+\")?"),  
    #("MULTI_LINE_COMMENT", r"/\*[\s\S]*?\*/"),      
    ("COMMENT", r"//[^\n]*"),                       
    ("KEYWORD", r"\b(int|float|double|char|if|else|for|while|do|switch|case|default|return|void|break|continue|static|const|sizeof|struct|union|typedef|enum|namespace|class|public|private|protected|virtual|override|new|delete|try|catch|throw|using|nullptr)\b"), # C++ keywords
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),  
    ("STRING_LITERAL", r'"([^"\\]|\\.)*"'),         
    ("CHAR_LITERAL", r"'([^'\\]|\\.)'"),            
    ("CONSTANT_FLOAT", r"\b\d+\.\d+([eE][+-]?\d+)?\b"),  
    ("CONSTANT_INTEGER", r"\b\d+\b"),               
    ("LOGICAL", r"&&|\|\||!"),                      
    ("COMPARISON", r"==|!="),                       
    ("RELATIONAL", r"[<>]=?"),                      
    ("OPERATOR", r"[+\-*/%]=?|[~^&|]"),             
    ("ASSIGNMENT", r"="),                           
    ("PUNCTUATOR", r"[;{}()[\],.:]"),               
    ("WHITESPACE", r"\s+"),                         
]

token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPECIFICATION)
token_re = re.compile(token_regex, re.MULTILINE)  

def tokenize(code):
    tokens = []
    for match in token_re.finditer(code):
        type = match.lastgroup
        value = match.group(type)
        if type != "WHITESPACE":  
            tokens.append((type, value))
    return tokens

def display_tokens(tokens):
    for token_type, token_value in tokens:
        print(f"Token Type: {token_type}, Token Value: {token_value}")


cpp_code = """
// This is a comment
int main() {
    float a = 3.14; // Declare a float variable
    /* Multi-line
       comment */
    int b = 10;     // Declare another integer
    if (a < b) {
        return 1;   // Return 1 if a is less than b
    } else {
        return 0;   // Return 0 otherwise
    }
}
"""
print("Enter text for analysis (type 'perform' to analyze the input):")
input_data = ""
while True:
    line = input()
    if line.strip().lower() == 'perform':
        break
    input_data += line + "\n"

tokens = tokenize(input_data)
display_tokens(tokens)
