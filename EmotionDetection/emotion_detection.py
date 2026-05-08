import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes text and returns formatted emotion scores and the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    # Task 3: Format output kepada dictionary
    formatted_response = json.loads(response.text)
    
    # Ekstrak set emosi
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Cari emosi dominan (skor paling tinggi)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Pulangkan format yang diminta
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }