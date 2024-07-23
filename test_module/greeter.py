from translate import Translator

translator = Translator(to_lang="zh")
translation = translator.translate("Hello, I love you")
print(translation)