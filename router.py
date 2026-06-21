from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "How long does it take to process a refund?",
        "Are there any ongoing sales or promotions?",
        "Can I cancel or modify my order after placing it?",
        "Do you offer international shipping?",
        "What are the modes of refund available after cancellation?",
        "Can I ask the delivery agent to reschedule the pickup date?",
        "How quickly can I get my order delivered?",
        "Can I pay online?",
        "What payment methods are accepted?",
        "Where is my package?",
        "My item is damaged, what should I do?",
        "How do I use a promo code?",
        "Is there free shipping?",
        "Can I change my delivery address?",
        "I want a replacement for my order.",
        "Do you have cash on delivery?",
        "Is there any warranty on these products?",
    ],
)

sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
        "in black",
        "what about blue",
        "under 2000",
        "only puma",
        "for men",
        "do you have them in size 10",
        "I need to buy a watch",
        "give me a list of laptops",
        "show me electronic items",
        "do you sell smartphones",
        "looking for accessories",
        "I am looking for a specific product",
        "give me a list of"
    ],
)

small_talk = Route(
    name="small-talk",
    utterances=[
        "Hi",
        "How are you?",
        "What is your name?",
        "Are you a robot?",
        "What are you?",
        "What do you do?",
        "How can you help me?",
        "Where are you from?",
        "Hello there",
        "Good morning",
        "Good evening",
        "Tell me a joke",
        "Who made you?",
        "What's up",
        "Bye bye",
        "See you later",
        "You are awesome",
        "Thanks for the help",
        "I just want to chat",
        "Are you a human or AI?",
        "Can we talk?",
    ],
)

routes = [faq, sql, small_talk]

router = SemanticRouter(encoder=encoder, routes=routes, auto_sync="local")

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)
