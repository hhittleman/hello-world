import json
from watson_developer_cloud import VisualRecognitionV3

# Create an instance of your Watson Visual Recognition service
instance = VisualRecognitionV3(version='2016-05-20', api_key='9c4d1a53d18b540067565c3e78f04d03de71f9c2')

# Classify the image using Watson Visual Recognition
img = instance.classify(images_url='https://s-media-cache-ak0.pinimg.com/originals/c6/ae/95/c6ae950df86879b7e463d502b483d6b7.png')

# Print the JSON results
#print(json.dumps(img, indent=2))

# Format the results to be more readable
for results in img['images'][0]['classifiers'][0]['classes']:
    print('\n There is a ' + str(round((results['score']*100),1)) + ' percent chance the image contains: '+ results['class'])
