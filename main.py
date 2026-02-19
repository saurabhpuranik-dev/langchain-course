from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import prompt

load_dotenv()


def main():
    print("Hello from langchain-course!")

    information = """
    Elon Reeve Musk (born June 28, 1971) is a businessman and entrepreneur
    known for Tesla, SpaceX, X, and xAI.
    """

    summary_template = """
    from given information {information} about a person I want you to create 
    1) short summary
    2) two interresting facts about them

"""

    summary_prompt_template = PromptTemplate(
        input_variables=[information], template=summary_prompt_template
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=120
    )

    chain = summary_prompt_template | llm

    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()