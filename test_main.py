import pytest
from fastapi.testclient import TestClient
from main import app


class TestBase:
    client = TestClient(app)

    def test_home(self) -> None:
        response = self.client.get(
            app.url_path_for('point1')
        )
        assert response.status_code == 200

    def test_save(self) -> None:
        response = self.client.get(
            app.url_path_for('point2')
        )
        assert response.status_code == 200
