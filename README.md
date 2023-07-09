# Information Retrieval from Knowledge Document with LLM

Chatbot to perform question-answer based on knowledge document 

## Avilable features:
1. Multilingual querying 
2. Results Evaluation 
3. Query with audio (microphone) and get back response in audio format  (PS: multilingual querying not supported)

## Running the chatbot script
```
python main.py
```

## Running the program on sample question
1. Create a persistent vector database by running the following script.
<br>
PS: Replace the rag/knowledge_document.txt to use a different knowledge document.
```
python rag/vectorise_data.py
```

2. QA can be performed on a list of questions using the script main.py
<br>
PS: Update the sample_question.csv to create a new list of questions, or create a new sheet with questions and ideal answers (if evaluation is required).
```
python main.py
```

3. Evalution can be performed using multiple evalutaion methods such as Bi-Encoder, Semantic Similarity, and ContextQAEval. Run this script:
```
python eval.py
``` 
## Performace Metrics:
1. Average Bi-encoder Score: 49.9%
2. Average Semantic Similarity Score: 66.5%
3. Overall Accuracy: 91.2%

Additional requirements to run the audio script:
```
pipwin install pyaudio
```