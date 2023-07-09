import pandas as pd
from time import sleep
from tqdm import tqdm
from rag.query import query_doc

if __name__ == '__mainf__':
    df = pd.read_csv('sample_questions.csv')
    # print(df['Question'])

    # question = "नए पैन के लिए आवेदन करने के लिए कौन से दस्तावेज़ आवश्यक हैं?"
    # ans = query_doc(query=question)
    # print(ans)

    pred_answers = []

    for ques in tqdm(df['Question'], desc="Processing query: "):
        # print('\n',ques)
        answer = query_doc(query=ques)
        pred_answers.append(str(answer))
        sleep(10)

    new_df = {'Question' : df['Question'].to_list(), 
            'Ideal Answer' : df['Ideal Answer'].to_list(), 
            'Predicted Answers': pred_answers}
    
    new_df = pd.DataFrame(new_df)
    new_df.to_csv('final_result_3.csv', index=None)