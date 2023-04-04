# Wiki Chatbot
Robo is a chatbot that can answer your queries about topics you specify by fetching information from Wikipedia.

## Installation
To use Robo, you need to have Python installed on your system. Once Python is installed, you can clone this repository and run the robo.py file using the following command:


```
python robo.py
```

## Dependencies
Robo has the following dependencies:

* random
* string
* scikit-learn
* wikipedia-api
* nltk


## You can install these dependencies using the following command:


1.  Clone the repository

```
git clone https://github.com/tikendraw/wiki-chatbot.git
```
2. Install the required libraries
```
pip install -r requirements.txt
```
3. Run the robo.py file
```
python wikichat.py
```

## Usage
When you run the robo.py file, Robo will greet you and ask you what topic you want to talk about. You should enter the exact title of a Wikipedia article. Robo will then fetch the summary and text of the article from Wikipedia and use it to answer your queries.

You can ask Robo questions about the topic by typing your question in the terminal. Robo will use natural language processing and cosine similarity to find the most relevant sentence in the article and use it to answer your question.

If you want to change the topic, you can say "new topic" or "change topic" and Robo will ask you for a new topic.

If you want to exit, you can say "bye" and Robo will say goodbye.

## License
This is just a fun project and it is not licensed.
