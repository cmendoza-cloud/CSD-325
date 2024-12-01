def city_country(city, country, population=None, language=None):
    """Return a string in the format City, Country - population xxx, Language."""
    result = f"{city}, {country}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"
    return result

# Call the function with different arguments
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan", 13929286))
print(city_country("Paris", "France", 2148000, "French"))
