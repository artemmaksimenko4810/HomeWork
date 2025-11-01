N = int(input())

all_lang = []

for i in range(N):
    Mi = int(input())
    student_lang = set()

    for j in range(Mi):
        lang = input()
        student_lang.add(lang)
    all_lang.append(student_lang)

if all_lang:
    usual_lang = set.intersection(*all_lang)
    all_known_lang = set.union(*all_lang)

    print(len(usual_lang))
    for language in sorted(usual_lang):
        print(language)


    print(len(all_known_lang))
    for language in sorted(all_known_lang):
        print(language)
