from langchain_core.messages import HumanMessage
from graph.graph import app
from crews.crews import analysis_crew

if __name__ == '__main__':
    # Use the Runnable
    final_state = app.invoke(
        {"messages": [HumanMessage(content="what is the weather in sf")]},
        config={"configurable": {"thread_id": 42}}
    )
    result1 = final_state['messages'][-1].content
    print(f"RESULT 1: {result1}")

    final_state = app.invoke(
        {"messages": [HumanMessage(content="what about ny")]},
        config={"configurable": {"thread_id": 42}}
    )
    result2 = final_state['messages'][-1].content
    print(f"RESULT 2: {result2}")

    result3 = analysis_crew.kickoff()

    print(f"RESULT 3 (CODING AGENT): {result3}")