import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    project = PriorityQueue()
    large_path = {"nome": "large_file", "qtd_linhas": 20}
    small_path = {"nome": "small_file", "qtd_linhas": 3}

    project.enqueue(large_path)
    assert len(project) == 1

    project.enqueue(small_path)
    assert project.search(0) == small_path
    assert project.search(1) == large_path
    
    project.dequeue()
    assert len(project) == 1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        project.search(2)
