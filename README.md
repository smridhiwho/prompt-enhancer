# Prompt Enhancer Pro

A Streamlit application that enhances user prompts using AI and prompt engineering best practices. Each user is allowed to enhance their prompts twice.

## Features

- AI-powered prompt enhancement
- Two enhancements per user
- Google Ads integration
- User usage tracking
- Modern, responsive UI

## Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd prompt-enhancer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your Google Ads client ID

5. Run the application:
```bash
streamlit run main.py
```

## Deployment

### Option 1: Streamlit Community Cloud (Recommended)

1. Create a GitHub repository and push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account

3. Click "New app" and select your repository

4. Set up your environment variables in Streamlit Cloud:
   - Go to your app's settings
   - Add the following secrets:
     ```toml
     DEEPSEEK_API_KEY = "your-deepseek-api-key"
     HUGGINGFACE_API_KEY = "your-huggingface-api-key"
     GOOGLE_ADS_CLIENT_ID = "your-google-ads-client-id"
     ```

5. Deploy your app!

### Option 2: Heroku

1. Create a `Procfile`:
```
web: streamlit run main.py
```

2. Create a `runtime.txt`:
```
python-3.9.18
```

3. Deploy using Heroku CLI:
```bash
heroku create your-app-name
git push heroku main
```

4. Set up environment variables in Heroku:
```bash
heroku config:set DEEPSEEK_API_KEY=your-deepseek-api-key
heroku config:set HUGGINGFACE_API_KEY=your-huggingface-api-key
heroku config:set GOOGLE_ADS_CLIENT_ID=your-google-ads-client-id
```

### Option 3: Docker

1. Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Build and run:
```bash
docker build -t prompt-enhancer .
docker run -p 8501:8501 prompt-enhancer
```

## Environment Variables

- `DEEPSEEK_API_KEY`: Your Deepseek API key
- `HUGGINGFACE_API_KEY`: Your HuggingFace API key
- `GOOGLE_ADS_CLIENT_ID`: Your Google Ads client ID

## Usage

1. Enter your prompt in the text area
2. Click "Enhance Prompt"
3. Each user is allowed to enhance their prompts twice
4. The remaining number of enhancements will be displayed after each use

## Monetization

The application is monetized through:
- Google Ads integration
- Premium features (coming soon)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 