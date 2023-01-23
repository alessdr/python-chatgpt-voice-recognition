import speech_recognition as sr

import pyttsx3
import requests
import json


def call_chatgpt_api(quest):
    auth_token = "COLE_AQUI_SUA_API_KEY"
    header = {
        "Authorization": "Bearer " + auth_token
    }
    data = {
        "model": "text-davinci-003",
        "prompt": quest,
        "temperature": 1,
        "max_tokens": 500
    }

    # API
    url = "https://api.openai.com/v1/completions"
    resp = requests.post(url, json=data, headers=header)
    return resp.text


def process_response(elements):
    try:
        return json.loads(elements)['choices'][0]['text'].strip() if elements else 'No response.'
    except KeyError:
        return json.loads(elements)['error']['message'].strip()
    except Exception:
        return "Unknown error."


def recognition():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Olá sou o ChatGPT. Em que posso te ajudar? ")
        audio = mic.listen(source)

    try:
        frase = mic.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Não entendi")

    return frase


if __name__ == '__main__':
    question = recognition()
    msg = process_response(call_chatgpt_api(question))
    print(msg)

    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()
