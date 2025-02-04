from text_to_speech import save

text = "Hello, Dear friends! Welcome to this program"
language = "hi"#specify the language (IETF language tag)
output_file = "greeting2.mp3"
#specify the output file(only accepts.mp3)
save(text, language, Fast=True, file=output_file)