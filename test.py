import os
import openai
import pyttsx3
'''
openai.api_key="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"
ram=openai.Engine.list()

prompt="help"
response=openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=996)
responses=response.choice[0].text
print(responses)
#print(response['choice'][0]['text'])
#print(response['choices'][0]['message']['content'])
'''
for i in range (0,3):
  openai.api_key = "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"

  query = input("enter the question")
  start_sequence = "AI:"
  restart_sequence = "Human: "
  prompt = query
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=1024,
    # n=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=None
  )
  mesg = response.choices[0].text
  print(mesg)

