from regex import F
from transformers import T5TokenizerFast, T5ForConditionalGeneration, Seq2SeqTrainer, Seq2SeqTrainingArguments, DataCollatorForSeq2Seq, EarlyStoppingCallback, TrainerCallback
from datasets import Dataset
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import cohen_kappa_score, max_error
import nltk
nltk.download('punkt')
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fold', type=int, default=0)
    parser.add_argument('--set', type=int, default=1)
    parser.add_argument('--folder', type=str, default='data')
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--model_name', type=str, default='t5-base', choices=['t5-base', 't5-small', 't5-large', 't5-3b', 't5-11b'], 
                        help='model name, choose from t5-small, t5-base, t5-large, t5-3b, t5-11b')

    return parser.parse_args()

def extract_scores(sentence):
    num_scores = 11
    try: 
        scores = [(s.split(': ')[1]) for s in sentence.split(', ')]
    except:
        print("Failed to extract scores from this sentence:", sentence)
        print("------------------------------------------------------")
        return [-100] * num_scores
    # Verify that the sentence has the correct number of scores
    if len(scores) < num_scores:
        print("Not enought scores from this sentence:", sentence)
        print("------------------------------------------------------")
        scores += ['nan'] * (num_scores - len(scores))
    elif len(scores) > num_scores:
        print("Too many scores from this sentence:", sentence)
        print("------------------------------------------------------")
        scores = scores[:num_scores]

    # convert scores to integers
    for i, s in enumerate(scores):
        if s == 'nan' or s == 'Nan' or s == 'None':
            scores[i] = -100
        # check if s is a number
        else:
            try:
                scores[i] = int(s)
            except:
                # means T5 failed to predict the score
                scores[i] = -100
    
    return scores

    
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    # print(predictions, labels)
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    predictions = np.where(predictions != -100, predictions, tokenizer.pad_token_id)
    # print(predictions, labels)
    # print(f"  ▶ pred id range = [{predictions.min()}, {predictions.max()}], vocab_size = {tokenizer.vocab_size}")

    # print("predictions shape: ", predictions.shape, "dtype: ", predictions.dtype)
    # print("labels shape: ", labels.shape, "dtype: ", labels.dtype)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    prediction_scores = np.array([extract_scores(pred) for pred in decoded_preds], dtype=int)
    label_scores = np.array([extract_scores(label) for label in decoded_labels], dtype=int)

    val_scores = [cohen_kappa_score(label, pred, weights='quadratic') for label, pred in zip(label_scores.T, prediction_scores.T)]
    # val_scores = [(label, pred) for label, pred in zip(label_scores.T, prediction_scores.T)]
    val_scores = [s if not np.isnan(s) else "NA" for s in val_scores]
    return {"QWK_voice": val_scores[0], 
            "QWK_style": val_scores[1], 
            "QWK_sf": val_scores[2], 
            "QWK_wc": val_scores[3], 
            "QWK_conv": val_scores[4], 
            "QWK_org": val_scores[5], 
            "QWK_narr": val_scores[6],
            "QWK_lang": val_scores[7],
            "QWK_pa": val_scores[8],
            "QWK_cont": val_scores[9],
            "QWK_overall": val_scores[10]} 

def preprocess_function(examples, tokenizer):
    ''' 
    Tokenize the inputs and labels, adding a prefix to the essay. 
        Returns {input_ids: Tensor, attention_mask: Tensor, labels: Tensor}
    '''
    task_prefix = f"score the essay of the prompt "
    inputs = [task_prefix + str(essay_set) + essay for essay, essay_set in zip(examples['essay'], examples['essay_set'])]
    model_inputs = tokenizer(inputs, return_tensors='pt', padding=True, truncation=True, max_length=1024)

    labels = [f"Voice: {voice}, Style: {style}, Sentence Fluency: {sf}, Word Choice: {wc}, Conventions: {conv}, Organization: {org}, Narrativity: {narr}, Language: {lang}, Prompt Adherence: {pa}, Content: {cont}, Overall: {overall}" for voice, style, sf, wc, conv, org, narr, lang, pa, cont, overall in zip(examples['voice'], examples['style'], examples['sf'], examples['wc'], examples['conv'], examples['org'], examples['narr'], examples['lang'], examples['pa'], examples['cont'], examples['overall'])]
    # for now only include sf, wc, conv, org, cont, overall
    # labels = [f"Sentence Fluency: {sf}, Word Choice: {wc}, Conventions: {conv}, Organization: {org}, Content: {cont}, Overall: {overall}" for sf, wc, conv, org, cont, overall in zip(examples['sf'], examples['wc'], examples['conv'], examples['org'], examples['cont'], examples['overall'])]
    tokenized_labels = tokenizer(labels, return_tensors='pt', padding=True, truncation=True, max_length=128)['input_ids']
    
    model_inputs['labels'] = tokenized_labels

    return model_inputs


