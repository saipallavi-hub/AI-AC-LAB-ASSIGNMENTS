#write a python code Generate a recommendation system that also provides reasons for each suggestion.
import random
def recommend_items(user_preferences, item_database, num_recommendations=5):
    """
    This function generates recommendations based on user preferences and an item database.
    
    Parameters:
    - user_preferences: A dictionary containing user preferences (e.g., {'genre': 'sci-fi', 'price_range': 'low'})
    - item_database: A list of dictionaries, each representing an item with attributes (e.g., [{'name': 'Item1', 'genre': 'sci-fi', 'price': 'low'}, ...])
    - num_recommendations: The number of recommendations to return
    
    Returns:
    - A list of tuples containing recommended items and the reasons for their recommendation.
    """
    
    recommendations = []
    
    # Filter items based on user preferences
    filtered_items = []
    for item in item_database:
        match = True
        for key, value in user_preferences.items():
            if item.get(key) != value:
                match = False
                break
        if match:
            filtered_items.append(item)
    
    # If not enough items match preferences, fill with random items
    if len(filtered_items) < num_recommendations:
        additional_items = [item for item in item_database if item not in filtered_items]
        filtered_items.extend(random.sample(additional_items, min(num_recommendations - len(filtered_items), len(additional_items))))
    
    # Select recommendations and generate reasons
    for item in random.sample(filtered_items, min(num_recommendations, len(filtered_items))):
        reason = f"Recommended because it matches your preference for {', '.join([f'{k}: {v}' for k, v in user_preferences.items()])}."
        recommendations.append((item, reason))
    
    return recommendations
# Example usage
if __name__ == "__main__":
    user_preferences = {'genre': 'sci-fi', 'price': 'low'}
    item_database = [
        {'name': 'Item1', 'genre': 'sci-fi', 'price': 'low'},
        {'name': 'Item2', 'genre': 'fantasy', 'price': 'medium'},
        {'name': 'Item3', 'genre': 'sci-fi', 'price': 'high'},
        {'name': 'Item4', 'genre': 'sci-fi', 'price': 'low'},
        {'name': 'Item5', 'genre': 'romance', 'price': 'low'},
        {'name': 'Item6', 'genre': 'sci-fi', 'price': 'medium'},
    ]
    
    recommendations = recommend_items(user_preferences, item_database, num_recommendations=3)
    
    for item, reason in recommendations:
        print(f"Recommended Item: {item['name']}")
        print(f"Reason: {reason}\n")
        