import os
import argparse
import people_also_ask
import pandas as pd

ROOT = os.path.dirname(__file__)

def get_qnas(prompt):
    questions = people_also_ask.get_related_questions(prompt, 5)
    qnas = {}
    for q in questions:
        qnas[q] = people_also_ask.get_simple_answer(q)
    
    return qnas

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Fetches the questions and answers from People Also Ask section.'
    )

    parser.add_argument(
        '-p',
        '--prompt',
        required=True,
        help='Your search term'
    )

    args = parser.parse_args()

    qnas = get_qnas(args.prompt)
    
    df = pd.DataFrame.from_dict(qnas, orient='index', columns=['Answers'])
    df.index.name = 'Questions'

    print(df.head())

    df.to_csv(os.path.join(ROOT, f'{args.prompt} - PAA.csv'))

