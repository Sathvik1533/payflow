import hashlib
import hmac

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

TEST_SECRET = "payflow-local-test-secret"


def test_webhook_accepts_valid_signature(monkeypatch):
    monkeypatch.setenv("RAZORPAY_WEBHOOK_SECRET", TEST_SECRET)

    body = b'{"event":"payment.captured"}'

    signature = hmac.new(
        TEST_SECRET.encode("utf-8"),
        body,
        hashlib.sha256,
    ).hexdigest()
    response = client.post(
        "/webhooks/razorpay",
        content=body,
        headers={
            "Content-Type": "application/json",
            "X-Razorpay-Signature": signature,
        },
    )
    
    assert response.status_code == 200
    assert response.json()["received"] is True
    assert response.json()["event"] == "payment.captured"


def test_webhook_rejects_invalid_signature(monkeypatch):
    monkeypatch.setenv("RAZORPAY_WEBHOOK_SECRET", TEST_SECRET)

    body = b'{"event":"payment.captured"}'

    response = client.post(
        "/webhooks/razorpay",
        content=body,
        headers={
            "Content-Type": "application/json",
            "X-Razorpay-Signature": "invalid-signature",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid webhook signature"

def test_webhook_rejects_missing_signature(monkeypatch):
    monkeypatch.setenv("RAZORPAY_WEBHOOK_SECRET", TEST_SECRET)

    response = client.post(
        "/webhooks/razorpay",
        content=b'{"event":"payment.captured"}',
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Missing webhook signature"


def test_webhook_rejects_invalid_json(monkeypatch):
    monkeypatch.setenv("RAZORPAY_WEBHOOK_SECRET", TEST_SECRET)

    body = b"not-json"

    signature = hmac.new(
        TEST_SECRET.encode("utf-8"),
        body,
        hashlib.sha256,
    ).hexdigest()

    response = client.post(
        "/webhooks/razorpay",
        content=body,
        headers={
            "Content-Type": "application/json",
            "X-Razorpay-Signature": signature,
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid JSON payload"
