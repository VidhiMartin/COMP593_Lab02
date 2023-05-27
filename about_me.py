"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'name': 'Vidhi Martin',
        # TODO: Put full name into data structure
        'Student_ID': '10298344', 
        # TODO: Put student ID into data structure
        'Toppings': [
                'pepperoni',
                'cheese',
                'pineapple'
            ],
        # TODO: Put list of 3 pizza toppings into data structure
        'movies': [
           {
                'title': 'The empire strikes back',
                'genre': 'sci-fi'
            },
            {
                'title': 'Big hero 6',
                'genre': 'sci-fi'
            },
            # TODO: Add one more movie
        ]
    } 

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['ranch', 'pesto'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'Grave encounters', 'horror')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me['genres'], end = ', ')

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['titles'], end = ', ')

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    student_name = my_info['name']
    student_ID = my_info['Student_ID']
    # Print sentence containing name
    # Print sentence containing student ID
    print(f'My name is {student_name} and my student ID is {student_ID}')

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print('\n My favourite pizza toppings are: ')
    # Print bullet list of favourite pizza toppings
    for pizza_toppings in my_info['Toppings']:
        print(f' . {pizza_toppings}')

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['Toppings'].extend(toppings)
    for i, topping_name in enumerate(my_info['Toppings']):
     # Convert all pizza toppings to lowercase
         my_info['Toppings'][i] = topping_name.lowercase()
    # Sort toppings list alphabetically
    my_info['Toppings'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    new_movie = {
        'title': 'Grave encounters',
        'genre': 'horror'
    }
    my_info['movies'].append(new_movie)
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    
    print(my_info['genre'], end = ', ')

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print(movie_list['title'], end = ', ')

if __name__ == '__main__':
    main()