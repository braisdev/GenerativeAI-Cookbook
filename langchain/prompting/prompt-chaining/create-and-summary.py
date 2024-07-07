from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (ChatPromptTemplate)
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI

create_prompt = ChatPromptTemplate.from_template("""Write a fiction story about how the {subjects} save the 
earth from dangerous giant aliens""")

summarize_prompt = ChatPromptTemplate.from_template("""Give me an ordered list summarizing what happened in this 
story: {story}""")


@chain
def create_and_summary_chain(subjects: str):
    model = ChatOpenAI(model="gpt-4-0125-preview")

    create_prompt_val = create_prompt.invoke({"subjects": subjects})
    create_output = model.invoke(create_prompt_val)
    parsed_create_output = StrOutputParser().invoke(create_output)

    summarize_chain = summarize_prompt | model | StrOutputParser()

    print("Let's summarize!")

    return summarize_chain.invoke({"story": parsed_create_output})


print(create_and_summary_chain.invoke("orcas"))
