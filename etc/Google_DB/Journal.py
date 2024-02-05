import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys


def wait_for_enter():
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


class DailyJournal:
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

    def add_entry(self):
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_time = datetime.now().strftime("%Y-%m-%d")
        # Ask specific questions about the situation
        print(
            "\nThese are the Q's which helps you to reflect not necessarily you need to answer all this but use these Q's to formulate your responses"
        )
        print("Lets Start")
        print("Situation / Trigger")
        what_happened = input("What happened? ")
        wait_for_enter()
        where = input("Where? ")
        wait_for_enter()
        when = input("When? ")
        wait_for_enter()
        who_with = input("Who with? ")
        wait_for_enter()
        how = input("How? ")
        wait_for_enter()
        # Combine the situation details into a single string
        situation_trigger = f"{what_happened}. {where}. {when}. {who_with}. {how}"
        print("\nGet It all Out. Write everything")
        print(situation_trigger)
        print()

        # Ask specific questions about feelings
        print("Feelings Emotions & Body Sensations")
        emotion = input("1. What emotion did I feel at that time? ")
        wait_for_enter()
        what_else = input("2. What else? ")
        wait_for_enter()
        intensity = input("3. How intense was it? ")
        wait_for_enter()
        body_notice = input("4. What did I notice in my body? ")
        wait_for_enter()
        where_felt = input("5. Where did I feel it? ")
        wait_for_enter()

        feelings = f"{emotion}. {what_else}. Intensity: {intensity}. Body Notice: {body_notice}. Where Felt: {where_felt}"
        print(
            "\nFeeling better? You are the best, YOu have achieved a lot. You go to the extra mile, YOu find innovative solutions, you must be super proud!"
        )
        print(feelings)
        print()

        print("Unhelpful Thoughts / Images")
        thought_through_mind = input("1. What went through my mind? ")
        wait_for_enter()
        disturbed_by = input(
            "2. What disturbed me? What did those thoughts/images/memories mean to me, or say about me or the situation? "
        )
        wait_for_enter()
        responding_to = input("3. What am I responding to? ")
        wait_for_enter()
        button_pressed = input(
            "4. What ‘button’ is this pressing for me? What would be the worst thing about that, or that could happen? "
        )
        wait_for_enter()

        unhelpful_thoughts_images = (
            f"{thought_through_mind}. {disturbed_by}. {responding_to}. {button_pressed}"
        )
        print(unhelpful_thoughts_images)
        print(
            "\nThis is the garbage memory You pick either from your or someone else behaviour. Discard it"
        )

        print("\nFacts that provide Evidence against the unhelpful thought")
        # Ask specific questions about facts supporting the unhelpful thought
        facts_support_unhelpful_thought_1 = input("1. What are the facts? ")
        wait_for_enter()
        facts_support_unhelpful_thought_2 = input(
            "2. What facts do I have that the unhelpful thought/s are totally true? "
        )
        wait_for_enter()

        facts_support_unhelpful_thought = (
            f"{facts_support_unhelpful_thought_1}. {facts_support_unhelpful_thought_2}"
        )
        print(facts_support_unhelpful_thought)
        print("We are our own worst critic. Show it some love too")

        print()
        print("Facts that provide Evidence against the unhelpful thought")

        # Ask specific questions about facts providing evidence against the unhelpful thought
        facts_evidence_against_unhelpful_thought_1 = input(
            "1. What facts do I have that the unhelpful thought/s are NOT totally true? "
        )
        wait_for_enter()
        opinion_or_fact = input(
            "2. Is it possible that this is opinion, rather than fact? "
        )
        wait_for_enter()
        others_opinions = input("3. What have others said about this? ")
        wait_for_enter()
        facts_evidence_against_unhelpful_thought = f"{facts_evidence_against_unhelpful_thought_1}. Opinion or Fact: {opinion_or_fact}. Others' Opinions: {others_opinions}"
        print(
            "Look at you finally feeling free! Obviously our thoughts can create problems when there are none. YOu remember yesterday you were feeling anxious because you saw a girl and she laugh and your first thought was, if my lower torn? Even though it was perfectly fine, the girl wasnt even looking at you but that was your thought. Dont take these weightless neuron synapses too seriously."
        )
        print(facts_evidence_against_unhelpful_thought)
        print("\nAlternative: more realistic and balanced perspective")
        alternative_perspective_1 = input(
            "STOPP! Take a breath…. 1. What would someone else say about this situation? What’s the bigger picture? "
        )
        wait_for_enter()
        alternative_perspective_2 = input("2. Is there another way of seeing it? ")
        wait_for_enter()
        alternative_perspective_3 = input("3. What advice would I give someone else? ")
        wait_for_enter()
        alternative_perspective_4 = input(
            "4. Is my reaction in proportion to the actual event? "
        )
        wait_for_enter()
        alternative_perspective_5 = input(
            "5. Is this really as important as it seems? "
        )

        alternative_perspective = f"{alternative_perspective_1}. {alternative_perspective_2}. {alternative_perspective_3}. {alternative_perspective_4}. {alternative_perspective_5}"
        encouraging_message = "\nYou're doing great! Embracing different perspectives can lead to amazing growth. Remember, life is a journey, and every experience helps shape who you are becoming. Keep exploring new viewpoints and watch how your world expands!"

        print(alternative_perspective)
        print(encouraging_message, "\n")
        outcome_re_rate_emotion_1 = input(
            "Outcome: Re-rate emotion 1. What am I feeling now? (0-100%) "
        )
        wait_for_enter()
        outcome_re_rate_emotion_2 = input(
            "2. What could I do differently? What would be more effective? "
        )
        wait_for_enter()
        outcome_re_rate_emotion_3 = input("3. Do what works! Act wisely. ")
        wait_for_enter()
        outcome_re_rate_emotion_4 = input(
            "4. What will be most helpful for me or the situation? "
        )
        wait_for_enter()
        outcome_re_rate_emotion_5 = input("5. What will the consequences be? ")
        wait_for_enter()
        outcome_re_rate_emotion = f"{outcome_re_rate_emotion_1}. {outcome_re_rate_emotion_2}. {outcome_re_rate_emotion_3}. {outcome_re_rate_emotion_4}. {outcome_re_rate_emotion_5}"
        print(
            "You have earned 10 points. "
            "Your mental health i getting better, you feeel amazing. Your dreams are becoming reality, you are finding lots of love, and every thing you want, is at your disposal. You are destined for greatness, never be scared, be brave, laugh at scares. LION"
        )
        entry = [
            current_date_time,
            date_time,
            situation_trigger,
            feelings,
            unhelpful_thoughts_images,
            facts_support_unhelpful_thought,
            facts_evidence_against_unhelpful_thought,
            alternative_perspective,
            outcome_re_rate_emotion,
        ]
        self.worksheet.append_row(entry)
        print("Entry added successfully.")


