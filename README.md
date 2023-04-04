# Wiki Chatbot
wikichatbot is a chatbot that can answer your queries about topics you specify by fetching information from Wikipedia.


## Dependencies
wikichatbot has the following dependencies:

* random
* string
* scikit-learn
* wikipedia-api
* nltk


## You can install these dependencies using the following command:
To use wikichatbot, you need to have Python installed on your system. Once Python is installed, you can clone this repository and run the wikichatbot.py file using the following command:



1.  Clone the repository

```
git clone https://github.com/tikendraw/wiki-chatbot.git
```
2. Install the required libraries
```
pip install -r requirements.txt
```
3. Run the wikichatbot.py file
```
python wikichat.py
```

## Usage
When you run the wikichatbot.py file, wikichatbot will greet you and ask you what topic you want to talk about. You should enter the exact title of a Wikipedia article. wikichatbot will then fetch the summary and text of the article from Wikipedia and use it to answer your queries.

You can ask wikichatbot questions about the topic by typing your question in the terminal. wikichatbot will use natural language processing and cosine similarity to find the most relevant sentence in the article and use it to answer your question.

If you want to change the topic, you can say "new topic" or "change topic" and wikichatbot will ask you for a new topic.

If you want to exit, you can say "bye" and wikichatbot will say goodbye.

## License
This is just a fun project and it is not licensed.
