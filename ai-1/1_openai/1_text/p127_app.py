import openai

prompt = '''# "Hello World!" 표시
    def helloworld():
'''

resopnse = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=0,
)
print(resopnse.choices[0].text)