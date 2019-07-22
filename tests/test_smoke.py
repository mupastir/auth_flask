from http import HTTPStatus


class TestSmoke(object):

    def test_smoke(self, client):
        response = client.get("/auth/smoke")
        assert response.status_code == HTTPStatus.OK
        assert response.json["status"] == "success"
        assert response.json["message"] == "ok"
        assert "response_datetime" in response.json.keys()
