# AUDIO KEY WORD EXTRACTOR

### ENVIRONMENT SETUP
```bash
conda create -p ./env -y
conda activate ./env
pip install -r requirements.txt
```

### TO RUN THE APP
```python
python src/app.py
```

### AUDIO PROCESSING
```mermaid
graph TD;
    AUDIO_FILE_UPLOADED-->AUDIO_FILE_INTO_CHUNCKS-->AUDIO_TO_TEXT-->KEYWORDS;
```
