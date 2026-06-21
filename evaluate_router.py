from router import router

# A dataset of queries the router has NEVER seen before
test_data = [
    # --- SQL / Product Queries ---
    ("I'm searching for cheap laptops", "sql"),
    ("Do you have formal black shoes", "sql"),
    ("Show me smartwatches under 5000", "sql"),
    ("Where can I find running gear?", "sql"),
    ("Looking for an iphone", "sql"),
    ("Are there any red sneakers available?", "sql"),
    ("I need a gift for my brother, maybe a watch", "sql"),
    ("Show me the highest rated shoes", "sql"),
    ("Give me a list of gaming accessories", "sql"),
    ("I want to buy some electronics", "sql"),
    
    # --- FAQ Queries ---
    ("What happens if my item is broken?", "faq"),
    ("Can I return this after 14 days?", "faq"),
    ("How do I use my credit card?", "faq"),
    ("Is shipping free to my country?", "faq"),
    ("When will the delivery guy arrive?", "faq"),
    ("My package is delayed, how do I track it?", "faq"),
    ("Do you accept cash on delivery?", "faq"),
    ("Is it possible to change my address now?", "faq"),
    ("What are your replacement rules?", "faq"),
    ("Are there any promo codes I can use right now?", "faq"),
    
    # --- Small Talk Queries ---
    ("Hey there", "small-talk"),
    ("Are you a human?", "small-talk"),
    ("Tell me a joke", "small-talk"),
    ("What's up?", "small-talk"),
    ("How is your day going?", "small-talk"),
    ("Good morning bot", "small-talk"),
    ("Who created you?", "small-talk"),
    ("Can we chat for a bit?", "small-talk"),
    ("You are very helpful", "small-talk"),
    ("Bye bye", "small-talk")
]

def evaluate():
    print("Evaluating Semantic Router Accuracy...\n")
    
    correct_predictions = 0
    total_predictions = len(test_data)
    
    # Track accuracy per category
    category_metrics = {
        "sql": {"correct": 0, "total": 0},
        "faq": {"correct": 0, "total": 0},
        "small-talk": {"correct": 0, "total": 0}
    }
    
    # Track errors to see where it gets confused
    errors = []

    for query, expected in test_data:
        # Pass query to router
        route_obj = router(query)
        predicted = route_obj.name if route_obj else "unknown"
        
        # Update metrics
        category_metrics[expected]["total"] += 1
        
        if predicted == expected:
            correct_predictions += 1
            category_metrics[expected]["correct"] += 1
        else:
            errors.append(f"Query: '{query}'\n  Expected: {expected} | Got: {predicted}\n")

    # --- Print Results ---
    accuracy = (correct_predictions / total_predictions) * 100
    print(f"Overall Accuracy: {accuracy:.2f}% ({correct_predictions}/{total_predictions})\n")
    
    print("--- Breakdown by Category ---")
    for category, metrics in category_metrics.items():
        cat_accuracy = (metrics["correct"] / metrics["total"]) * 100
        print(f"[{category.upper()}] Accuracy: {cat_accuracy:.2f}% ({metrics['correct']}/{metrics['total']})")
        
    if errors:
        print("\n--- Missclassified Queries ---")
        for error in errors:
            print(error)

if __name__ == "__main__":
    evaluate()
