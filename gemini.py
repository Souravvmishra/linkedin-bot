import time
import google.generativeai as genai
import telebot

bot = telebot.TeleBot("6064570542:AAElcStNmpmmRwfcClBjTMHT7SJiJ9442xU")

genai.configure(api_key="AIzaSyCBFNk2oMDu26hDxmpVp5vpJeB-jKEFMcA")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "input: write a random unique advice by masculinesage twitter account.",
  "output: They only try to\npull you down when you are above them. What is your long-term goal? If you\n  Don’t have one; consider this your task for today. Make a 50-year plan. It is\nnot about what you deserve. It is about how badly you want something. The\n  hard work makes you worthy.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: I don't care if\n  you watch porn or not. But if you are into incest. God is watching you. You\n  are a stain on your family's name and you will suffer in life due to lack of\n  basic values and honor.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: You can't rob a\n  man who has nothing. You can't shame a man with no honor. A man with no honor\n  can never be trusted.",
  "input: write a random unique advice by masculinesage twitter account.write a random unique advice by masculinesage twitter account.",
  "output: Going to therapy\n  is a trend these days. Too many individuals are seeking mental support.\n  Mental weakness is at an all-time high.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: Don't compare\n  your girl with other girls. Only a fool does that. Stay away from a man who\n  can't say no to his woman. His life is filled with dishonor, shame and\n  failures.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: Don't beg others\n  for a party. Let them invite you or never talk about it. Don't live with a\n  needy broke vibe around you. Always have large goals. Even if you know you\n  can't achieve it. Because you will miss, and you will still hit a goal much\n  beyond your capabilities.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: You can solve\n  nearly all of your married life problems if you take care of the things in\n  the bedroom. The answer to a good life is hidden in your way of life. Do you\n  have a routine? How much time do you spend under the sun? How much do you\n  connect with nature? You can't be high energy living in dark rooms with LEDs.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: You don't have to\n  force women to make them submissive. Just make them comfortable living under\n  your leadership and she will be submissive on her own.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: What is your\n  life's purpose? It is not allowed because it is not right.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: All of this is\n  achievable. Most men live in a delusion that it is all luck.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: Funny how they\n  believe that Ego is demonic. Equal rights and equal responsibilities. Funny\n  how this makes some people angry.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: They want you to\n  distrust your brothers so you become weak. The weaker you will become the\n  easier you will be to defeat and rule. Don't trust those who make rules for\n  you. Trust the brotherhood.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output: Politics is not\n  about views, values or motives. It is about power. Interact with people you\n  love, even if you don’t have a reason to. Avoid people you hate. Being liked\n  is more important than being right in a social situation. Don’t be the who is\n  always proving others wrong. Always avoid arguments. Start your day with\n  energy. Spend time in Sun. Spend time with your loved ones. Honor your\n  parents. Locked out of heaven. I am a Man of God.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output : People hate Zuckerberg and Elon\n\nBut no one knows who runs TikTok\n\nLesson in there",
  "input: write a random unique advice by masculinesage twitter account.",
  "output : You cannot trust man who abandons his parents. A man who is not loyal to the people who created him cannot be loyal to anyone else.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :If the human lifespan was 200 years, most people would waste an additional 100 years",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :What the fuck is a \"dream job\"\n\nWho the hell is dreaming about having a job",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :Never forget that you're going to die.\n\nYou gotta do whatever you want to do before that happens.\n\nLots of people forget that",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :A man with a landlord and an employer is not a free man.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :Stop being shy. No one gives a fuck about you.\n\nYou think you look awkward. No one else thinks about you at all.\n\nYou are not in high school where everyone notices every time you speak.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :People are not \"against you\"\n\nPeople are for themselves.\n\nThey simply do not care about you",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :Never buy a car on a loan.\n\nBuy in cash or don't buy it.\n\nPeople buying consumer goods with debt are slaves working for a bank's profits.\n\nIf you have $10k, buy a $10k car. If you have $50k, buy a 50k car.\n\nIf you have 10k but you're buying a $50k car with debt, you're an idiot.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :If you're rich, you could wear fake gold and diamond jewellery and everyone will assume it's real.\n\nIf you're poor, you could wear real gold and everyone will assume it's fake.\n\nLesson in there.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :You could get hit by a car today and die.\n\nIn 3 months everyone except your mom and dad would move on.\n\nThe only two people who *truly* care.\n\nShame on people who abandon their parents.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :You're a man. No one cares about your problems.\n\nLift weights, eat well, and go solve them.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :Never disrespect a friend when he's with his girl. Hype him up instead.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :At age 25, it stops being about your \"potential\" and starts being about results.\n\n18 to 25 is the time society gives you to figure things out.\n\nBeyond that - you WILL be considered a loser if you're not making things happen.",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :The reason women don't have to pay to enter clubs is because they're the product.\n\nYou can hate it but it's true",
  "input: write a random unique advice by masculinesage twitter account.",
  "output :I've said this before, but it bears repeating:\n\n99% of the things you worry about can be solved by getting physically stronger, making more money, and a bit of meditation.",
  "input: write a random unique advice by masculinesage twitter account as an developer or startup founder or engineer. Write things that are in  trend now a days",
  "output: ",
]

# response = model.generate_content(prompt_parts)
# print(str(response.text))


def get_tweet():
    return  str(model.generate_content(prompt_parts).text)
