import google.generativeai as palm
from markdown import Markdown
from io import StringIO
from .unmark import unmark
import os
import environ
env = environ.Env()
environ.Env.read_env()


class Timeline:
    def __init__(self):
        palm.configure(api_key=env('GOOGLE_API_KEY'))

    def print_content(self, project, weeks):
        prompt = f'''
        You are an expert work planner. Assume that the user is working on a {project} project. Create a weekly based project timeline for him that contains all the necessary details of what he needs to complete by the week. The following has to be followed while making the timeline:

        1. THE PROJECT TIMELINE HAS TO BE FOR {weeks} WEEKS!! 
        2. Do not provide day-to-day based timeline. 
        3. For every week, explain in detail the task that needs to be completed. 
        4. The explanation of every task must be done in pointers.
        '''


        completion = palm.generate_text(
            model="models/text-bison-001",
            prompt=prompt,
            temperature=0,
            max_output_tokens=800,
        )
        return completion.result
    def input_text(self, project, weeks):
        return self.print_content(project, weeks)





def timeline_generator(project_name,weeks):
    my_timeline = Timeline()
    markdownoutput = my_timeline.input_text(project_name,weeks)
    unmarked_yorker = unmark(markdownoutput)
    return unmarked_yorker

# project_name = "E-commerce Platform"

# summary_text = """
# Created an ATM Management system using MySQL and python. MySQL was used to store the user credentials: 
# userid and password, and bank account details such as bank balance, loan etc. Python-MySQL connector 
# was used to establish a link between python and MySQL so that it was convenient to code through python. 
# An ATM-like interface was built in python where the new users were asked to create an account by entering 
# their preferred userid and password, while recurring users were asked to log in using their credentials. 
# Then a choice-based interface just like in ATMs was shown where users could choose between: withdraw money, 
# deposit money, check bank balance, etc.
# """
# print(timeline_generator(project_name,4))


