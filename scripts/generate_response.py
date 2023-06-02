import openai
from time import time

with open("openaikey.txt", "r") as f:
    openai.api_key = f.read()

def generate_response(user_input):

    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=user_input,
        # max_tokens=1000,
        temperature=0.4,
        )

        message = response.choices[0].message.content
        return message
    
    except openai.error.RateLimitError:
        print("Rate limit reached. Wait 1 min:)")
        time.sleep(60)

    # except openai.error.InvalidRequestError:
        
    

def main():
    while True:
        print(generate_response([{"role":"user","content": input("Enter: ")}]))

if __name__ == "__main__":
    main()