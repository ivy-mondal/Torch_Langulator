#translierate yo line here
from openai import OpenAI


def transliterate(yo_sentence):
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system",
             "content": f"I wil give you a sentence. Your task is to transliterate the given sentence to the Latin script. Transliterate phonetically, exactly how it is pronounced. In the transliteration, use 26 English letters and spaces only. Only give the transliterated sentence, nothing else."
             },
            {"role": "user",
             "content": f"{yo_sentence}"}
        ]
    )
    result = completion.choices[0].message.content
    return result
