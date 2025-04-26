from langchain.tools.tavily_search import TavilySearchResults
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI

class ResearchAgent:
    def __init__(self):
        self.search_tool = TavilySearchResults(k=5)

    def run(self, query):
        results = self.search_tool.invoke({"query": query})
        return results

class AnswerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

    def run(self, research_data):
        prompt = f"Based on the following research results, draft a detailed, coherent answer:\n{research_data}"
        messages = [SystemMessage(content="You are an expert answer drafter."), HumanMessage(content=prompt)]
        answer = self.llm.invoke(messages)
        return answer.content