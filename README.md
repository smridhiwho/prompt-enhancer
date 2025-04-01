# Prompt Enhancer

A Streamlit application that enhances your prompts using the Google Gemini API and advanced prompt engineering techniques.

## Features

- Clean and intuitive user interface
- One free enhancement per day
- Advanced prompt engineering techniques
- Real-time prompt enhancement
- No login required
- Powered by Google's Gemini 1.5 Pro model
- Support the project for unlimited daily enhancements

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/prompt-enhancer.git
   cd prompt-enhancer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file and add your Google API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - You can get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Running the Application

To run the application, execute:
```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Enter your prompt in the left text area
2. Click the "Enhance Prompt" button
3. View your enhanced prompt in the right text area
4. Note: Free users are limited to one enhancement per day

## Premium Features

Want unlimited daily enhancements? Support the project by buying me a coffee! Your support helps maintain and improve the application.

[Buy Me a Coffee](https://www.buymeacoffee.com/yourusername)

## Development

### Project Structure
```
prompt-enhancer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Note

You'll need to obtain a Google API key to use this application. The API key should be kept secure and never shared publicly. The free tier of Google's API has generous limits for personal use. 