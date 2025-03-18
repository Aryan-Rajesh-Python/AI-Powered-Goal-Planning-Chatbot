# AI-Powered Goal Planning Chatbot

## 📌 Overview
This is an **AI-powered goal-setting chatbot** that helps users define, track, and manage their goals efficiently. Built using **Google Gemini API, LangChain, and PostgreSQL**, it ensures structured goal planning with AI-driven responses and persistent storage.

## 🚀 Features
✅ **Conversational AI** – Uses Gemini API to guide users in goal setting.  
✅ **Task Management** – Users assign weightages to goals (must sum to 100%).  
✅ **Memory** – Chatbot remembers previous interactions.  
✅ **Database Storage** – PostgreSQL stores user goals persistently.  
✅ **General Queries** – Chatbot can answer general knowledge queries (e.g., movie summaries).  

## 🛠️ Tech Stack
- **Python** – Main programming language
- **Google Gemini API** – AI-powered chatbot
- **LangChain** – Implements conversation memory
- **PostgreSQL** – Stores user goals
- **psycopg2** – Connects Python to PostgreSQL
- **dotenv** – Manages API keys securely

## 📂 Project Structure
```
zeeproc_chatbot/
│── chatbot.py         # Main chatbot script
│── database.py        # PostgreSQL connection script
│── .env               # Stores API keys (DO NOT SHARE)
│── requirements.txt   # List of dependencies
│── README.md          # Project documentation
```

## 🛠️ Setup Instructions
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **2️⃣ Set Up PostgreSQL**
- Create a database `zeeproc_chatbot` in PostgreSQL.
- Run the following SQL command to create the `user_goals` table:
  ```sql
  CREATE TABLE user_goals (
      id SERIAL PRIMARY KEY,
      user_id TEXT NOT NULL,
      goal TEXT NOT NULL,
      weightage INT NOT NULL CHECK (weightage BETWEEN 1 AND 100),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  ```

### **3️⃣ Set Up API Keys**
- Create a `.env` file in the project folder.
- Add your **Google Gemini API key**:
  ```
  GEMINI_API_KEY=your_api_key_here
  ```

### **4️⃣ Run the Chatbot**
```bash
python chatbot.py
```

## 🎯 Usage
1️⃣ **Enter your User ID**  
2️⃣ **Add goals and assign weightages** (must sum to 100%)  
3️⃣ **Chatbot stores goals in PostgreSQL**  
4️⃣ **Chatbot remembers previous conversations**  
5️⃣ **You can ask general questions too!**  

## 📌 Future Improvements
- ✅ **Fetch stored goals** when a user returns.
- ✅ **Dynamic Schema Handling** for different types of data storage.
- ✅ **Advanced AI responses** using fine-tuned models.

## 📞 Contact
For any queries, reach out to **aryanreddy463@gmail.com**.

🚀 **Built with AI to help users achieve their goals efficiently!**
