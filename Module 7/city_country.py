def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country} - {language}"
    else:
        return f"{city}, {country}"


# Call the function with different arguments
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan", 13929286))
print(city_country("Paris", "France", 2148000, "French"))
