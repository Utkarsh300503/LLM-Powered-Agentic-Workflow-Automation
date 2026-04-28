# 🤖 LLM-Powered Agentic Workflow Automation

An AI agent built with LangChain and OpenAI that autonomously 
handles multi-step research workflows — searching, summarizing, 
and compiling structured reports from a single prompt.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange)
![Automation](https://img.shields.io/badge/Workflow%20Time-60%25%20Reduced-brightgreen)

---

## 🎯 Problem Statement

Multi-step research workflows — searching for information, 
reading sources, summarizing findings, and compiling reports 
— are repetitive and time-consuming. This agent replaces 
30-45 minutes of manual work with a single prompt, running 
the entire pipeline autonomously.

---

## 🧠 How the Agent Works
User Prompt → LangChain Agent → Tool Selection & Execution
→ Memory & Decision Loop → Structured Report → Saved Output

1. **Input** — User provides a research topic or task
2. **Search** — Agent queries DuckDuckGo for relevant information
3. **Summarize** — Custom summarizer tool condenses findings
4. **Compile** — Agent structures output into a clean report
5. **Save** — Report saved locally with timestamp

---

## ⚙️ Agentic Pipeline Architecture

┌─────────────────────────────────────────┐
│           LangChain Agent               │
│                                         │
│  ┌─────────┐  ┌──────────┐  ┌────────┐ │
│  │ Search  │  │Summarizer│  │ Save   │ │
│  │  Tool   │  │  Tool    │  │ Tool   │ │
│  └─────────┘  └──────────┘  └────────┘ │
│                                         │
│         Memory + Decision Loop          │
└─────────────────────────────────────────┘

- **Memory** — Retains context across tool calls in a session
- **Tool Use** — Agent decides which tool to call and when
- **Decision Loop** — Iterates until task is fully complete
- **Verbose Mode** — Full reasoning trace visible for debugging

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Workflow Time Saved | **60%** |
| Manual Time (before) | 30–45 mins |
| Agent Time (after) | < 5 mins |
| Max Iterations | 5 (configurable) |

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **LangChain** — agent framework, tool use, memory
- **OpenAI GPT-3.5-turbo** — core reasoning model
- **DuckDuckGo Search** — real-time web search tool
- **LangChain Community** — additional tool integrations

---

## 🚀 Setup & Run

```bash
# Clone the repo
git clone https://github.com/Utkarsh300503/LLM-Agentic-Workflow-Automation.git
cd LLM-Agentic-Workflow-Automation

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
# Windows: set OPENAI_API_KEY=your-api-key-here

# Run the agent
python main.py
```

---

## 📁 Project Structure

├── main.py                  # Entry point — agent setup and execution
├── tools/
│   ├── search_tool.py       # DuckDuckGo search integration
│   ├── summarizer_tool.py   # LLM-based summarization tool
│   └── save_tool.py         # Report saving tool
├── prompts/
│   └── system_prompt.txt    # Agent system prompt
├── reports/                 # Auto-generated research reports
├── requirements.txt
└── README.md

---

## 💡 Example Usage

```python
# Run the agent on any research topic
result = agent_executor.invoke({
    "input": "Research the latest trends in Generative AI 
               for fintech applications"
})

# Agent will:
# 1. Search for relevant information
# 2. Summarize key findings  
# 3. Compile a structured report
# 4. Save report to /reports folder
```

**Sample Output:**

Entering new AgentExecutor chain...
Invoking search tool: "Generative AI fintech 2025"
Invoking summarizer tool: [search results]
Invoking save tool: "report_20250429_143022.txt"
Report saved successfully.

---

## 🔍 Key Engineering Decisions

- **OpenAI Tools Agent** over ReAct — more reliable tool 
  calling with structured outputs
- **DuckDuckGo** over SerpAPI — no API key needed, 
  zero cost for testing
- **Max iterations capped at 5** — prevents infinite loops 
  while allowing complex multi-step tasks
- **Verbose mode on** — full agent reasoning visible, 
  useful for debugging and demos

---

## 🗺️ Future Improvements

- [ ] Add PDF/URL ingestion as input source
- [ ] Integrate vector memory for cross-session context
- [ ] Add Slack/email output tool
- [ ] Support for CrewAI multi-agent collaboration

---

## 👤 Author

**Utkarsh Tiwari**  
[LinkedIn](https://linkedin.com/in/utkarshtiwari300503) •
[GitHub](https://github.com/Utkarsh300503)
