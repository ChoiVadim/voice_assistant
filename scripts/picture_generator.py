import openai
import webbrowser
import os

with open("openaikey.txt", "r") as f:
    openai.api_key = f.read()

    
def image_generation(prompt = "", n = 1):
    response = openai.Image.create(
        prompt=prompt,
        size="1024x1024",
        n=n
    )
    image_url = response["data"]

    return [i['url'] for i in image_url]

def image_variations(image, n = 1):
    try:
        response = openai.Image.create_variation(
            open(image, "rb"),
            n=n,
            size="1024x1024"
        )

    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)

    return response['data'][0]

def main():
    prompt = """a medium-full-shot, movie poster studio photographic portrait
    of perfect beautiful Korean women wearing strapless and tiny short pant,
    outdoors, sunset photo at golden hours, depth of field, Bokeh, shot on 
    Leica Q2, on Flickr"""

    urls = image_generation(prompt, 4)
    for url in urls:
        webbrowser.open(url, new=0, autoraise=True)

if __name__ == "__main__":
    main()