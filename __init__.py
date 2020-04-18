from mycroft import MycroftSkill, intent_file_handler


class LewisSmells(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('smells.lewis.intent')
    def handle_smells_lewis(self, message):
        smell = ''

        self.speak_dialog('smells.lewis', data={
            'smell': smell
        })


def create_skill():
    return LewisSmells()

