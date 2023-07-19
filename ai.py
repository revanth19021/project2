import openai

openai.api_key="Your API_key_Here"

model_engine="text-davinci-003"
prompt=input("enter the promp: ")

#generate a response

completion=openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response=completion.choice[0].text
print(response)