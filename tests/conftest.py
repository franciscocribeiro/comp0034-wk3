import os
from pathlib import Path
import pytest
from Birth_App import create_app, db

@pytest.fixture(scope = "module")
def app():

    deb_path = Path(__file__).parent.parent.joinpath