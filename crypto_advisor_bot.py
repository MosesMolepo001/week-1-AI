# crypto_advisor_bot.py

# 1. Define chatbot personality
print("👋 Hi! I'm CryptoBuddy — your first AI-powered financial sidekick! 🚀")
print("Ask me anything about crypto trends or sustainable coins!")
print("Type 'exit' to end our chat.\n")

# 2. Predefined crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# 3. Chat loop
while True:
    user_query = input("You: ").lower()

    if user_query in ["exit", "quit", "bye"]:
        print("CryptoBuddy: Bye! And remember — crypto is risky. Do your own research! 🧠")
        break

    elif "trending" in user_query or "rising" in user_query:
        print("CryptoBuddy: These cryptos are currently trending up 📈:")
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising":
                print(f" - {coin}")

    elif "sustainable" in user_query or "eco" in user_query:
        # Recommend the most sustainable coin
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Go with {recommend}! 🌱 It’s eco-friendly and has long-term potential.")

    elif "energy" in user_query:
        print("CryptoBuddy: Here's how each coin ranks in energy usage:")
        for coin, data in crypto_db.items():
            print(f" - {coin}: {data['energy_use']}")

    elif "long-term" in user_query or "growth" in user_query or "invest" in user_query:
        # Find coins with rising trend and high market cap
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"CryptoBuddy: {coin} is trending and has a strong market cap — looks promising! 💰")

        # Recommend Cardano for sustainable + trending combo
        if crypto_db["Cardano"]["price_trend"] == "rising" and crypto_db["Cardano"]["sustainability_score"] > 7:
            print("CryptoBuddy: Also consider Cardano (ADA) — trending up and highly sustainable! 🚀")

    elif "market cap" in user_query:
        print("CryptoBuddy: Market cap breakdown:")
        for coin, data in crypto_db.items():
            print(f" - {coin}: {data['market_cap']}")

    else:
        print("CryptoBuddy: Sorry, I didn’t understand that. Try asking about rising, sustainable, energy use, long-term ,trends, sustainability, or investments. 🤖")

