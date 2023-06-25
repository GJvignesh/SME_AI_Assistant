from usellm import Message, Options, UseLLM
import constants as c

# Initialize the service
service = UseLLM(service_url="https://usellm.org/api/llm")


def answer(meta_data_about_project, question_from_client):
    # Prepare the conversation
    messages = [
        Message(role="system", content=c.base_prompt + meta_data_about_project),
        Message(role="user", content=question_from_client),
    ]
    options = Options(messages=messages)

    # Interact with the service
    response = service.chat(options)

    # Print the assistant's response
    print(response.content)
    return response.content

# Credits to https://usellm.org/docs/useLLM-py/installation-usage
