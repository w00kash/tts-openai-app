
# Text-to-Speech OpenAI Demo App

Simple Python app to demonstrate use of OpenAI Text-to-Speech capabilities with Web UI using Streamlit


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file or pass it when running Docker container

`OPENAI_API_KEY`

Optionaly you use different TTS model (***`tts-1`*** or ***`tts-1-hd`***) - (default: *`tts-1`*)

`OPENAI_TTS_MODEL`


## Run Locally

Clone the project

```bash
git clone https://github.com/w00kash/tts-openai-app.git
```

Go to the project directory

```bash
cd tts-openai-app/
```

Build Docker Image

```bash
docker build -t tts-openai-app .
```

Start as Docker container

```bash
docker run -it -d --name tts-openai-app \
-p 8080:8501 \
-v ./media:/app/media/ \
-e OPENAI_API_KEY="{your_openai_api_key}" tts-openai-app
```

## Tech Stack

- Python
- OpenAI API
- Streamlit
- Docker


## Licence

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

