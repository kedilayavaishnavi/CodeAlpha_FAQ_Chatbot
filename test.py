from chatbot_engine import FAQBot

bot = FAQBot("faqs.csv")
print(bot.get_answer("Can I get my money back?"))
print(bot.get_answer("What's the weather today?"))