
import cv2
from base64 import b64encode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import imutils
import requests
import time
import os
import playsound
import pygame
from gtts import gTTS
from googletrans import Translator
#from mtranslate import translate as trans
global LANGUAGES
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu', }


class azure_tts():
    def __init__(self):

        self.subscription_key = '73409a02d79d4c5791f7644b3ee8e881'
        self.location = "eastus"
        self.input_file = "sentences.txt"

        if self.subscription_key == 'YOUR_SUBSCRIPTION_KEY':
            print(
                "Kindly modify the subscription key inside this file (line 5). \nExiting...")

    def get_token(self):
        self.token_url = "https://{}.api.cognitive.microsoft.com/sts/v1.0/issueToken".format(
            self.location)
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        self.response = requests.post(self.token_url, headers=self.headers)
        self.access_token = str(self.response.text)
        return self.access_token

    def generate_speech(self, input_text, outfile, token, lang, Voice):
        self.url = "https://eastus.tts.speech.microsoft.com/cognitiveservices/v1"
        self.header = {
            'Authorization': 'Bearer '+str(token),
            'Content-Type': 'application/ssml+xml;charset = utf-8',
            'X-Microsoft-OutputFormat': 'audio-24khz-160kbitrate-mono-mp3'
        }

        '''
        You can customise your speech output here
        by changing language, gender and name
        '''

        data = """<speak version='1.0' xml:lang={}>\
                    <voice xml:lang={} xml:gender='Male' name={} rate='0'>{}</voice>\
                </speak>""".format(lang, lang, Voice, input_text)
        data = data.encode('utf-8')

        # print(data)
        try:
            response = requests.post(self.url, headers=self.header, data=data)
            response.raise_for_status()
            with open(outfile, "wb") as file:
                file.write(response.content)
            print(response)
            response.close()
        except Exception as e:
            print("ERROR: ", e)

    def Convert2Speech(self, mytext, langg):
        Lang = list(LANGUAGES.keys())[
            list(LANGUAGES.values()).index(langg.lower())]
        trans = Translator()
        ftext = trans.translate(mytext, dest=Lang)
        ftext = ftext.text
        # print(ftext)
        ftext = "%s" % (ftext)
        #tts = gTTS(text=ftext)
        return ftext

    def azure_tts_rest(self, text, lang):
        Flang = lang
        token = self.get_token()  # Each Token is valid for 10 minutes

        df = pd.read_excel('/home/pi/Desktop/STR_VR2/STR_VR2/langData.xlsx')
        ftext = self.Convert2Speech(text, langg=Flang)
        print(ftext)
        print(Flang)
        for i in df[df['LangName'] == lang].index.values:

            if df.iloc[i]['Gender'] == 'Female' and df.iloc[i]['Country'] == '(India)':

                lang = '"'+df.iloc[i]['Locale']+'"'
                voice = '"'+df.iloc[i]['ShortName']+'"'

        # print(voice)
        #outfile = os.path.join(self.output_folder, "_azure.mp3")
        self.outfile = "/home/pi/Desktop/_azure.mp3"
        self.generate_speech(ftext, self.outfile, token,
                             lang=lang, Voice=voice)
        """pygame wala code """
        time.sleep(1)  # Avoiding too many requests
        # token = sleep_and_refresh(i)  # Enable only when input file is large
        pygame.mixer.init()
        pygame.mixer.music.load(self.outfile)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        # token = sleep_and_refresh(i)  # Enable only when input file is large
        # print("DONE!")


'''
    def azure_tts_rest(self, text, lang):
        texlang = lang
        token = self.get_token()  # Each Token is valid for 10 minutes
        df = pd.read_excel('/home/pi/Desktop/STR_VR2/STR_VR2/langData.xlsx')

        for i in df[df['LangName'] == lang].index.values:

            if df.iloc[i]['Gender'] == 'Female' and df.iloc[i]['Country'] == '(India)':

                lang = '"'+df.iloc[i]['Locale']+'"'
                voice = '"'+df.iloc[i]['ShortName']+'"'
        self.outfile = "/home/pi/Desktop/_azure.mp3"
        #outfile = os.path.join(self.output_folder, "_azure.mp3")
        Lowlang = list(LANGUAGES.keys())[list(
            LANGUAGES.values()).index(texlang.lower())]
        trans = Translator()
        ftext = trans.translate(text, dest=Lowlang)
        print(ftext)
        self.generate_speech(ftext, self.outfile, token,
                             lang=lang, voice=voice)
        time.sleep(1)  # Avoiding too many requests
        # token = sleep_and_refresh(i)  # Enable only when input file is large
        pygame.mixer.init()
        pygame.mixer.music.load(self.outfile)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        # token = sleep_and_refresh(i)  # Enable only when input file is large
        print("DONE!")'''


class gcp_ocr():

    global ENDPOINT_URL, api_key
    api_key = 'AIzaSyAnOfbmrMSkYqi7zDdasspw0H9krjWyx6Q'
    ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

    def makeImageData(self, imgpath):
        self.img_req = None
        with open(imgpath, 'rb') as f:
            self.ctxt = b64encode(f.read()).decode()
            self.img_req = {
                'image': {'content': self.ctxt},
                'features': [{'type': 'DOCUMENT_TEXT_DETECTION', 'maxResults': 1}, {'type': "OBJECT_LOCALIZATION", 'maxResults': 10}]
            }
        return json.dumps({"requests": self.img_req}).encode()

    def requestOCR(self, url, api_key, imgpath):
        self.imgdata = self.makeImageData(imgpath)
        self.response = requests.post(ENDPOINT_URL,
                                      data=self.imgdata,
                                      params={'key': api_key},
                                      headers={'Content-Type': 'application/json'})
        return self.response

    def getResult(self, path):

        self.img_loc = path

        self.result = self.requestOCR(ENDPOINT_URL, api_key, self.img_loc)

        if self.result.status_code != 200 or self.result.json().get('error'):
            print("Error")

        else:
            # gg = result.json()['responses'][0]
            self.result = self.result.json()
            if "localizedObjectAnnotations" in self.result['responses'][0].keys():

                self.objdetect = self.result['responses'][0]['localizedObjectAnnotations'][0]['boundingPoly']['normalizedVertices']
            else:
                self.objdetect = None
            self.result = self.result['responses'][0]['textAnnotations'][0]['description']

        # detect_lang = result[0]['locale']
        self.text = self.result
        # print(self.text)
        # text = result.split('.')
        # for i in text:
        #   print(i)

        return self.text, self.objdetect


'''
gcp = gcp_ocr()
az = azure_tts():
# img = cv2.resize(cv2.imread("/home/pi/Desktop/test5_1.jpeg"),None, fx = 1.5, fy = 1.5)
# cv2.imwrite("/home/pi/Desktop/test11.jpeg", img)
#txt = gcp.getResult(path="/home/pi/Desktop/test5_1.jpeg")
az.azure_tts_rest(text=txt)
filename = "/home/pi/Desktop/_azure.mp3"'''
