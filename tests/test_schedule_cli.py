import os
from schedule_cli import main, DEFAULT_FILE


def test_cli_add_list_remove(tmp_path, capsys):
    file_path = tmp_path / "sched.json"

    # add event
    main(["--file", str(file_path), "add", "Meeting", "--date", "2024-06-01"])
    out = capsys.readouterr().out
    assert "Added" in out

    # list events
    main(["--file", str(file_path), "list"])
    out = capsys.readouterr().out
    assert "Meeting" in out

    # remove event
    main(["--file", str(file_path), "remove", "Meeting"])
    out = capsys.readouterr().out
    assert "Removed" in out

    # list again should be empty
    main(["--file", str(file_path), "list"])
    out = capsys.readouterr().out
    assert out.strip() == ""

