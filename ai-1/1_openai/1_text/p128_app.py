import openai

messages = [
    {"role": "system", "content": "서연이는 여고생 여동생 캐릭터의 채팅 AI입니다. 남동생과 대화합니다."},
    {"role": "user", "content": "안녕!"},
]

resopnse = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
print(resopnse)
print('-'*50)
print(resopnse['choices'][0]['message']['content']) 