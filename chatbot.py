import os
import psycopg2
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Model
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model

# PostgreSQL connection parameters
DB_NAME = "zeeproc_chatbot"
DB_USER = "postgres"
DB_PASSWORD = "aryan"  # Replace with your PostgreSQL password
DB_HOST = "localhost"
DB_PORT = "5432"

# Initialize conversation memory
memory = ConversationBufferMemory(return_messages=True)

def connect_db():
    """Establishes a connection to PostgreSQL and returns the connection object."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None

def ask_gemini(question):
    """Uses Gemini API to generate responses while incorporating memory."""
    memory_input = memory.load_memory_variables({})
    chat_history = memory_input["history"] if "history" in memory_input else ""
    full_prompt = f"Chat History:\n{chat_history}\n\nUser: {question}\nAI:"
    
    response = model.generate_content([full_prompt])
    memory.save_context({"input": question}, {"output": response.text.strip()})
    return response.text.strip()

def collect_user_goals(user_id):
    """Chatbot collects user goals and ensures weightage sums to 100%."""
    print("\n📝 Chatbot: Let's set up your goals. Each goal must have a weightage, and the total should sum to 100%.\n")

    user_goals = []
    total_weightage = 0

    while total_weightage < 100:
        goal = input("🤖 Enter your goal (or type 'done' to finish): ").strip()
        if goal.lower() == "done":
            break

        try:
            weightage = int(input(f"📊 Assign a weightage to '{goal}' (remaining {100 - total_weightage}%): ").strip())
            if weightage < 1 or weightage > (100 - total_weightage):
                print("❌ Invalid weightage. Try again.")
                continue
        except ValueError:
            print("❌ Please enter a valid number for weightage.")
            continue

        user_goals.append((user_id, goal, weightage))
        total_weightage += weightage

    if total_weightage != 100:
        print("\n❌ Total weightage must be exactly 100%. Restarting...\n")
        return collect_user_goals(user_id)

    return user_goals

def store_goals_in_db(user_id, goals):
    """Stores collected user goals into PostgreSQL."""
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor()
    for goal in goals:
        cursor.execute(
            "INSERT INTO user_goals (user_id, goal, weightage) VALUES (%s, %s, %s)",
            (user_id, goal[1], goal[2])
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("\n✅ Goals successfully stored in the database!")

def chatbot_loop():
    """Main chatbot loop with memory for user interaction."""
    user_id = input("\n🆔 Enter your User ID: ").strip()
    print("\n🤖 Chatbot:", ask_gemini("Introduce yourself as a smart AI goal planner."))

    goals = collect_user_goals(user_id)
    store_goals_in_db(user_id, goals)

    print("\n💬 Chatbot: Here’s a summary of your goals:")
    for goal in goals:
        print(f"📌 {goal[1]} → {goal[2]}%")

    summary = ask_gemini(f"Summarize these user goals: {goals}")
    print("\n🤖 Chatbot Summary:", summary)

    # Keep the chatbot running to remember previous conversations
    while True:
        user_input = input("\n💬 You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\n🤖 Chatbot: Goodbye! See you soon. 👋")
            break

        response = ask_gemini(user_input)
        print("\n🤖 Chatbot:", response)

if __name__ == "__main__":
    chatbot_loop()