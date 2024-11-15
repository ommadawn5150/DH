# CERN LHC RAG

## Web based RAG system

This is a web based RAG system for CERN LHC. RAG is a model that can generate answer from given question and context. 
When you ask a question, RAG will find the answer from the context and return it.
You can use this system via Jupyter notebook or discord bot. 

## Installation

To install this RAG, follow these steps:

### Environment setup

1. Clone the repository: `git clone https://github.com/ommadawn5150/LHC-RAG.git`
2. Navigate to the project directory: `cd LHC-RAG`
3. Setup python venv of version `3.10.12` : `python3 -m venv venv`
4. Enter the virtual environment `source ./venv/bin/activate` (for Linux/Mac users)
5. Install required python packages: `pip install -r requirements.txt`

### API setup

1. Get the groq API key : https://console.groq.com/
2. Set api key as environment variable: `export GROQ_API_KEY={YOUR_API_KEY}`

## Usage

### Jupyter notebook
Open `rag.ipynb` and follow the notebook instruction.  

### discord bot
Set discord bot TOKEN as environment variable: `export DISCORD_BOT_TOKEN={YOUR_TOKEN}`  
Execute `python3 rag.py` on the shell

## Features

### Hugging face embeddings 

For embedding model this rag system is using `intfloat/multilingual-e5-large-instruct` locally.  
This model also performed well in Leaderborad : MultilabelClassification #2, Retrieval w/Instructions #11. ([LeaderBoard](https://huggingface.co/spaces/mteb/leaderboard))

multilingual-e5 has 4 tyoes for its size, every size and # of dimension is following.  

| model	| size | # of dimension |
| ---- | ----: | ----: |
| small | 471MB | 384 |
| base	| 1.11GB | 768 |
| large	| 2.24GB | 1024 |
| large-instruct	| 3.2GB | 1024 |


### Groq 

This rag is using groq api. The api is availabel for free now ('24/11/14), but it might costs in the future.  
Default llm model is using `llama3-groq-70b-8192-tool-use-preview`.
You can see available models here https://console.groq.com/docs/models .  
To change the model, just replace `model_name` to other model name.


### discord.py

You can use rag as discord bot via discord bot API by using discord.py.  
DISCORD_BOT_TOKEN is required to use this feature. You can get the token from discord developer portal.

## References

- [intfloat/multilingual-e5-large-instruc](https://huggingface.co/intfloat/multilingual-e5-large-instruct "multilingual-e5-large-instruc")
- [Groq](http://groq.com "Qiita Home")
- [discord.py](https://github.com/Rapptz/discord.py)
- [Discord Developer Portal](https://discordapp.com/developers/applications/)
- [Pythonで実用Discord Bot(discordpy解説)](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)


## License

This package is open-sourced software licensed under the [MIT license](https://choosealicense.com/licenses/mit/)
