user = input('> ')

def convertEmoji(message):
    words = message.split(' ')
    emojis = {
        ":)":"😄",
        ":(":"😢",
        "israel":"🇮🇱"
    }
    output = ''
    for word in words:
        output+= f"{emojis.get(word,word)} "
    return output



print(convertEmoji(user))
