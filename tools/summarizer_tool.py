from langchain.tools import tool
from langchain_openai import ChatOpenAI

@tool
def summarize_text(text: str) -> str:
    """Summarizes a long block of text into 3-5 concise bullet points.
    Use this after searching to condense information clearly."""
    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        response = llm.invoke(
            f"Summarize the following text into 3-5 clear bullet points. "
            f"Be concise and factual:\n\n{text}"
        )
        return response.content
    except Exception as e:
        return f"Summarization failed: {str(e)}"