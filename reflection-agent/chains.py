from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

gpt4o = ChatOpenAI(name="gpt-4o", temperature=0)

reflection_prompt = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "Youu are a viral twitter influencer grading a tweet. Generate a critique and recommendations for the user.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ],
)

generation_prompt = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts. If the user provides critique or recommendations then respond to it with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_chain = generation_prompt | gpt4o
reflection_chain = reflection_prompt | gpt4o
