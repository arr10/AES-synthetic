from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import random
import os
from ruburics import get_ruburic, ANONYMIZATION
from prompts import get_prompt
import argparse

def create_prompt(row, args, df, type_of_prompt='improve'):
    full_prompt = f'''Currently, my essay got the following scores:'''
    scores_dict = {}
    if args.set == 1 or args.set == 2:
        overall, org, wc, sf, conv, cont = row['overall'], row['org'], row['wc'], row['sf'], row['conv'], row['cont']
        full_prompt += f'overall: {overall} out of 12, organization: {org} out of 6, word choice: {wc} out of 6, sentence fluency: {sf} out of 6, conventions: {conv} out of 6, content: {cont} out of 6.'
        scores_dict.update({'overall': overall, 'org': org, 'wc': wc, 'sf': sf, 'conv': conv, 'cont': cont})
    elif args.set in [3, 4, 5, 6]:
        overall, narr, lang, pa, cont = row['overall'], row['narr'], row['lang'], row['pa'], row['cont']
        full_prompt += f'overall: {overall} out of 3, narrative: {narr} out of 3, language: {lang} out of 3, persuasive appeals: {pa} out of 3, content: {cont} out of 3.'
        scores_dict.update({'overall': overall, 'narr': narr, 'lang': lang, 'pa': pa, 'cont': cont})
    elif args.set == 7:
        overall, narr, lang, style, voice = row['overall'], row['narr'], row['lang'], row['style'], row['voice']
        full_prompt += f'overall: {overall} out of 30, narrative: {narr} out of 3, language: {lang} out of 3, style: {style} out of 3, voice: {voice} out of 3.'
        scores_dict.update({'overall': overall, 'narr': narr, 'lang': lang, 'style': style, 'voice': voice})
    elif args.set == 8:
        overall, cont, org, wc, sf, conv, voice = row['overall'], row['cont'], row['org'], row['wc'], row['sf'], row['conv'], row['voice']
        full_prompt += f'''overall: {overall} out of 60, content: {cont} out of 6, organization: {org} out of 6, word choice: {wc} out of 6, sentence fluency: {sf} out of 6, conventions: {conv} out of 6, voice: {voice} out of 6.'''
        scores_dict.update({'overall': overall, 'cont': cont, 'org': org, 'wc': wc, 'sf': sf, 'conv': conv, 'voice': voice})
    else:
        raise ValueError("Invalid essay set. Please choose a set between 1 and 8.")
    full_prompt += f"\nRubric:\n"
    full_prompt += "".join(get_ruburic(args.set)[0])
    full_prompt += ANONYMIZATION
    full_prompt += f"\nEssay Prompt given to me:\n"
    full_prompt += get_prompt(args.set)
    if type_of_prompt == 'improve':
        full_prompt += '''Improve the essay to get improved score by exactly 1 point in each category.'''
    else:
        full_prompt += '''For demonstration purposes, make essay to be worse by exactly 1 point in each rubric category.'''
    full_prompt += f'''Before essay and after essay use <START> and <END> tags to mark the start and end of the essay.
    My current essay is:
    <START>
    {row['essay']}
    <END>
        '''

    return full_prompt, scores_dict



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
        type_of_prompt = random.choice(['improve', 'worsen'])
        full_prompt, scores_dict = create_prompt(row, args, df, type_of_prompt)
        messages.append({"role": "user", "content": full_prompt})
        try:        
            chat_completion = openai.chat.completions.create(
                model=model_name,
                messages=messages,
                top_p=0.9,
            )
            answer = chat_completion.choices[0].message.content
            # make answer to be only from <Start> to <End>, case insensitive
            start_index = answer.lower().find('<start>')
            end_index = answer.lower().find('<end>')
            if start_index != -1 and end_index != -1:
                answer = answer[start_index + len('<start>'):end_index].strip()
            # if not found, keep answer as is

        except Exception as e:
            print(e)
        new_row_df = pd.DataFrame([{
        'essay_set': row['essay_set'],
        'essay':      answer
        }]) 
        for key, value in scores_dict.items():
            new_row_df[key] = value
        output_df = pd.concat([output_df, new_row_df], ignore_index=True)
        if i % 100 == 0:
            print(f'Generated {i+1} essays so far. Out of {N_ESSAYS} essays to generate.')
        output_df.to_csv(f'data/fold_0/sample_llm_aug1_set{args.set}.tsv', sep='\t', index=False)
