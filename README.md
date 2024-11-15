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

Before running the bot, make sure you have set the environment variable `DISCORD_BOT_TOKEN` with your discord bot token and you have invited the bot to your server.
And you need to save document loader which is made in `rag.ipynb` as pickle file.  
After above preparation, execute `python3 rag.py` on venv shell.

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
Default llm model is using [`llama3-groq-70b-8192-tool-use-preview`](https://groq.com/introducing-llama-3-groq-tool-use-models/).  
You can see other available models here https://console.groq.com/docs/models .  
To change the model, just replace `model_name` to other model name in `helpers.py`.


### discord.py

You can use rag as discord bot via discord bot API by using discord.py.  
DISCORD_BOT_TOKEN is required to use this feature. You can get the token from discord developer portal.

## Validation

Tried some questions and validated the result.

Q : ATLASの総質量は？ (7000 tonne)  
>ATLASの総質量は、約7,000トンです。この質量は、検出器の大きさと複雑さを反映しています。ATLASは、LHCの4つの主要検出器の1つで、素粒子物理学の研究に使用されています。
>
>Source: https://home.cern/science/experiments/l3

Q : LHCはいつから運用されていますか？ (2008年 9月 10日)
>LHCは2008年9月10日に初めて陽子ビームを加速し、2010年3月30日に7TeVで運用を開始しました。2013年2月13日にLHCは、2015年4月5日に13TeVで運用を再開しました。LHCは、2023年まで運用を続ける予定です。 
>
>Reference(s):
>https://home.cern/science/engineering/restarting-lhc-why-13-tev

Q : LHCのデータ量は?
>LHCのデータ量は、13TeVの衝突エネルギーで運転することで、より多くの粒子衝突イベントが生成されるため、従来の7TeVの運転時よりも大幅に増加します。この高エネルギーでの運転は、新しい粒子の検出や、既知の粒子の性質の詳細な研究を可能にするデータを提供します。
>
>Source: https://home.cern/science/engineering/restarting-lhc-why-13-tev

Q : ATLAS検出器の構造は？
>ATLAS検出器は、LHCの4つの主要検出器の1つです。ATLAS検出器は、粒子衝突の詳細を捉えるために設計されています。検出器の構造は、以下の4つの主要部分で構成されています。
>- **Inner Detector (ID)**: これは、粒子の軌跡を捉えるための最も内側の検出器です。IDは、シリコンの微細なピクセル検出器、シリコンのストリップ検出器、トランスション・レジストリー・トラッカー（TRT）で構成されています。
>- **Calorimeters**: これらは、粒子のエネルギーを測定するための検出器です。ATLASのCalorimetersは、Electromagnetic Calorimeter（EMCal）とHadronic Calorimeter（HCal）で構成されています。
>- **Muon Spectrometer**: これは、ミューオンの検出と測定を行うための検出器です。Muon Spectrometerは、ミューオン・トラッカーとミューオン・カロリメータで構成されています。
>- **Trigger and Data Acquisition**: これは、検出器が捉えたデータを処理し、有用な情報を抽出するためのシステムです。
>
>ATLAS検出器は、LHCの13TeVの衝突エネルギーで粒子を捉えるように設計されています。このエネルギーは、素粒子物理学の研究において、新しい粒子や相互作用の発見を可能にする高エネルギー領域を探検することを目的としています。
>- **Source:** [1](https://home.cern/science/experiments/l3), [2](https://home.cern/science/experiments), [3](https://home.cern/science/engineering/restarting-lhc-why-13-tev), [4](https://home.cern/fr/science/accelerators)

## References

- [intfloat/multilingual-e5-large-instruc](https://huggingface.co/intfloat/multilingual-e5-large-instruct "multilingual-e5-large-instruc")
- [Groq](http://groq.com "Qiita Home")
- [discord.py](https://github.com/Rapptz/discord.py)
- [Discord Developer Portal](https://discordapp.com/developers/applications/)
- [Pythonで実用Discord Bot(discordpy解説)](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)


## License

This package is open-sourced software licensed under the [MIT license](https://choosealicense.com/licenses/mit/)
