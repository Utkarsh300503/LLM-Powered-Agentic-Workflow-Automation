import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from tools.search_tool import search_web
from tools.summarizer_tool import summarize_text
from tools.save_tool import save_report

# ── API Key ────────────────────────────────────────────
# Set your OpenAI API key here or via environment variable
# os.environ["OPENAI_API_KEY"] = "your-key-here"

def load_system_prompt():
    with open("prompts/system_prompt.txt", "r") as f:
        return f.read()

def build_agent():
    tools = [search_web, summarize_text, save_report]

    prompt = ChatPromptTemplate.from_messages([
        ("system", load_system_prompt()),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    agent = create_openai_tools_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=6,
        handle_parsing_errors=True
    )

    return agent_executor

def run(topic: str):
    print(f"\n{'='*60}")
    print(f"🤖 Research Agent Starting...")
    print(f"📌 Topic: {topic}")
    print(f"{'='*60}\n")

    agent = build_agent()

    result = agent.invoke({
        "input": f"Research the following topic thoroughly and "
                 f"save a complete report: {topic}"
    })

    print(f"\n{'='*60}")
    print("✅ Agent completed successfully!")
    print(f"{'='*60}")
    print("\n📄 Final Output:\n")
    print(result["output"])

if __name__ == "__main__":
    # Change this to any topic you want to research
    topic = "Generative AI applications in fintech and payments 2025"
    run(topic)