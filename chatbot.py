import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "1bf0d6a0-af00-11e9-bfc4-13e5395c821e5e0a08df-744c-4040-94ea-db2672eac83f"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
        
def answer_questions():
    question = input (">")
    answer =classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    
    if confidence < 75:
        print("I don't know, please ask me another question!")
    elif answerclass == "Attractions":
        print("The best attractions in Edmonton are the WEM and the Muttart Conserveratory")
    elif answerclass == "Weather":
        print("The weather in Edmonton is sorta cold, around 20C in the summer and -15C in the winter")
    elif answerclass == "Food":
        print("The best food to eat in Edmonton is waffles with maple syrup :)")
print("What do you want to know about Edmonton")
while True:
    answer_questions()
        