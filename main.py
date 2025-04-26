from agents import ResearchAgent, AnswerAgent
from graph import ResearchGraph

def main():
    query = input("Enter your research query: ")
    researcher = ResearchAgent()
    drafter = AnswerAgent()
    graph = ResearchGraph(researcher, drafter)
    answer = graph.run(query)
    print("\nGenerated Answer:\n")
    print(answer)

if __name__ == "__main__":
    main()