import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = input_json, headers=Headers)
    if response.status_code ==400:
        return {'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None}

    emotions = json.loads(response.text)
    dict_emotion = emotions['emotionPredictions'][0]['emotion']
    
    dominant_emotion =""
    dominant_score =0
    for emotion_type,value in dict_emotion.items():
        
        if dominant_score < value:
            dominant_score= value
            dominant_emotion=emotion_type

        if emotion_type=='anger':
            anger_score = value
        elif emotion_type=='disgust':
            disgust_score = value
        elif emotion_type=='fear':
            fear_score = value
        elif emotion_type=='joy':
            joy_score = value
        elif emotion_type=='sadness':
            sadness_score = value

    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion}

def emotion_predictor(detected_text):
    if all(value is None for value in detected_text.values()):
        return detected_text
    if detected_text['emotionPredictions'] is not None:
        emotions = detected_text['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        max_emotion = max(emotions, key=emotions.get)
        #max_emotion_score = emotions[max_emotion]
        formated_dict_emotions = {
                                'anger': anger,
                                'disgust': disgust,
                                'fear': fear,
                                'joy': joy,
                                'sadness': sadness,
                                'dominant_emotion': max_emotion
                                }
        return formated_dict_emotions