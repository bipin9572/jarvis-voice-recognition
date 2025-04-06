from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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"
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)