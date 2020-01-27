""" https://www.interviewcake.com/question/python/inflight-entertainment """

from collections import Counter
from typing import List, Tuple, Optional


def find_movies(flight_length: int, movie_runtime_list: List[int]) -> bool:
    movie_counts = Counter(movie_runtime_list)
    for first_movie_runtime in movie_runtime_list:
        desired_second_movie_runtime = flight_length - first_movie_runtime
        has_second_movie = movie_counts.get(desired_second_movie_runtime)
        if has_second_movie and (desired_second_movie_runtime != first_movie_runtime or has_second_movie >= 2):
            return True
    return False


print(find_movies(100, [120, 40, 55, 30, 60, 40, 100, 100, 100]) is True)
print(find_movies(100, [120, 55, 30, 60, 100, 100, 100]) is False)
print(find_movies(100, [120, 55, 30, 60, 100, 100, 100]) is False)
print(find_movies(100, [120, 55, 30, 60, 50, 100, 100, 100]) is False)
print(find_movies(100, [120, 55, 30, 60, 50, 50, 100, 100, 100]) is True)


# todo: determine what this runtime is
def find_movies_within_x_minutes(flight_length: int, movie_runtime_list: List[int], stretch_space=20) -> bool:
    sorted_movies = sorted(movie_runtime_list)
    reverse_sorted_movies = list(reversed(sorted_movies))
    reverse_distance = 0
    for forward_count, forward in enumerate(sorted_movies):
        current_reverse_distance = reverse_distance
        if forward_count - len(movie_runtime_list) >= current_reverse_distance:
            # don't go forward over items we should already be skipping
            break
        for backward_count, backward in enumerate(reverse_sorted_movies[current_reverse_distance:]):
            if forward_count >= len(movie_runtime_list) - current_reverse_distance - backward_count - 1:
                # forward and backward are the same, don't invert the two tracers
                break
            combined_length = forward + backward
            desired_length = abs(combined_length - flight_length)

            if desired_length <= stretch_space:
                return True

            if combined_length - stretch_space > flight_length:
                # backward number is too big
                reverse_distance += 1

            if combined_length + stretch_space < flight_length:
                # forward number is too small
                break

    return False


print(find_movies_within_x_minutes(100, [0, 3, 5, 6, 10, 20, 60, 65, 75, 130, 150]) is True)
print(find_movies_within_x_minutes(100, [120, 40, 55, 30, 60, 40, 100, 100, 100]) is True)
print(find_movies_within_x_minutes(100, [120, 55, 30, 60, 100, 100, 100]) is True)
print(find_movies_within_x_minutes(100, [120, 55, 30, 60, 100, 100, 100]) is True)
print(find_movies_within_x_minutes(100, [120, 55, 30, 60, 50, 100, 100, 100]) is True)
print(find_movies_within_x_minutes(100, [120, 55, 30, 60, 50, 50, 100, 100, 100]) is True)
print(find_movies_within_x_minutes(100, [30, 40, 95, 120]) is False)


def _find_movies(flight_length: int, sorted_movie_sublist: List[int], current_best_fit: List[int]) -> Tuple[List[int], List[int]]:
    for movie_count, movie in enumerate(sorted_movie_sublist):
        sum_current_best_fit = sum(current_best_fit)
        if abs(sum_current_best_fit + movie - flight_length) < abs(sum_current_best_fit - flight_length):
            new_best_fit = current_best_fit.copy()
            new_best_fit.append(movie)
            return sorted_movie_sublist[movie_count + 1:], new_best_fit


def fit_any_movies(flight_length: int, movie_runtime_list: List[int]) -> Tuple[List[int], int]:
    """ given a flight length and a list of runtimes, provide the combination of movies that get you closest to the
    flight length and provide the combination runtime """

    sorted_movies = sorted(movie_runtime_list)
    first_movie = _find_movies(flight_length, sorted_movies, [])
    movies_to_find = [first_movie]

    best_movies = first_movie
    while movies_to_find:
        movie_to_find = movies_to_find.pop()
        if movie_to_find:
            if abs(sum(movie_to_find[1]) - flight_length) < abs(sum(best_movies[1]) - flight_length):
                best_movies = movie_to_find
            movies_to_find.append(movie_to_find)
    a = 1


print(fit_any_movies(100, [120, 55, 30, 60, 50, 100, 100, 100]) is False)
