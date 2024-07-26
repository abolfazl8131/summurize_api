import ollama



def summurize_the_text(full, paragraphs):

    text = f'summurize the text below in the {paragraphs} paragraphs\
            rules: do not use bad words, dont miss any important data,\
            the text: {full}'
    
    response = ollama.generate(model='gemma:2b',
    prompt=text)

    return response['response']

