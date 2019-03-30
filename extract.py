import os
import pprint
DIR = './workbase'
number = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
commitObjs = [(int, str)]
for i in range(1, number, 1):
    content = open("./workbase/" + str(i) + ".txt")
    canPrintLines = False
    msg = ""
    for line in content:
        if line.startswith("diff"):
            canPrintLines = False # We have found a diff so the message has ended
        if canPrintLines:
            if (line != "\n"):
                msg = msg + line.strip()
        if line.startswith("Date"):
            canPrintLines = True # We have found a date so we can pick up the message
    commitObjs.append((i, msg))
pprint.pprint(commitObjs)
# print("extracted msgs")

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt') # if necessary...
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]
'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))
vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
# print(vectorizer)
def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]
issueMsg = "I attempted to change my password to the string \"Q|~>(I%$9r*IctB1yRBWJL\"|. This does not change my password, but this is unclear from the UI. I think what might be happening is an error appears for a moment, but the page is immediately reloads, dismissing the error.It also seems like in general, changing passwords via the settings page is broken? I can change my password via password reset, but not the settings page. That's probably a separate bug, though.This is on the Recurse Center's Zulip instance, not sure what version it's running."
simBasedCommits = []
for commitObj in commitObjs:
    sim = cosine_sim(str(issueMsg), str(commitObj))
    if (sim > 0.0):
        simBasedCommits.append((sim, commitObj))
        print(sim)
        print(commitObj)
from operator import itemgetter
sorted(simBasedCommits, key=itemgetter(0))
for simBasedCommit in simBasedCommits:
    print(str(simBasedCommit[0]) + ',' + str(simBasedCommit[1][0]))