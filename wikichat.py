# ## Import necessary libraries

import random
import string  # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")
import wikipediaapi


import nltk

# nltk.download('popular', quiet=True) # for downloading packages
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only
# nltk.download()


lemmer = nltk.stem.WordNetLemmatizer()
# WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = {ord(punct): None for punct in string.punctuation}


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def wikisource(topic: str) -> str:

    wiki_wiki = wikipediaapi.Wikipedia(
        language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    page = wiki_wiki.page(topic)

    # Page - Exists: True
    try:
        if page.exists():
            return page.summary + page.text
        elif page.exists() == False:
            raise ValueError(
                f"{topic} article does not exists in Wikipedia. You may have Misspelled"
            )
    except Exception as e:
        print("Exception occured in wikisource: ", e)


def get_context(topic, online: bool = True, path_to_file: str = None):

    if path_to_file is not None and not online:

        try:
            with open(path_to_file, "r", errors="ignore") as f:
                raw = f.read().lower().encode()
                # raw = raw.lower()
        except Exception as e:
            print("Exception occured whlie Reading file : ", e)
    elif online and path_to_file is None:
        raw = wikisource(topic)

    return nltk.sent_tokenize(raw)



GREETING_INPUTS = (
    "hello",
    "hi",
    "greetings",
    "sup",
    "what's up",
    "hey",
)
GREETING_RESPONSES = [
    "hi",
    "hey",
    "*nods*",
    "hi there",
    "hello",
    "I am glad! You are talking to me",
]
TOPIC_CHANGE_WORDS = [
    "new topic",
    "change topic",
    "change subject",
    "change topic",
    "topic change",
    "subject change",
]


def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response, sent_tokens):
    robo_response = ""
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(
        tfidf[-1], tfidf
    )  # finding similarity between userinput and text data
    idx = vals.argsort()[0][
        -2
    ]  # argsorting and picking the second last value as last value is userinput itself to is matches to itself perfectly
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response += "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response += sent_tokens[idx]
        return robo_response


flag = True
topic = str()


print(
    """ROBO: My name is Robo. I will answer your queries about topics you specify.
      To change topic say "change topic or new topic". If you want to exit, type Bye!"""
)

while flag:
    print("\n")

    if len(topic.strip()) == 0:
        print("ROBO: Hi")
        topic = str(
            input(
                "ROBO: what do you Want to talk about?(Case Sensitive: Sould be Exact as wikipedia title.): "
            )
        )
        sent_tokens = get_context(topic)
        print(f"ROBO: Lets talk about {topic}")

    user_response = input("USER: ")
    user_response = user_response.lower()

    if user_response != "bye" and user_response not in TOPIC_CHANGE_WORDS:
        # print('USER: ', user_response)
        if user_response in ["thanks", "thank you"]:
            flag = False
            print("ROBO: You are welcome..")
        elif greeting(user_response) is None:
            print("ROBO: ", response(user_response, sent_tokens))
            sent_tokens.remove(user_response)

        else:
            print(f"ROBO: {greeting(user_response)}")

    elif user_response in TOPIC_CHANGE_WORDS:
        topic = ""

    else:
        flag = False
        print("ROBO: Bye! take care..")
