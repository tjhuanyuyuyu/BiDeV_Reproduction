# BiDeV_Reproduction
## This is a simple reproduction of the BiDeV method. If there are any deficiencies, please feel free to give me your advice.


### How to Run

```bash
pip install -r requirements.txt
```

Apply for a LLM api key and fill in .env


Use the following command to run the script:

```bash
python eval.py [--data DATA_FILE] [--wiki WIKI_FILE] [--mode MODE] [--n_iter N]
```



### Arguments

| Argument   | Type   | Default                     | Description                                                                           |
| ---------- | ------ | --------------------------- | ------------------------------------------------------------------------------------- |
| `--data`   | string | `sample3_100.json`          | Filename of the input dataset (located inside the `data/` folder)                     |
| `--wiki`   | string | `hover_evidence_corpus.txt` | Filename of the evidence corpus (located inside the `data/` folder)                   |
| `--mode`   | string | `gold`                      | Mode of evidence usage: `gold` (use provided evidence) or `open` (use retrieval only) |
| `--n_iter` | int    | `3`                         | Number of BiDeV percept-rewrite iterations                                                  |

**Note**: Do not include the `data/` prefix in file names. The script automatically assumes all files are under the `data/` directory.


### Output

For each claim, the script prints:

* The claim, questions, answers, rewrite claims, sub_clams, checker's results.
* The predicted label
* The ground-truth label

At the end, an overall accuracy summary is shown.





