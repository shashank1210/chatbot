# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# actions.py
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import sqlite3

# class ActionSearchCollege(Action):
#     def name(self) -> Text:
#         return "action_search_college"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # Get user's query
#         user_message = tracker.latest_message.get('text')
        
#         # Search database
#         conn = sqlite3.connect('E:/projeto/scripts/college_data.db')
#         c = conn.cursor()
        
#         # Search in content and title
#         c.execute('''
#             SELECT title, content, url 
#             FROM pages 
#             WHERE content LIKE ? OR title LIKE ?
#             LIMIT 1
#         ''', (f'%{user_message}%', f'%{user_message}%'))
        
#         result = c.fetchone()
        
#         if result:
#             title, content, url = result
#             # Send a condensed response
#             summary = content[:200] + '...' if len(content) > 200 else content
#             response = f"{title}\n\n{summary}\n\nMore info: {url}"
#             dispatcher.utter_message(text=response)
#         else:
#             dispatcher.utter_message(text="I couldn't find specific information about that. Please try rephrasing your question.")
        
#         conn.close()
#         return []