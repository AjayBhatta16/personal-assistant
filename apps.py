import wikipedia

apps = {
    "tell me about": "wikipedia",
    "teach me something new": "wiki-random"
}

def execute(str):
    currentApp = ''
    for key in apps:
        if key in str:
            currentApp = apps[key]
    if currentApp == '':
        return 'Sorry, I can\'t help you with that.'
    if currentApp == 'wikipedia':
        try:
            return wikipedia.summary(str[14:])
        except wikipedia.exceptions.PageError as e:
            return f'Sorry, I couldn\'t find any wikipedia articles for {str[14:]}'
    if currentApp == 'wiki-random':
        return wikipedia.WikipediaPage(title=wikipedia.random()).summary
    