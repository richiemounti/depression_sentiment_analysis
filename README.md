# How to install the sentiment analysis project

# Installation and Setup
Clone the repository.
```
https://github.com/richiemounti/depression_sentiment_analysis.git

```

## Create a virtual environment
```
python3 -m venv venv;
```

If you need to set up install virtualenv:
 ```bash
        #linux
        virtualenv venv
   ```
    
   ```bash
        #windows
        python -m virtualenv venv
   `````

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```bash
        #linux
        source venv/bin/activate
   ```
  
   ```bash
        #windows
        venv/Scripts/activate
    ```
## Install requirements
```
pip install -r requirements.txt
```
# Running the files

1. Run the Download_twitter_Api.py

```
python3 Download_twitter_Api.py
```

2. Once step  1 is done run preprocessor.py

```
python3 preprocessor.py
```

3. After step 2 is done run depression_sentiment_analysis.py

```
python3 depression_sentiment_analysis.py
```

4. You can test the project live by typing a tweet after running InsertTweetDemo.py

```
python3 InsertTweetDemo.py

```
