import openai

openai.api_key = "your_secret_api_key"


def generate_openai_response(prompt):
    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completion.choices[0].text
