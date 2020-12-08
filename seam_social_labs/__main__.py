import sys
from .classmodule import chat_response
from .funcmodule import my_function

def main():
    arg = sys.argv[1]
    if (arg == "Love Miami"):
    	lang = "english"
    elif(arg == "Amor Miami"):
    	lang = "spanish"
    elif(arg == "Renmen Miami"):
    	lang = "creole"
    else:
        lang = "invalid"
    
    d = chat_response(lang)
    d.questions()

if __name__ == '__main__':
    main()

