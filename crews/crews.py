from crewai import Crew
from agents.agents import coding_agent
from tasks.tasks import return_compiled_task
import random

ages = [random.randint(13, 19) for _ in range(50)]
ages_as_string = ",".join(map(str, ages))

analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[return_compiled_task(ages_as_string)]
)