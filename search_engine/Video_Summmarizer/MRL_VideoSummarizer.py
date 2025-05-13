from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

from Video_Summmarizer.i_video_summarizer import IVideoSummarizer
from langchain_ollama import OllamaLLM

class MRLVideoSummarizer(IVideoSummarizer):
    """
    Class for summarizing videos.
    """

    def __init__(self) -> None:
        """Initialize the VideoSummarizer class."""
        super().__init__()
        self.llm_model = OllamaLLM(
            model="llama3",
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n", "\n\n", "\n\n\n"],
            chunk_size=5990,
            chunk_overlap=50,
            length_function=len
        )
        self.map_prompt = """
            Act as a text summarizer. Write a concise summary of the following: 
            "{text}"
            CONCISE SUMMARY:
        """

        self.reduce_prompt = """
        Act as a text summarizer. Write a concise summary of the following text delimited by triple backquotes.
        Return your response in bullet points which covers the key points of the text.
        Do not add anything else.
        Start the summary by the following text : "The video is about: \n" 
        ```{text}```
        BULLET POINT SUMMARY:
        """

        self.map_prompt_template = PromptTemplate(template=self.map_prompt, input_variables=["text"])
        self.reduce_prompt_template = PromptTemplate(template=self.reduce_prompt, input_variables=["text"])

        self.summary_chain = load_summarize_chain(
            self.llm_model,
            chain_type="map_reduce",
            map_prompt=self.map_prompt_template,
            combine_prompt=self.reduce_prompt_template,
            verbose=True,
            return_intermediate_steps=True
        )


    def summarize(self, captions : str) -> str:
        """
        Summarize the a caption (video transcripts) of any length
        using map-reduce paradigm.
        :param caption: The caption of the video to summarize.
        :return: The summarized caption.
        """

        # Check if the captions are empty
        if not captions:
            raise ValueError("Captions cannot be empty.")
        if not isinstance(captions, str):
            raise TypeError("Captions should be a string. You have passed a %s", type(captions))
        if len(captions) == 0 :
            raise ValueError("Captions cannot be empty string.")
        # Summarize the captions when the data type is a string
        docs = self.text_splitter.create_documents([captions])
        return self.summary_chain.invoke(docs)['output_text']
