def ft_filter(function, iterable):
    """
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if function is None:
        function = bool
    return (item for item in iterable if function(item))


# def test_ft_filter():
#     """
#     Test the ft_filter function against the built-in filter function.
#     """
#     # Define test cases
#     test_cases = [
#         # Test with a function (e.g., is_even)
#         {
#             "description": "Filter even numbers",
#             "function": lambda x: x % 2 == 0,
#             "iterable": [1, 2, 3, 4, 5, 6],
#             "expected": [2, 4, 6],
#         },
#         # Test with a function to filter strings
#         {
#             "description": "Filter non-empty strings",
#             "function": lambda s: len(s) > 0,
#             "iterable": ["hello", "", "world", ""],
#             "expected": ["hello", "world"],
#         },
#         # Test with None (truthy values)
#         {
#             "description": "Filter truthy values",
#             "function": None,
#             "iterable": [0, 1, False, 2, '', 3, None, 4],
#             "expected": [1, 2, 3, 4],
#         },
#         # Test with an empty iterable
#         {
#             "description": "Filter empty iterable",
#             "function": lambda x: x > 0,
#             "iterable": [],
#             "expected": [],
#         },
#         # Test with a function always returning False
#         {
#             "description": "Filter with always False function",
#             "function": lambda x: False,
#             "iterable": [1, 2, 3, 4],
#             "expected": [],
#         },
#         # Test with a function always returning True
#         {
#             "description": "Filter with always True function",
#             "function": lambda x: True,
#             "iterable": [1, 2, 3, 4],
#             "expected": [1, 2, 3, 4],
#         },
#     ]

#     # Run test cases
#     for case in test_cases:
#         print(f"Running test: {case['description']}")
#         # Apply ft_filter and built-in filter
#         ft_result = list(ft_filter(case["function"], case["iterable"]))
#         expected_result = list(filter(case["function"], case["iterable"]))

#         # Compare results
#         assert ft_result == expected_result, (
#             f"Test failed!\n"
#             f"Expected: {expected_result}\n"
#             f"Got: {ft_result}"
#         )
#         print(f"Passed! Output: {ft_result}")

# # Run the tester
# if __name__ == "__main__":
#     test_ft_filter()
