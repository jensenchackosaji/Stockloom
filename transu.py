from googletrans import Translator


def translate_to_malayalam(text):
    try:
        translator = Translator()
        translated = translator.translate(text, src='en', dest='ml')
        return translated.text
    except Exception as e:
        print("An error occurred:", str(e))
        return None


def main():
    print("English to Malayalam Converter")
    while True:
        input_text = input("Enter English text (or 'exit' to quit): ")

        if input_text.lower() == 'exit':
            break

        malayalam_text = translate_to_malayalam(input_text)
        if malayalam_text:
            print("Malayalam Translation: ", malayalam_text)
        else:
            print("Translation failed. Please try again.")


if __name__ == "__main__":
    main()
