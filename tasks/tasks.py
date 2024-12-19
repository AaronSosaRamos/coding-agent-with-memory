from crewai import Task
from agents.agents import coding_agent

def return_compiled_task(dataset):
    data_analysis_task = Task(
        description=f"Analyze the given dataset and calculate the average age of participants: {dataset}",
        agent=coding_agent,
        expected_output="The average age of participants in the dataset.",
    )

    return data_analysis_task