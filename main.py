from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

load_dotenv()

tavily =TavilyClient()

@tool
def search(query : str ) -> str:
    """"
    Tool that searches over internet 

    Args : qurty to search for 

    Returns :
    The search result

    """
    print(f"Searching for {query}")
    return tavily.search (query=query)
    


llm = ChatOpenAI (model="gpt-4o")
tools= [search]
agent= create_agent (model=llm, tools=tools )





def main():
    print("Hello from langchain-course!")
    result= agent.invoke({"messages":HumanMessage(content="What is weather in Tokyo?")})
    print(result)

  


if __name__ == "__main__":
    main()