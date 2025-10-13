import random

words = [
    "freedom","journey","staring","painter","mirrors","beneath","arrival","silence","courage","fitness",
    "trouble","captain","fortune","gardens","holiday","justice","library","machine","natural","passion",
    "quality","respect","station","teacher","uncover","variety","warning","yelling","zealous","balance",
    "brother","climate","diamond","express","fiction","genuine","history","imagine","jackets","kingdom",
    "leaders","monster","nursing","opinion","protect","recover","special","traffic","uniteds","victory",
    "wealthy","writers","against","barrier","concert","deliver","enhance","friends","glimpse","honesty",
    "insight","justice","keeping","letters","message","nothing","officer","patient","quickly","running",
    "seasons","towards","upgrade","virtual","wonders","younger","zephyrs","adviser","bravery","counsel",
    "dancers","explore","fishing","grocery","harmony","inspire","jewelry","kindred","landing","morning",
    "network","outcome","picture","railway","science","tourism","upwards","village","whisper","yielded",
    "zeolite","absolve","brewing","channel","deliver","essence","fashion","gallery","healthy","insight",
    "justice","kingpin","logical","musical","notable","options","perfect","railcar","skilled","theater",
    "uniform","venture","warrior","zephyrs","antique","builder","central","defense","elegant","forever",
    "gateway","harvest","inquiry","junglee","kinetic","limited","moments","neutral","outline","passage",
    "readers","savings","therapy","uncover","version","writers","younger","zealous","beloved","crystal",
    "destiny","elected","flavors","glacier","highest","improve","journey","keynote","lessons","matters",
    "novelty","orchard","prairie","require","sisters","through","uniform","vintage","warfare","zeolite",
    "airport","breathe","collect","driving","element","forward","general","housing","invited","justice",
    "keeping","legends","measure","nothing","outside","present","quickly","reading","succeed","tonight",
    "upgrade","variety","weather","yielded","zephyrs","another","borders","control","distant","explain",
    "fortune","genuine","harvest","impress","journey","kingdom","letters","morning","natural","outline"
]

word = random.choice(words)
word_string = []
life = 3
for x in word:
    word_string.append(x)

user_word = ["_", "_", "_", "_", "_", "_", "_"]

while life > 0:
    while user_word != word_string:
        user_letter = input("Guess a letter: ")
        for x in range (7):
            if user_letter == word_string[x]:
                user_word[x] = user_letter
            else:
                life -= 1
        print(user_word, f"You have {life} lives left")
    print("Correct!")
print("Gameover")