# Data augmentation with LLM and Essay Scoring with T5 Models

This repository implements LLM based essay augmentation. This repository also implements an automatic essay scoring system using T5 transformer models, following the approach described in the Autoregressive Score Generation for Multi-trait Essay Scoring (ArTS) paper. 

## Requirements

- Python 3.7+
- PyTorch
- Transformers
- Datasets
- Pandas
- NumPy
- Matplotlib
- scikit-learn
- NLTK

## Data Format

The training, validation, and test data should be formatted as TSV files organized in fold directories:
```
data/
  fold_0/
    train.tsv
    dev.tsv
    test.tsv
  fold_1/
    ...
```

Each TSV file should contain columns for:
- `essay`: The essay text
- `essay_set`: The prompt set number
- Various trait scores: `voice`, `style`, `sf`, `wc`, `conv`, `org`, `narr`, `lang`, `pa`, `cont`, `overall`

## Usage

### Training

To train the model, use train.sh or run the training script directly:

```bash
python train.py --fold 0 --set 1 --folder data --batch_size 1 --model_name t5-base
```

### Parameters

- `--fold`: Cross-validation fold number (default: 0)
- `--set`: Essay set number to train on (default: 1)
- `--folder`: Data directory path (default: 'data')
- `--batch_size`: Batch size for training (default: 1)
- `--model_name`: T5 model size - options include:
  - `t5-small`: 60M parameters
  - `t5-base`: 220M parameters (default)
  - `t5-large`: 770M parameters
  - `t5-3b`: 3B parameters
  - `t5-11b`: 11B parameters

## Model Output

The model generates a string with all scores in the format:
```
Voice: X, Style: X, Sentence Fluency: X, Word Choice: X, Conventions: X, Organization: X, Narrativity: X, Language: X, Prompt Adherence: X, Content: X, Overall: X
```

## Evaluation

The model is evaluated using Quadratic Weighted Kappa (QWK) for each trait. Results are saved to:
```
{folder}/fold_{fold}/results_final_{set}.txt
```

## Example Command

```bash
python train.py --fold 0 --set 2 --batch_size 4 --model_name t5-base --folder data_incontext
```

This command will train a T5-base model on essay set 2 using fold 0 with a batch size of 4, and will use data from the data_incontext folder.