# ===============================================================
# patent_crew.py
# ===============================================================
# Full workflow for analyzing patent trends using CrewAI + Ollama.
# Compatible with: Python 3.11+, CrewAI 0.28+, crewai-tools, langchain-ollama
# ===============================================================

from crewai import Agent, Crew, Task, Process
from crewai_tools import BaseTool
from langchain_ollama import OllamaLLM
from typing import Optional, List


# ===============================================================
# 1. DEFINE A CUSTOM TOOL
# ===============================================================
class AnalyzePatentTrendsTool(BaseTool):
    """
    A custom tool that analyzes patent summaries and extracts
    emerging technology trends.
    """

    name: str = "Analyze Patent Trends"
    description: str = (
        "Analyzes summarized patent data and identifies patterns or technologies "
        "showing significant growth potential."
    )

    def _run(self, query: str) -> str:
        """
        Simulates trend analysis logic. Replace this with a call to
        a real analytics API, LLM, or dataset.
        """
        return (
            f"🔍 Trend Analysis for: '{query}'\n"
            f"- AI-driven healthcare and automation are gaining traction.\n"
            f"- Robotics patents show increased filings in manufacturing and surgery.\n"
            f"- Green tech and sustainable materials are the next big wave.\n"
            f"- Predict strong growth in embedded AI and energy-efficient hardware."
        )


# ===============================================================
# 2. SET UP THE LLM
# ===============================================================
# Make sure you have Ollama installed and a model pulled, e.g.:
#   ollama pull llama3.1
# ===============================================================
llm = OllamaLLM(model="llama3.1:latest")


# ===============================================================
# 3. DEFINE AGENTS
# ===============================================================
research_agent = Agent(
    role="Patent Researcher",
    goal="Gather and summarize the latest AI-related patent data.",
    backstory=(
        "A patent research expert skilled in analyzing large datasets of filings "
        "to identify key innovations, inventors, and industries driving change."
    ),
    llm=llm,
)

trend_agent = Agent(
    role="Technology Trend Analyst",
    goal="Detect patterns and forecast emerging innovations using summarized data.",
    backstory=(
        "A forward-thinking analyst specializing in AI, automation, and sustainability, "
        "capable of translating raw patent data into actionable insights."
    ),
    llm=llm,
)


# ===============================================================
# 4. DEFINE TOOLS
# ===============================================================
trend_tool = AnalyzePatentTrendsTool()


# ===============================================================
# 5. DEFINE TASKS
# ===============================================================
task1 = Task(
    description=(
        "Search the USPTO and WIPO databases for the 20 most recent AI-related patents "
        "filed globally. Summarize each with inventor, assignee, and technical focus."
    ),
    expected_output="A concise summary of 20 recent AI patents with relevant metadata.",
    agent=research_agent,
)

task2 = Task(
    description=(
        "Use the summarized patent dataset to analyze trends and emerging topics "
        "using the trend analysis tool."
    ),
    expected_output="A structured trend report outlining 3–5 emerging technologies.",
    agent=trend_agent,
    tools=[trend_tool],
)

task3 = Task(
    description=(
        "Generate an executive summary that connects the discovered trends "
        "to potential business and R&D opportunities."
    ),
    expected_output="A 1-page narrative summarizing future opportunities in AI patents.",
    agent=trend_agent,
)


# ===============================================================
# 6. BUILD THE CREW
# ===============================================================
crew = Crew(
    agents=[research_agent, trend_agent],
    tasks=[task1, task2, task3],
    process=Process.sequential,
)


# ===============================================================
# 7. RUN THE CREW
# ===============================================================
if __name__ == "__main__":
    print("\n🚀 Starting Patent Research Crew...\n")
    result = crew.kickoff()
    print("\n================ FINAL REPORT ================\n")
    print(result)
    print("\n==============================================\n")
