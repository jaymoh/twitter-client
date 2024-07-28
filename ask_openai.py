#!/usr/bin/env python3

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI


def ask_openai(prompt):
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        print("Missing OpenAI API Key")
        sys.exit(1)

    client = OpenAI(api_key=openai_api_key)

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo-0125",
                                                  messages=[
                                                      {"role": "system", "content": "You are a helpful assistant."},
                                                      {"role": "user", "content": prompt}
                                                  ])
        # Write response to a file
        with open("response.json", "w") as f:
            f.write(str(response))
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Error while fetching quote:", e)
        return None


if __name__ == "__main__":
    while True:
        question = input("Enter a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Exiting the chat.")
            break
        answer = ask_openai(question)
        if answer:
            print(answer)
            print() # Empty line
        else:
            print("Failed to fetch answer from OpenAI.")
