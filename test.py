from dotenv import load_dotenv
load_dotenv()

import os
import openai

def run_gpt(prompt, init):
    openai.api_key = os.getenv('API_KEY')

    model_engine = "text-davinci-002"

    # prompt = "how to make gui python exe?"
    if (init):
        completions = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.5
        )
    # else:
        # completions = openai.Completion(prompt)

    message = completions.choices[0].text
    return message
