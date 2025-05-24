import openai

prefix_prompot = """def helloworld(): 
    '''
    설명 : """ 
suffix_prompot = """
    '''

    print("Hello World!")

helloWorld()
"""
resopnse = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prefix_prompot,
    suffix=suffix_prompot,
    temperature=0.7,
    max_tokens=200,
)
print(resopnse.choices[0].text)