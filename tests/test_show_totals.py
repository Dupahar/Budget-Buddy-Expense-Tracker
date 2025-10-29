import tempfile
from show_totals import show_totals

def test_show_totals_basic(tmp_path):
    file = tmp_path / "expenses.txt"
    file.write_text("Food,10\nTransport,5.5\nFood,2.5\n")
    totals = show_totals(str(file))
    assert totals["Food"] == 12.5
    assert totals["Transport"] == 5.5
