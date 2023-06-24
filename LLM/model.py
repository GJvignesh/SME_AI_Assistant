import constants as c
import openai

openai.api_key = ''


def answer(meta_data_about_project, question_from_client):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=question_from_client,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        system=c.base_prompt + meta_data_about_project
    )
    return response.choices[0].text

