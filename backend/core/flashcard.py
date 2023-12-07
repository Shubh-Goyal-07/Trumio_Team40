import google.generativeai as palm
from markdown import Markdown
from io import StringIO
import os
import environ

env = environ.Env()
environ.Env.read_env()

class Flashcard:
    def __init__(self):
        
        palm.configure(api_key=os.environ['GOOGLE_API_KEY'])

    def print_content(self, project, summary):
        prompt = f"""
        You are an expert summarizer, and you add some fun and catchy content to the summary. 
        You have to create flash-card content for the {project} project, where details of what the user has done are: {summary}. 
        Follow the following guidelines while making a short and fun summary of the project:

        1. The summarizing - flash card content must summarize the project completion process in small points.
        2. The content should be short, fun, and satisfactory.
        3. No more than five pointers can be written.
        """

        completion = palm.generate_text(
            model="models/text-bison-001",
            prompt=prompt,
            temperature=0,
            max_output_tokens=800,
        )
        return completion.result
    def input_text(self, project, summary):
        return self.print_content(project, summary)





def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text) if text else ""



def flashcard_text_generator(project_name,summary_text):
    my_flashcard = Flashcard()
    markdownoutput = my_flashcard.input_text(project_name,summary_text)
    unmarked_yorker = unmark(markdownoutput)
    return unmarked_yorker

# project_name = "ATM Management System"

# summary_text = """
# Created an ATM Management system using MySQL and python. MySQL was used to store the user credentials: 
# userid and password, and bank account details such as bank balance, loan etc. Python-MySQL connector 
# was used to establish a link between python and MySQL so that it was convenient to code through python. 
# An ATM-like interface was built in python where the new users were asked to create an account by entering 
# their preferred userid and password, while recurring users were asked to log in using their credentials. 
# Then a choice-based interface just like in ATMs was shown where users could choose between: withdraw money, 
# deposit money, check bank balance, etc.
# """
# print(flashcard_text_generator(project_name,summary_text))
