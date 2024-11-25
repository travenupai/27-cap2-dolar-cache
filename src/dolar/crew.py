from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.dolar.tools.dollar_exchange_tool import dollar_exchange_tool

# Uncomment the following line to use an example of a custom tool
# from dolar.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class Dolar():
	"""Dolar crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def exchange_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['exchange_agent'],
			tools =[dollar_exchange_tool],
			verbose=True,
			allow_delegation=False,
   
		)

	
	@task
	def check_exchange_rate(self) -> Task:
		return Task(
			config=self.tasks_config['check_exchange_rate'],
		)

		
	@crew
	def crew(self) -> Crew:
		"""Creates the Dolar crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
