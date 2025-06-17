from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import os
from ruburics import get_ruburic, ANONYMIZATION
from prompts import get_prompt
from argparse import ArgumentParser
load_dotenv()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--set', type=int, default=1, help='Essay set to evaluate')
    args = parser.parse_args()
    openai = OpenAI(
        api_key=os.getenv("DEEPINFRA_API_KEY"),
        base_url="https://api.deepinfra.com/v1/openai",
    )

    model_name = "meta-llama/Llama-3.3-70B-Instruct"

    # Load the TSV file into a pandas DataFrame
    df = pd.read_csv('data/fold_0/test.tsv', delimiter='\t')
    set = args.set
    num_rubrics = len(get_ruburic(set)[1])
    df = df[df['essay_set']==set]

    try:    
        df_temp = pd.read_csv(f'data/fold_0/test_ans_set{set}.tsv', sep='\t')
    except:
        df_temp = pd.DataFrame(columns = df.columns)
        df_temp.to_csv(f'data/fold_0/test_ans_set{set}.tsv', sep='\t', index=False)

    def create_prompt(row):
        a, b = get_ruburic(set)
        full_prompt = f'''
    You are a jury in an essay competition. Given a prompt, student's essay and grading rubric for an essay, give a score for each rubric and an overall score for the essay. Give it in the format:
    {(', '.join([f"{k}: int" for k in b]))}
    Give nothing, just the scores in the format above, without any explanation or additional text.
        '''
        full_prompt += ANONYMIZATION
        full_prompt += f"\nPrompt:\n"
        full_prompt += get_prompt(row['essay_set'])
        full_prompt += f"\n\nRubrics:"
        for rubric_num in range(0, num_rubrics):
            full_prompt += a[rubric_num]
        full_prompt += f"\nEssay:\n"
        full_prompt += row['essay']

        return full_prompt

    def make_message(row):
        try:
            prompt = create_prompt(row)
            messages = [
                {"role": "user", "content": prompt},
            ]
            chat_completion = openai.chat.completions.create(
                model=model_name,
                messages=messages,
            )
            row[f'llm_answer'] = chat_completion.choices[0].message.content
            for rubric_num in range(0, num_rubrics):
                rubric_name = get_ruburic(set)[1][rubric_num]
                row[f'LLM_{rubric_name}'] = int(row[f'llm_answer'].split(',')[rubric_num].split(':')[1].strip())
        except Exception as e:
            print(e)
        # save the row
        df_temp = pd.read_csv(f'data/fold_0/test_ans_set{set}.tsv', sep='\t')
        df_temp = pd.concat([df_temp, pd.DataFrame([row])], ignore_index=True)
        df_temp.to_csv(f'data/fold_0/test_ans_set{set}.tsv', sep='\t', index=False)
        return row

    df = df.apply(make_message, axis=1)
    df.to_csv(f'data/fold_0/test_final_ans_set{set}.tsv', sep='\t', index=False)
    df.head()