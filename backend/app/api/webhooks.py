import hashlib
import hmac
import os

from fastapi import APIRouter, HTTPException, Request,Header 

router = APIRouter(prefix="/webhooks")



@router.post("/razorpay")
async def razorpay_webhook(
    request: Request,
    signature: str | None = Header(
        default=None,
        alias="X-Razorpay-Signature",
    ),
):

    secret = os.getenv("RAZORPAY_WEBHOOK_SECRET")

    if not secret:
        raise HTTPException(
            status_code=500,
            detail="Webhook secret is not configured",
        )

    # 2. Read the original request body
    raw_body = await request.body()

    if not signature:
        raise HTTPException(
            status_code=400,
            detail="Missing webhook signature",
        )

    # 4. Calculate the expected signature
    expected_signature = hmac.new(
        secret.encode("utf-8"),
        raw_body,
        hashlib.sha256,
    ).hexdigest()

    # 5. Reject requests with an invalid signature
    if not hmac.compare_digest(expected_signature, signature):
        raise HTTPException(
            status_code=400,
            detail="Invalid webhook signature",
        )

    # 6. Parse JSON only after signature verification
    try:
        payload = await request.json()
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON payload",
        )

    if not isinstance(payload, dict):
        raise HTTPException(
            status_code=400,
            detail="JSON payload must be an object",
        )

    # 7. Return a development response
    return {
        "received": True,
        "body_length": len(raw_body),
        "event": payload.get("event"),
    }