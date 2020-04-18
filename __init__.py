import random
from mycroft import MycroftSkill, intent_file_handler

smells = {'smells': [
    'Lush dirty spray',
    'Beard oil',
    'Hash browns',
    'Milk chocolate',
    'jose mourinho',
    'solder',
    'clocks',
    'wet dog',
    'palmolive soap',
    'orange lucozade',
    'original lucozade',
    'his grey blanket',
    'fried chicken',
    'bed slobber',
    'a lovely bit of squirrel',
    'tangfastics',
    'a really long sit down shower',
    'lawnmower oil',
    'hotel chocolat rocky road',
    'the space bar after playing football manager for 3 hours',
    'cheese wraps'
]}

class LewisSmells(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('smells.lewis.intent')
    def handle_smells_lewis(self, message):
        self.log.info("Seeing what lewis smells of.")
        smell = random.choice(smells['smells'])
        self.log.info(f"It's {smell}!")

        self.speak_dialog('smells.lewis', data={
            'smell': smell
        })


def create_skill():
    return LewisSmells()

