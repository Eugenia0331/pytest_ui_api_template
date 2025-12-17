from api.BoardApi import BoardApi

def test_get_boards():
    api = BoardApi("https://api.trello.com/1")
    board_list = api.get_all_boards_by_org_id("ID организации")
    print(board_list)

def test_create_board():
    api = BoardApi("https://api.trello.com/1")
    board_list_before = api.get_all_boards_by_org_id("ID организации").get("boards")

    resp = api.create_board("Test board")
    print(resp)
    board_list_after = api.get_all_boards_by_org_id("ID организации").get("boards")

    assert len(board_list_after) - len(board_list_before) == 1

def test_delete_board():
    api = BoardApi("https://api.trello.com/1")
    board_list_before = api.get_all_boards_by_org_id("ID организации").get("boards")

    resp = api.delete_board_by_id("id")
    print(resp)

    board_list_after = api.get_all_boards_by_org_id("id").get("boards")

    assert len(board_list_before) - len(board_list_after) == 1