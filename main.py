from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from langchain_tavily import TavilySearch
 

load_dotenv()

tavily =TavilyClient()

class Source (BaseModel) :
    """" Schema for source used by agent  """
    url :str = Field (description="The URL of source ") 


class AgentResponse (BaseModel):

    """ Schema for response from Agent with answer and source """

    answer:str = Field (description="The Agents answer to query")
    sources: List[Source] = Field(default_factory=list, description= "List of sources used to generate the answer")
    


    


llm = ChatOpenAI (model="gpt-4o-mini")
tools= [TavilySearch()]
agent= create_agent (model=llm, tools=tools, response_format=AgentResponse )





def main():
    print("Hello from langchain-course!")
    result= agent.invoke({"messages":HumanMessage(content="What is weather in Tokyo?")})
    print(result)

  


if __name__ == "__main__":
    main()