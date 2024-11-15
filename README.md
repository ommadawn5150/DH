# CERN LHC RAG

## Web based RAG system

This is a web based RAG (Retrieval-augmented generation) system for CERN LHC. RAG is a model that can generate answer from given question and context. 
When you ask a question, RAG will find the answer from the context and return it.
You can use this system via Jupyter notebook or discord bot. 

## Installation

To install this RAG sytem, follow these steps:

### Environment setup

1. Clone the repository: `git clone https://github.com/ommadawn5150/LHC-RAG.git`
2. Navigate to the project directory: `cd LHC-RAG`
3. Setup python venv of version `3.10.12` : `python3 -m venv venv`
4. Enter the virtual environment `source ./venv/bin/activate` (for Linux/Mac users)
5. Install required python packages: `pip install -r requirements.txt`

### API setup

1. Get the groq API key : https://console.groq.com/
2. Set api key as environment variable: `export GROQ_API_KEY={YOUR_API_KEY}`

### Discord bot setup

1. Get the discord bot token from discord developer portal: https://discordapp.com/developers/applications/
2. Set discord bot TOKEN as environment variable: `export DISCORD_BOT_TOKEN={YOUR_TOKEN}`
3. Invite the bot to your server

## Usage

### Jupyter notebook
Open `rag.ipynb` and follow the notebook instruction.  

### discord bot
Execute `python3 rag.py` on venv shell.

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

## Validation

Tried some questions and validated the result.

Q : ATLASの総質量は？ (7000 tonne)  
>RAG A :  
>ATLASの総質量は7000トンです。  
>Source: https://home.cern/science/experiments/atlas

Q : LHCはいつから運用されていますか？ (2008年 9月 10日)
>LHCは2008年9月10日に初めて運用が始まりました。CERNの加速器複合体の最新の追加です。LHCは、27kmの環状の超伝導磁石と、粒子のエネルギーを高めるための加速構造で構成されています。  
Reference(s):  
> https://home.cern/science/accelerators/large-hadron-collider  
> https://home.cern/science/accelerators/large-hadron-collider

Q : LHCのデータ量は?
>LHCのデータ量は、非常に大きなものです。LHCは、1秒間に40MHzの衝突を生成し、1つの衝突で1MBのデータが生成されます。このため、1秒間に40MBのデータが生成されます。1日で28800秒がありますから、1日で1.15TBのデータが生成されます。LHCは、1年で300日程度運営されるため、1年で345TBのデータが生成されます。
>
>LHCのデータは、CERNのOpen Data Portalで公開されています。このポータルでは、ALICE、ATLAS、CMS、LHCbの4つの実験のデータが公開されています。各実験のデータは、異なる形式で提供されていますが、一般的にROOT形式で提供されています。
>
>LHCのデータは、研究者たちが素粒子物理学の研究に使用しています。このデータを分析することで、新しい粒子の発見や既知の粒子の性質の詳細な研究が行われます。
>
>LHCのデータは、CERNのOpen Data Portalでダウンロードすることができます。このポータルでは、データのダウンロード方法や、データの使用に関するガイドラインも提供されています。
>
>LHCのデータは、CERNのOpen Data Portalで公開されています。このポータルでは、ALICE、ATLAS、CMS、LHCbの4つの実験のデータが公開されています。各実験のデータは、異なる形式で提供されていますが、一般的にROOT形式で提供されています。
>
>LHCのデータは、CERNのOpen Data Portalでダウンロードすることができます。このポータルでは、データのダウンロード方法や、データの使用に関するガイドラインも提供されています。  
Reference(s):  
>https://home.cern/science/computing/open-source-open-science  
>https://home.cern/science/experiments  
>https://home.cern/science/experiments  
>https://home.cern/science/experiments/cms


## References

- [intfloat/multilingual-e5-large-instruc](https://huggingface.co/intfloat/multilingual-e5-large-instruct "multilingual-e5-large-instruc")
- [Groq](http://groq.com "Qiita Home")
- [discord.py](https://github.com/Rapptz/discord.py)
- [Discord Developer Portal](https://discordapp.com/developers/applications/)
- [Pythonで実用Discord Bot(discordpy解説)](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)


## License

This package is open-sourced software licensed under the [MIT license](https://choosealicense.com/licenses/mit/)