# Example usage:
if __name__ == "__main__":
    journal = DailyJournal(
        "Thought Diary Format_Saksham",
        "../../secrets/high-triode-283417-cdca1a47ea5e.json",
    )
    journal.add_entry()

"""
what-ifs and could-have-beens.  I'm trapped in a never-ending loop, replaying scenes from the past like a broken record
When ruminating about past, automatically, 
goes for too long, No physical feeling or even mental, 
but then I get urge to stop what Im doing and smoke	

Little tired, unfocused, uninterested.  There's no tangible sensation, no physical ache. A little small funny feeling in stomach

Comparison, thinking about past, ex	

There are no facts to suppor if Im better or worse as compared to her or anyone else	

I have better job, life, satisfaction, experience, knowledge	

A. It is common to not be in present. 
It is natural to seek pleasure after a hard work session. 
When I want a quick out, jerkoff, entertainment or daydream can offer solace, 
but it is like empty calorie. It is neither real, nor helpful. 
In fact, they often left me feeling more depleted than before.. 
And when was the last time comparison between you and anyone else told you that You have an edge? 
Alt will be appreciating myself for even smallest to biggest thing I do, 
as the song goes:  you've gotta make your own kind of music Sing your own special song. 
Give myself small, medium nd large victories to keep me happy, but again, my self worth, 
my self, I doesnt depend on wns or external activities, I am hence I am 	

"""
