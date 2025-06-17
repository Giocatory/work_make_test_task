import sys
import pytest
from csv_processor.cli import main

def write_csv(tmp_path, text: str) -> str:
    file = tmp_path / "data.csv"
    file.write_text(text)
    return str(file)

def test_cli_no_args(capsys):
    with pytest.raises(SystemExit):
        main()

def test_cli_filter(tmp_path, capsys, monkeypatch):
    path = write_csv(tmp_path, "name,price\nx,5\ny,15\n")
    monkeypatch.setattr(sys, 'argv', ['prog', path, '--filter', 'price', 'gt', '10'])
    main()
    captured = capsys.readouterr()
    assert 'y' in captured.out

def test_cli_agg(tmp_path, capsys, monkeypatch):
    path = write_csv(tmp_path, "name,price\nx,5\ny,15\n")
    monkeypatch.setattr(sys, 'argv', [
        'prog', path,
        '--filter', 'price', 'gt', '0',
        '--agg', 'price', 'avg'
    ])
    main()
    captured = capsys.readouterr()
    assert 'avg(price)' in captured.out
