import openai

with open("openaikey.txt", "r") as f:
    openai.api_key = f.read()

    
def image_generation(prompt = ""):
    response = openai.Image.create(
        prompt=prompt,
        size="1024x1024",
        n=1
    )
    image_url = response["data"][0]

    return image_url.values()

def image_variations(image):
    try:
        response = openai.Image.create_variation(
            open(image, "rb"),
            n=1,
            size="1024x1024"
        )

    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)

    return response['data'][0]['url']

def main():
    image_generation("dog with cat")

if __name__ == "__main__":
    main()