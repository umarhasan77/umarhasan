from langgraph.graph import StateGraph, END

class ResearchGraph:
    def __init__(self, researcher, drafter):
        self.researcher = researcher
        self.drafter = drafter

    def run(self, query):
        research_data = self.researcher.run(query)
        answer = self.drafter.run(research_data)
        return answer