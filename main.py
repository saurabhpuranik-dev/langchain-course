from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")

    information = """
    Elon Reeve Musk (born June 28, 1971) is a businessman and entrepreneur
    known for Tesla, SpaceX, X, and xAI.
    """

    prompt = ChatPromptTemplate.from_template(
        """
        With the given information below:

        {information}

        Please provide:
        1) A short summary
        2) 3 interesting facts
        """
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )

    chain = prompt | llm

    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()