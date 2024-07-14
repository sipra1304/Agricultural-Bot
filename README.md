# 🌾 Saarthi - AgroBot 🤖

Saarthi is an AI-powered agricultural chatbot designed to provide comprehensive and actionable advice to farmers. Leveraging Google Generative AI and LangChain, Saarthi can answer a variety of questions related to farming practices, crop management, market trends, and government schemes.

## ✨ Features
- 🌱 **Expert Agricultural Advice:** Provides detailed guidance on farming practices, pest control, crop management, and more.
- 🌾 **Custom Responses:** Tailors advice based on crop type, location, climate, and budget.
- 💸 **Government Schemes:** Informs about relevant government schemes and subsidies.
- 💬 **Conversational Interface:** Easy-to-use chatbot interface powered by Google Generative AI.

## 🚀 Getting Started

### 📋 Prerequisites
- 🐍 Python 3.6+
- 📦 Google AI Python SDK
- Required Python packages: `google-generativeai`, `langchain`, `streamlit`, `python-dotenv`

### 🛠 Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/saarthi-agrobot.git
   cd saarthi-agrobot
   ```

2. **Install the required packages.**

3. **Set up environment variables:**
   - Create a `.env` file in the project directory.
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

### 💻 Usage
1. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```
2. **Interact with the chatbot:**
   - Open the local Streamlit app in your browser.
   - Ask questions related to farming practices, crop management, market trends, and government schemes.

### 📚 Example Interaction
- **User:** "What are the best crops that I can grow with minimum investment in Odisha state of India?"
- **Saarthi:** "To give you the best recommendations, I need some more information: What's your location in Odisha? What is your access to irrigation? What's your farm size? Based on this information, I can suggest some low-investment crops that are well-suited to Odisha..."

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License
This project is licensed under the MIT License.

## 🙏 Acknowledgements
- [Google Generative AI](https://ai.google.dev/gemini-api/docs/get-started/python)
