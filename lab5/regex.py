import re
# #1task
# pattern1 = re.compile(r"ab*")
# text = "ab abb abbb a abbbabb ababab"

# matches = pattern1.findall(text)

# print(matches)

# #2task
# pattern2 = re.compile(r"ab{2,3}")
# matches = pattern2.findall("ab abb abbb abbbb")

# print(matches)

# #3task
# pattern3 = re.compile(r"[a-z]+\_")
# text = "a_def_123_ghi_456_jkl"
# matches = pattern3.findall(text)

# print(matches)

# #4task
# pattern4 = re.compile(r"[A-Z]{1}[a-z]+")
# text = "Hello world"
# matches = pattern4.findall(text)
# print(matches)

# #5task
# pattern5 = re.compile(r"a.+b\Z")
# text = "appleb"
# matches = pattern5.findall(text)
# print(matches)

# #task6
# pattern6 = re.compile(r"[ ,.]")
# text = "This is a sample, text."
# modified_text = re.sub(pattern6, ":", text)
# print(modified_text)

# #task7

# def snakeToCamel(text):
#     camelCase=""
#     pattern = re.compile(r"[_]")
#     words=pattern.split(text)
#     for i, word in enumerate(words):
#         if i != 0:
#             camelCase+=word.capitalize()
#         else: 
#             camelCase += word
#     return camelCase

# text = "hello_world"
# print(snakeToCamel(text))

# #task8
# def spaces(text):
#     res = ""
#     pattern = re.compile(r"[A-Z][a-z]+")
#     words = pattern.findall(text)
#     for i, word in enumerate(words):
#         if i != 0:
#             res += ", " + word
#         else:
#             res += word
#     return res

# text = "SplitThisStringAtUppercaseLetters"
# print(spaces(text))

# #task9
# def cap(text):
#     res = ""
#     pattern = re.compile(r"[A-Z][a-z]+")
#     words = pattern.findall(text)
#     for i, word in enumerate(words):
#         if i != 0:
#             res += " " + word
#         else:
#             res += word
#     return res

# text = "SplitThisStringAtUppercaseLetters"
# print(cap(text))

# #task10
# def camel_to_snake(text):
#     res = ""
#     pattern = re.compile(r"[A-Z][a-z]+")
#     words = pattern.findall(text)
#     for i, word in enumerate(words):
#         if i != 0:
#             res += "_" + word.lower()
#         else:
#             res += word.lower()
#     return res

# text = "SplitThisStringAtUppercaseLetters"
# print(camel_to_snake(text))