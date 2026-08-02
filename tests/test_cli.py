import os
from unittest.mock import patch, MagicMock
from csv_chat_local.cli import main

@patch('csv_chat_local.cli.subprocess.run')
def test_cli_runs_streamlit(mock_run):
    main()
    
    # Verify subprocess.run was called
    mock_run.assert_called_once()
    
    # Get the arguments it was called with
    args, kwargs = mock_run.call_args
    cmd = args[0]
    
    # Check that it's running streamlit run app.py
    assert "-m" in cmd
    assert "streamlit" in cmd
    assert "run" in cmd
    assert cmd[-1].endswith("app.py")
