from openai import OpenAI


def get_lines(topic, language):
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": f"I will provide you a topic. Your task is to generate a sentence with approximately 500 characters in {language}. In your output include only the sentence, nothing else."
            },
            {
                "role": "user",
                "content": f"{topic}"
            }
        ]
    )
    yo_line = completion.choices[0].message.content
    return yo_line

# print(get_lines("cat","Russian"))
