import json
from datetime import datetime
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from secrets import sheet_name, id_name
from messages import get_gita_info, list_of_messages, get_stoic_quotes


class DailyJournal:
    ENCOURAGING_MESSAGES = list_of_messages()

    def __init__(self, spreadsheet_name, credentials_file):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_file, scope
        )
        self.client = gspread.authorize(credentials)
        self.spreadsheet = self.client.open(spreadsheet_name)
        self.worksheet = self.spreadsheet.get_worksheet(0)

    def _wait_for_enter(self):
        enter_count = 0
        while True:
            key = input()
            if key == "":
                enter_count += 1
                if enter_count == 2:
                    print(f"\nEnter count = {enter_count + 1}")
                    print("Press enter to confirm")
                    print()
                if enter_count >= 3:
                    break
            else:
                enter_count = 0

    def _ask_question(self, question):
        user_input = input(question)
        self._wait_for_enter()
        return user_input

    def _get_date_time(self):
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_time = datetime.now().strftime("%Y-%m-%d")
        return current_date_time, date_time

    def _ask_situation_trigger(self):
        print("\nSituation / Trigger")
        questions = ["What happened? ", "Where? ", "When? ", "Who with? ", "How? "]
        answers = [self._ask_question(question) for question in questions]
        situation_trigger = ". ".join(answers)
        return situation_trigger

    def _ask_feelings_emotions(self):
        print("\nFeelings Emotions & Body Sensations")
        questions = [
            "1. What emotion did I feel at that time? ",
            "2. What else? ",
            "3. How intense was it? ",
            "4. What did I notice in my body? ",
            "5. Where did I feel it? ",
        ]
        answers = [self._ask_question(question) for question in questions]
        feelings = ". ".join(answers)
        return feelings

    def _ask_unhelpful_thoughts_images(self):
        print("\nUnhelpful Thoughts / Images")
        questions = [
            "1. What went through my mind? ",
            "2. What disturbed me? What did those thoughts/images/memories mean to me, or say about me or the situation? ",
            "3. What am I responding to? ",
            "4. What ‘button’ is this pressing for me? What would be the worst thing about that, or that could happen? ",
        ]
        answers = [self._ask_question(question) for question in questions]
        unhelpful_thoughts_images = ". ".join(answers)
        return unhelpful_thoughts_images

    def _ask_facts_support_unhelpful_thought(self):
        print("\nFacts that provide Evidence against the unhelpful thought")
        questions = [
            "1. What are the facts? ",
            "2. What facts do I have that the unhelpful thought/s are totally true? ",
        ]
        answers = [self._ask_question(question) for question in questions]
        facts_support_unhelpful_thought = ". ".join(answers)
        return facts_support_unhelpful_thought

    def _ask_facts_evidence_against_unhelpful_thought(self):
        print("\nFacts that provide Evidence against the unhelpful thought")
        questions = [
            "1. What facts do I have that the unhelpful thought/s are NOT totally true? ",
            "2. Is it possible that this is opinion, rather than fact? ",
            "3. What have others said about this? ",
        ]
        answers = [self._ask_question(question) for question in questions]
        facts_evidence_against_unhelpful_thought = ". ".join(answers)
        return facts_evidence_against_unhelpful_thought

    def _ask_alternative_perspective(self):
        print("\nAlternative: more realistic and balanced perspective")
        questions = [
            "STOPP! Take a breath…. 1. What would someone else say about this situation? What’s the bigger picture? ",
            "2. Is there another way of seeing it? ",
            "3. What advice would I give someone else? ",
            "4. Is my reaction in proportion to the actual event? ",
            "5. Is this really as important as it seems? ",
        ]
        answers = [self._ask_question(question) for question in questions]
        alternative_perspective = ". ".join(answers)
        return alternative_perspective

    def _ask_outcome_re_rate_emotion(self):
        print("\nOutcome: Re-rate emotion")
        questions = [
            "1. What am I feeling now? (0-100%) ",
            "2. What could I do differently? What would be more effective? ",
            "3. Do what works! Act wisely. ",
            "4. What will be most helpful for me or the situation? ",
            "5. What will the consequences be? ",
        ]
        answers = [self._ask_question(question) for question in questions]
        outcome_re_rate_emotion = ". ".join(answers)
        return outcome_re_rate_emotion

    def _ask_additional_comments(self):
        print("\nAdditional Comments:")
        additional_comments = input("Write anything else you want to tell us: ")
        return additional_comments

    def _show_encouragements(self):
        print(random.choice(self.ENCOURAGING_MESSAGES))

    def _display_message(self, message):
        print(message)

    def _ask_for_input(self, section_name, questions):
        print(f"\n{section_name}:")
        answers = [self._ask_question(question) for question in questions]
        return ". ".join(answers)

    def add_entry(self):
        current_date_time, date_time = self._get_date_time()

        sections = {
            "Situation / Trigger": [
                "What happened? ",
                "Where? ",
                "When? ",
                "Who with? ",
                "How? ",
            ],
            "Feelings Emotions & Body Sensations": [
                "1. What emotion did I feel at that time? ",
                "2. What else? ",
                "3. How intense was it? ",
                "4. What did I notice in my body? ",
                "5. Where did I feel it? ",
            ],
            "Unhelpful Thoughts / Images": [
                "1. What went through my mind? ",
                "2. What disturbed me? What did those thoughts/images/memories mean to me, or say about me or the situation? ",
                "3. What am I responding to? ",
                "4. What ‘button’ is this pressing for me? What would be the worst thing about that, or that could happen? ",
            ],
            "Facts that support the unhelpful thought": [
                "1. What are the facts? ",
                "2. What facts do I have that the unhelpful thought/s are totally true? ",
            ],
            "Facts that provide Evidence against the unhelpful thought": [
                "1. What facts do I have that the unhelpful thought/s are NOT totally true? ",
                "2. Is it possible that this is opinion, rather than fact? ",
                "3. What have others said about this? ",
            ],
            "Alternative: more realistic and balanced perspective": [
                "STOPP! Take a breath…. 1. What would someone else say about this situation? What’s the bigger "
                "picture? ",
                "2. Is there another way of seeing it? ",
                "3. What advice would I give someone else? ",
                "4. Is my reaction in proportion to the actual event? ",
                "5. Is this really as important as it seems? ",
            ],
            "Outcome: Re-rate emotion": [
                "1. What am I feeling now? (0-100%) ",
                "2. What could I do differently? What would be more effective? ",
                "3. Do what works! Act wisely. ",
                "4. What will be most helpful for me or the situation? ",
                "5. What will the consequences be? ",
            ],
            "Additional Comments": ["Write anything else you want to tell us: "],
        }

        entry = {"current_date_time": current_date_time, "date_time": date_time}

        for section, questions in sections.items():
            entry[section] = self._ask_for_input(section, questions)
            self._show_encouragements()
            print()

        self._display_message("\nEntry added successfully.")

        # Save the entry to a JSON file
        with open("jsons/entries.json", "a+") as json_file:
            json.dump(entry, json_file, indent=4)
            json_file.write("\n")

        total_text = f"{list(entry.values())}"

        # Append the entry to the Google Sheets spreadsheet
        self.worksheet.append_row(list(entry.values()))
        return total_text

def main():
    journal = DailyJournal(
        sheet_name, id_name)

    question = journal.add_entry()
    krishna_says = get_gita_info(question)
    entry = {"question": question, "krishna_says": krishna_says}

    # Save the entry to a JSON file
    with open("jsons/krishna_says.json", "a+") as json_file:
        json.dump(entry, json_file, indent=4)
        json_file.write("\n")

    print(krishna_says)

    val2 = get_gita_info("Help me find my self and heal inner child")
    print(val2)

    val = get_stoic_quotes()
    print(val)


if __name__ == "__main__":
    main()

