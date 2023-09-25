from db import QASystem
import pandas as pd
import csv

def chatbot(input):
    qa = QASystem('test.csv')
    try:
        qa_response = qa.get_response(input)
        print("Try")
    except:
        qa_response = "I don't have the necessary information to answer; you must train me more"
        df = pd.DataFram([[]])
        # df = pd.DataFrame([['"' + input + '"', '"' + reply + '"']], columns=['Questions'])
        # df.to_csv('bank.csv', mode='a', header=False, index=False)

    return qa_response