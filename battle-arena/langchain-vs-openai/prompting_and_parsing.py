import openai
from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI


# OpenAI Chat Completion
def get_completion(model="gpt-3.5-turbo"):
    customer_email = """
    Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters worse,
    the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!
    """

    style = """
    American English in a calm and respectful tone
    """

    prompt = f"""
    Translate the text that is delimited by triple backticks into a style that is {style}.
    text: ```{customer_email}```
    """

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message.content


def langchain_get_completion(model="gpt-3.5-turbo"):
    chat = ChatOpenAI(model=model, temperature=0)

    customer_email = """
    Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters
    worse, the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!
    """

    customer_style = """
    American English in a calm and respectful tone
    """

    template_string = """Translate the text that is delimited by triple backticks into a style that is {style}.
    text: ```{text}```
    """

    prompt_template = ChatPromptTemplate.from_template(template_string)

    customer_messages = prompt_template.format_messages(
        style=customer_style,
        text=customer_email
    )

    customer_response = chat.invoke(customer_messages)

    return customer_response


print(langchain_get_completion())

