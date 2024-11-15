from langchain_groq import ChatGroq
from IPython.display import Markdown, display
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class LLM():
    prompt_template = """
        <|system|>
        Use the following pieces of context to answer the question at the end. : {context}
        And you need to answer with following engagements;
            - If you don't know the answer, just say that you don't know, don't try to make up an answer.
            - Use markdown formatting when displaying code.
            - Use proper grammar and punctuation.
            - Add additional information if you think it will help the user.
            - Start a new line for each paragraph.
            - Use complete sentences.
            - Use markdown formatting.
            - Emphasis should be used to terminologies.
            - Give sources you used at the end.
            - Answer in Japanese.
        </s>
        <|user|>
        {question}
        </s>
        {source}
    """
    model_name = "llama3-groq-70b-8192-tool-use-preview"


    def __init__(self, prompt_template="", model_name=""):
        if model_name != "":
            self.model_name = model_name
        self.client = ChatGroq(
                            model = self.model_name,
                            temperature=0,
                            max_tokens=None,
                            timeout=10,
                            max_retries=2
                            )

        if prompt_template != "":
            self.prompt_template = prompt_template
        
        #  Create the PromptTemplate Instance
        self.prompt = PromptTemplate(
            input_variables=[
                "context",
                "question",
                "source"
                ],
            template=self.prompt_template,
        )
        print("Prompt Template Created")
        print(self.prompt)

        self.llm_chain = self.prompt | self.client | StrOutputParser()

    def format_docs(self,docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def format_sources(self,docs):
        """
        Extracts and formats the sources (metadata) from the retrieved documents.
        This function ensures that the source information is passed to the LLM as part of the context.
        """
        # Extract sources (e.g., URLs or document titles) from metadata
        sources = [doc.metadata.get('source', 'Unknown Source') for doc in docs]
        # Join the sources into a single string to pass to the LLM
        return "Sources:\n" + "\n".join(sources)
    
    def show_markdown(self, markdown_text,title=None):
        display(Markdown(title + markdown_text))
    
    def chat(self, user_input,retriever, show=True,source=True):
        if source:
            rag_chain = (
                {
                    "context": retriever | self.format_docs,    # Retrieval Step for context
                    "question": RunnablePassthrough() ,     # Prompt Generation
                    "source": retriever | self.format_sources
                }
                | self.llm_chain                                # Generation Step
            )
        else:
            rag_chain = (
                {
                    "context": retriever | self.format_docs,    # Retrieval Step for context
                    "question": RunnablePassthrough()     # Prompt Generation
                }
                | self.llm_chain                                # Generation Step
            )

        response = rag_chain.invoke(user_input)

        if show : self.show_markdown(response, title="# Answer\n")
        return response
    
    def not_fine_tuned_chat(self, user_input, show=True):
        response = self.llm_chain.invoke({"context": "", "question": user_input, "source": ""})

        if show : self.show_markdown(response, title="# Not trained RAG Answer\n")
        return response