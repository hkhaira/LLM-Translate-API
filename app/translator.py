from openai import OpenAI
from app.config import OPEN_AI_API_KEY

openai_client = OpenAI()


def translate_text(input_str: str) -> str: 

    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": "You are an expert translator who translates text from english to hindi and only return translated text in json format."},
            {"role": "user", "content": input_str},
        ],
        response_format={
            "type": "json_object",
        }
    )
    return completion.choices[0].message.content

# def translate_text(input_str: str) -> str: 

#     completion = openai_client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are an expert translator who translates text from english to hindi and only return translated text"},
#             {"role": "user", "content": input_str},
#         ],
#     )
#     return completion.choices[0].message.content