if __name__ == "__main__":
    args = parse_args()
    fold = args.fold
    set = args.set
    folder = args.folder
    batch_size = args.batch_size
    model_name = f'google-t5/{args.model_name}'

    df_train = pd.read_csv(f'{folder}/fold_{fold}/train.tsv', delimiter='\t')
    df_val = pd.read_csv(f'{folder}/fold_{fold}/dev.tsv', delimiter='\t')
    df_test = pd.read_csv(f'{folder}/fold_{fold}/test.tsv', delimiter='\t')

    drop_columns = ['DK_1', 'DK_2', 'DK_3', 'Prompt Adherence', "Language", "Narrativity", "essay_id", 'Essay ID', 'Content', 'split']
    df_train = df_train[df_train['essay_set'] == set].fillna(-100).drop(columns=drop_columns)
    df_val = df_val[df_val['essay_set'] == set].fillna(-100).drop(columns=drop_columns)
    df_test = df_test[df_test['essay_set'] == set].fillna(-100).drop(columns=drop_columns)
    df_train[['overall', 'org', 'wc', 'sf', 'conv', 'pa', 'lang', 'narr', 'style', 'voice']] = df_train[['overall', 'org', 'wc', 'sf', 'conv', 'pa', 'lang', 'narr', 'style', 'voice']].astype(int)
    df_val[['overall', 'org', 'wc', 'sf', 'conv', 'pa', 'lang', 'narr', 'style', 'voice']] = df_val[['overall', 'org', 'wc', 'sf', 'conv', 'pa', 'lang', 'narr', 'style', 'voice']].astype(int)
    df_test[['overall', 'org', 'wc', 'sf', 'conv', 'pa', 'lang', 'narr', 'style', 'voice']] = df_test[['overall', 'org', 'wc', 'sf', 'conv', 'pa', 'lang', 'narr', 'style', 'voice']].astype(int)

    train_cols_to_remove = df_train.columns.tolist()
    val_cols_to_remove = df_val.columns.tolist()
    test_cols_to_remove = df_test.columns.tolist()
    tokenizer = T5TokenizerFast.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    train_dataset = Dataset.from_pandas(df_train).map(
        lambda x: preprocess_function(x, tokenizer), batched=True,
        remove_columns = train_cols_to_remove
        )
    val_dataset = Dataset.from_pandas(df_val).map(
        lambda x: preprocess_function(x, tokenizer), batched=True,
        remove_columns = val_cols_to_remove
        )
    test_dataset = Dataset.from_pandas(df_test).map(
        lambda x: preprocess_function(x, tokenizer), batched=True,
        remove_columns = test_cols_to_remove
        )

    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, padding=True)
    # add a gpu empty cache callback
    class ClearChacheCallback(TrainerCallback):
        def on_step_end(self, args, state, control, **kwargs):
            torch.cuda.empty_cache()
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2), ClearChacheCallback()]
    

    args = Seq2SeqTrainingArguments(
        f"{model_name}-finetuned-essay-scoring",
        eval_steps=5000,
        learning_rate=2e-5,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        weight_decay=0.01,
        save_total_limit=3,
        num_train_epochs=15,
        predict_with_generate=True,
        fp16=True,
    )

    trainer = Seq2SeqTrainer(
        model,
        args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        data_collator=data_collator,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )

    trainer.train()

    # Evaluate the model with the test dataset
    val_results = trainer.evaluate(max_length=128)
    results = trainer.evaluate(test_dataset, max_length=128)

    print(val_results)
    print(results)

    try:
        with open(f'{folder}/fold_{fold}/results_final_{set}.txt', 'w') as f:
            f.write(f"Results for validation set:\n")
            for key, value in val_results.items():
                f.write(f"{key}: {value}\n")
            f.write(f"\nResults for test set:\n")
            for key, value in results.items():
                f.write(f"{key}: {value}\n")
    except:
        print("Could not write results to file")