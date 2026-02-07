def main():
    text = input()
    result = convert(text)
    print(result)
def convert(text):
    replacements = {
        ":)": "🙂",
        ":(": "🙁"

    }

    for emoticon , emoji in replacements.items():
        text = text.replace(emoticon, emoji)

    return text
main()

