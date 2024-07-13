import ollama



def summurize_the_text(full):

    text = f'summurize the text below\
            rules: do not use bad words, dont miss any thing important,\
            the text: {full}'
    
    response = ollama.generate(model='gemma:2b',
    prompt=text)

    return response['response']

