from typing import Optional
import pytest
from Easy.merge_two_sorted_lists import ListNode, mergeTwoLists 

def test_mergeTwoLists_two_full_lists_returns_one_sorted_list():

    # Arrange
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    expected = [1, 1, 2, 3, 4, 4]

    # Act
    result_node = mergeTwoLists(list1, list2)

    # Convert the result linked list to a list for comparison
    result = []
    while result_node:
        result.append(result_node.val)
        result_node = result_node.next

    # Assert
    assert result == expected

def test_mergeTwoLists_two_empty_lists_returns_empty_list():

    # Arrange
    list1 = None
    list2 = None
    expected = []

    # Act
    result_node = mergeTwoLists(list1, list2)

    # Convert the result linked list to a list for comparison
    result = []
    while result_node:
        result.append(result_node.val)
        result_node = result_node.next

    # Assert
    assert result == expected

def test_mergeTwoLists_one_empty_list_returns_one_sorted_list():

    # Arrange
    list1 = None
    list2 = ListNode(0)
    expected = [0]

    # Act
    result_node = mergeTwoLists(list1, list2)

    # Convert the result linked list to a list for comparison
    result = []
    while result_node:
        result.append(result_node.val)
        result_node = result_node.next

    # Assert
    assert result == expected