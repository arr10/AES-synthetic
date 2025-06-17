
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import random
import os
from ruburics import get_ruburic, ANONYMIZATION
from prompts import get_prompt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate essays using LLM.')
    parser.add_argument('--model', type=str, default='meta-llama/Llama-3.3-70B-Instruct', help='Model name to use for generation')
    parser.add_argument('--n_essays', type=int, default=1000, help='Number of essays to generate')
    parser.add_argument('--set', type=int, default=1, help='Set to use for generation', choices=[1, 2, 3, 4, 5, 6, 7, 8])
    args = parser.parse_args()
    load_dotenv()

    openai = OpenAI(
        api_key=os.getenv("DEEPINFRA_API_KEY"),
        base_url="https://api.deepinfra.com/v1/openai",
    )
    model_name = args.model
    df = pd.read_csv(f'data/fold_0/sample_set{args.set}.tsv', sep='\t')
    df = df[df['essay_set'] == args.set]

    # create a output df
    output_df = pd.DataFrame(columns=['essay_set', 'essay', 'overall', 'org', 'wc', 'sf', 'conv', 'cont', 'pa', 'lang', 'narr', 'style', 'voice'])

    # iterate over the rows of the dataframe
    N_ESSAYS = args.n_essays

    for i in range(N_ESSAYS):
        messages = []
        row = df.sample(1).iloc[0]
        full_prompt = f'''Rephrase each sentence I will provide to you, but keep the meaning the same. Keep anonymization tags as they are.
        Example of anonymization tags: @CAPS, @LOCATION, @NAME. Answer only with the rephrased sentence.'''
        messages.append({"role": "user", "content": full_prompt})
        messages.append({"role": "assistant", "content": "Sure, I can help with that. Please provide the sentences you would like me to rephrase. From now on, I will only answer with the rephrased sentence you provide me."})
        # split the essay into sentences
        sentences = sent_tokenize(row['essay'])
        new_essay = ""
        for sentence in sentences:
            try:        
                chat_completion = openai.chat.completions.create(
                    model=model_name,
                    messages=messages + [{"role": "user", "content": sentence.strip() + '.'}],
                    top_p=0.9,
                )
                answer = chat_completion.choices[0].message.content
                new_essay += answer + ' '
            except Exception as e:
                print(e)
        row['essay'] = new_essay.strip()
        new_row_df = row
        output_df = pd.concat([output_df, new_row_df], ignore_index=True)
        if i % 100 == 0:
            print(f'Generated {i+1} essays so far. Out of {N_ESSAYS} essays to generate.')
        output_df.to_csv(f'data/fold_0/sample_llm_gptaug_set{args.set}.tsv', sep='\t', index=False)