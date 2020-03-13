# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):
     def name(self) -> Text:
         return "action_hello_world"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []


class CovidQuestion(Action):

    def name(self) -> Text:
        return "action_question"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intents = ['greet', 'goodbye', 'affirm', 'deny', 'open_question','what_is_covid', 'what_symptoms',
                   'how_spread',
                   'how_spread_air',
                   'tf_transmitted_person_no_sy',
                   'tf_transmitted_person_feces',
                   'what_todo_protect',
                   'should_worry',
                   'how_risky',
                   'do_antibi_help',
                   'do_medici_exist',
                   'is_there_vaccine',
                   'should_use_mask',
                   'how_long_incubation',
                   'does_my_pet_get_infected',
                   'can_open_packages',
                   'want_know_more'
                   ]

        intent = tracker.latest_message["intent"].get("name")

        if intent in intents:
            dispatcher.utter_template("utter_"+intent, tracker)


        return []