import html

my_sentence = "&lt;div&gt;This is a div&lt;/div&gt;"
print("original ", my_sentence)

# unescape html code
print("unescaped", html.unescape(my_sentence))
