# Information Retrieval from Knowledge Document with LLM

Try DEMO here: https://geeythree-ragbot.streamlit.app/ 

Chatbot to perform question-answer based on knowledge document 


## Avilable features:
1. Multilingual querying 
2. Results Evaluation 
3. Query with audio (microphone) and get back response in audio format  

PS:
1. Currently multilingual querying is not supported for Indian languages.
2. When using audio, only English language is supported as of now.

## Install dependencies
Please create a new virtual environment and install the dependencies from the requirements file. 
```
pip install -r requirements.txt
```
If you want to run the main.py, you will aditionally require to install PyAudio.
Refer this document to install PyAudio https://people.csail.mit.edu/hubert/pyaudio/

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
python run_all.py
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