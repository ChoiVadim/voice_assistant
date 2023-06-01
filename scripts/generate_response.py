import openai

with open("openaikey.txt", "r") as f:
    openai.api_key = f.read()

def generate_response(user_input):

    prompt = [{"role": "system", "content": """As an AI language model, I try my best to understand and respond 
    in the language that is used to communicate with me. If you ask me a question in English, I will respond in 
    English. If you ask me a question in Korean, I will respond in Korean. If you ask me a question in Russian, 
    I will respond in Russian."""}]

    prompt.append({"role":"user","content":user_input})

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=prompt,
    max_tokens=1000,
    temperature=0.2,
    )

    message = response.choices[0].message.content
    prompt.append({"role": "system", "content": message})

    return message

def main():
    generate_response(input())

if __name__ == "__main__":
    main()