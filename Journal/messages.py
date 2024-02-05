import requests
import random


def list_of_messages():
    unique_encouraging_messages = [
        "You're doing great! Keep up the good work!",
        "Remember, every small step counts towards progress.",
        "You've got this! Believe in yourself.",
        "Embrace the journey of self-reflection. You're growing every day.",
        "Your commitment to journaling is commendable. Keep it up!",
        "Celebrate your efforts in self-care. You deserve it.",
        "Reflecting on your day shows resilience and self-awareness. Keep going!",
        "You handled the situation with grace and composure.",
        "You navigated through the challenge admirably.",
        "You showed resilience in facing the triggering event.",
        "Despite the circumstances, you remained steadfast.",
        "Your ability to adapt to different situations is impressive.",
        "You acknowledged your emotions with honesty and bravery.",
        "You demonstrated self-awareness by recognizing your feelings.",
        "You managed your emotions with maturity and insight.",
        "Your awareness of your body's response is a sign of mindfulness.",
        "You're in tune with your emotional and physical well-being.",
        "You confronted unhelpful thoughts with courage.",
        "You challenged negative thoughts with a rational perspective.",
        "You recognized the impact of unhelpful thoughts on your well-being.",
        "You're taking steps to break free from limiting thought patterns.",
        "You're building resilience by addressing unhelpful thoughts head-on.",
        "You're actively seeking clarity by examining the facts.",
        "You're discerning between factual evidence and subjective interpretations.",
        "You're exploring the validity of your thoughts through objective analysis.",
        "You're gaining insights into the underlying beliefs shaping your thoughts.",
        "You're developing a deeper understanding of the factors influencing your mindset.",
        "You're challenging distorted thinking with evidence-based reasoning.",
        "You're uncovering alternative perspectives that counteract negative beliefs.",
        "You're recognizing the role of perception in shaping your thoughts.",
        "You're integrating external feedback to challenge unhelpful assumptions.",
        "You're cultivating a balanced perspective through critical reflection.",
        "You're broadening your perspective to see the bigger picture.",
        "You're exploring alternative viewpoints to foster understanding.",
        "You're approaching the situation with empathy and compassion.",
        "You're considering the advice you would offer to others in similar circumstances.",
        "You're maintaining perspective by evaluating the significance of the event.",
        "You're monitoring your emotional response with self-awareness.",
        "You're exploring constructive ways to manage your emotions.",
        "You're prioritizing actions that promote emotional well-being.",
        "You're making empowered choices to navigate challenging emotions.",
        "You're evaluating the potential outcomes of your decisions with clarity.",
        "You're embracing growth and self-discovery with courage.",
        "You're committed to your journey of personal development.",
        "You're fostering a positive mindset through self-reflection.",
        "You're investing in your well-being with dedication and perseverance.",
        "You're inspiring others with your resilience and determination.",
        "'As Epictetus said, 'It's not what happens to you, but how you react to it that matters.'",
        "'In the words of Marcus Aurelius, 'The impediment to action advances action. What stands in the way becomes the way.'",
        "'When we are no longer able to change a situation, we are challenged to change ourselves.' - Viktor E. Frankl",
        "'As the Bhagavad Gita teaches, 'You have control over your work alone, never the fruit.'",
        "'The only way out is through.' - Robert Frost",
        "'Pain is inevitable, suffering is optional.' - Haruki Murakami",
        "'You have power over your mind, not outside events. Realize this, and you will find strength.' - Marcus Aurelius",
        "'We suffer more often in imagination than in reality.' - Seneca",
        "'The soul becomes dyed with the color of its thoughts.' - Marcus Aurelius",
        "'If it is not right, do not do it, if it is not true, do not say it.' - Marcus Aurelius",
        "'How much time he gains who does not look to see what his neighbor says or does or thinks, but only at what he does himself, to make it just and holy.' - Marcus Aurelius",
        "'The happiness of your life depends upon the quality of your thoughts.' - Marcus Aurelius",
        "'Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.' - Marcus Aurelius",
        "'It is not the man who has too little, but the man who craves more, that is poor.' - Seneca",
        "'The best revenge is to be unlike him who performed the injury.' - Marcus Aurelius",
        "'Waste no more time arguing about what a good man should be. Be one.' - Marcus Aurelius",
        "'When you arise in the morning, think of what a precious privilege it is to be alive - to breathe, to think, to enjoy, to love.' - Marcus Aurelius",
        "'Dwell on the beauty of life. Watch the stars, and see yourself running with them.' - Marcus Aurelius",
    ]


def get_stoic_quotes():
    url = "https://stoic-quotes.com/api/quote"
    response = requests.get(url)
    return response.json()["text"]


def get_gita_info(question):
    # Encode the question to be included in the URL
    encoded_question = requests.utils.quote(question)
    # URL with the encoded question
    url = f"https://gitagpt.org/api/ask/gita?q={encoded_question}&email=null&locale=en"
    # Make the request
    response = requests.get(url)
    return response.json()["response"]
