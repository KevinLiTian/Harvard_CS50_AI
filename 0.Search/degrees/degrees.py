"""
A program that determines how many "degrees of sepatraion" apart
two hollywood actors are. Each degree consists of a film that two actors both starred in
"""

import csv
import sys

from util import Node, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    """ Main Function
    Take arguments from command line and get which dataset the AI
    will be using. Then use the shortest path function to get the
    degrees of separation between two stars
    """
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    if source == target:
        print("You have chosen the same person!")

    else:
        path = shortest_path(source, target)

        if path is None:
            print("Not connected.")
        else:
            degrees = len(path)
            print(f"{degrees} degrees of separation.")
            path = [(None, source)] + path
            for i in range(degrees):
                person1 = people[path[i][1]]["name"]
                person2 = people[path[i + 1][1]]["name"]
                movie = movies[path[i + 1][0]]["title"]
                print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # BFS search guarantee shortest path
    frontier = QueueFrontier()
    frontier.add(Node(source, None, None))

    searched = []
    searched.append(source)

    while not frontier.empty():
        # Get the next node and remove it from frontier
        cur_node = frontier.remove()
        if cur_node.state == target:
            path = back_track(cur_node)
            return path
        for (movie_id, person_id) in neighbors_for_person(cur_node.state):
            if not person_id in searched:
                searched.append(person_id)
                node = Node(person_id, cur_node, movie_id)
                frontier.add(node)

    return None

def back_track(node):
    """
    Back track from a node to the origin node through
    each node's parent node
    """
    path = []
    cur_node = node
    while cur_node.parent is not None:
        movie_id = cur_node.action
        person_id = cur_node.state
        path.insert(0, (movie_id, person_id))
        cur_node = cur_node.parent

    return path

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person))
    return neighbors


if __name__ == "__main__":
    main()
