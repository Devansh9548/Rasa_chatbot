from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRespondDoctorAddress(Action):
    def name(self) -> Text:
        return "action_respond_doctor_address"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        specialty = tracker.get_slot("specialty")
        dispatcher.utter_message(text=f"Your appointment with a {specialty} specialist has been booked. Please note the details.")
        return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideDoctorAddress(Action):

    def name(self) -> Text:
        return "action_provide_doctor_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Replace with the actual address of the doctor's department
        doctor_address = "123 Main Street, Suite 205"

        dispatcher.utter_message(text=f"The doctor's department is located at {doctor_address}")

        return []
