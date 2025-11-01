# tests/test_s3_client.py
import pytest
from app.utils.s3_client import S3ClientWrapper
from app.config.settings import (
    S3_ACCESS_KEY,
    S3_SECRET_KEY,
    S3_ENDPOINT_URL,
    S3_REGION,
    S3_USE_SSL,
    S3_BUCKET,
)

def test_s3_client_init():
    client = S3ClientWrapper(
        access_key=S3_ACCESS_KEY,
        secret_key=S3_SECRET_KEY,
        endpoint_url=S3_ENDPOINT_URL,
        region_name=S3_REGION,
        use_ssl=S3_USE_SSL,
        bucket=S3_BUCKET,
    )
    assert client.bucket == S3_BUCKET
