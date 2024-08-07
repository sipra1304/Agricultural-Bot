# 🌾 Saarthi - AgroBot 🤖

**[Chat with Saarthi](https://huggingface.co/spaces/Sipra1304/AgrobotSaarthi)**

Saarthi is an AI-powered agricultural chatbot designed to provide comprehensive and actionable advice to farmers. Leveraging Google Generative AI, Saarthi can answer a variety of questions related to farming practices, crop management, market trends, and government schemes.

## ✨ Features
- 🌱 **Expert Agricultural Advice:** Provides detailed guidance on farming practices, pest control, crop management, and more.
- 🌾 **Custom Responses:** Tailors advice based on crop type, location, climate, and budget.
- 💸 **Government Schemes:** Informs about relevant government schemes and subsidies.
- 💬 **Conversational Interface:** Easy-to-use chatbot interface powered by Google Generative AI.

## 🚀 Getting Started

### 📋 Prerequisites
- 🐍 Python 3.6+
- 📦 Google AI Python SDK
- Required Python packages: `google-generativeai`, `streamlit`, `python-dotenv`

### 🛠 Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/saarthi-agrobot.git
   cd saarthi-agrobot
   ```

2. **Install the required packages.**
   ```sh
   pip install -r requirements.txt
   ```

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

### 🌐 Hosting on Streamlit
You can also host Saarthi on Streamlit Cloud to make it accessible to others. Here are the steps to deploy on Streamlit:

1. **Sign up or log in to [Streamlit](https://streamlit.io/)**
2. **Create a new app:**
   - Connect your GitHub repository to Streamlit.
   - Select the repository and the branch you want to deploy.
   - Set `app.py` as the entry point.
3. **Set up environment variables:**
   - Add `GOOGLE_API_KEY` in the Streamlit app settings.
4. **Deploy the app:**
   - Click on "Deploy" and your app will be live!

### 📷 Sample Screenshots
Here are some screenshots of the Saarthi interface:

![Screenshot 2024-07-15 124047](https://github.com/user-attachments/assets/ea8a8333-5832-453c-9ee5-f55b8180d533)


![Screenshot 2024-07-15 123811](https://github.com/user-attachments/assets/9916a730-84e6-4f8d-baa8-4470cc9c40f5)

### 📚 Example Interaction
- **User:** "What are the best crops that I can grow with minimum investment in Odisha state of India?"
- **Saarthi:** "To give you the best recommendations, I need some more information: What's your location in Odisha? What is your access to irrigation? What's your farm size? Based on this information, I can suggest some low-investment crops that are well-suited to Odisha..."

## 🤝 Contributors
![@sipra1304](https://github.com/sipra1304) ![@beura-chirantan](https://github.com/beura-chirantan)

## 📄 License
This project is licensed under the MIT License.

## 🙏 Acknowledgements
- [Google Generative AI](https://ai.google.dev/gemini-api/docs/get-started/python)
