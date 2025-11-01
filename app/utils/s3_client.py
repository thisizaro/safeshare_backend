# app/utils/s3_client.py
from botocore.client import Config
import boto3
from typing import Optional
from app.config.settings import (
    STORAGE_PROVIDER,
    S3_ENDPOINT_URL,
    S3_ACCESS_KEY,
    S3_SECRET_KEY,
    S3_REGION,
    S3_USE_SSL,
    S3_BUCKET,
)


class S3ClientWrapper:
    def __init__(
        self,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        region_name: Optional[str] = None,
        use_ssl: bool = False,
        bucket: Optional[str] = None,
    ):
        self.bucket = bucket or S3_BUCKET

        # If endpoint_url is provided, configure for MinIO (S3-compatible).
        if endpoint_url:
            self.client = boto3.client(
                "s3",
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                endpoint_url=endpoint_url,
                region_name=region_name,
                config=Config(signature_version="s3v4"),
                verify=use_ssl,
            )
        else:
            # Default boto3 client (AWS credentials from env or IAM)
            self.client = boto3.client("s3", region_name=region_name)

    def upload_fileobj(self, file_obj, key: str, content_type: Optional[str] = None):
        """
        Uploads a file-like object to the configured bucket.
        file_obj: file-like object (must be binary, anzd pointer at start)
        key: object key in bucket
        """
        extra = {}
        if content_type:
            extra["ContentType"] = content_type
        self.client.upload_fileobj(Fileobj=file_obj, Bucket=self.bucket, Key=key, ExtraArgs=extra)

    def download_stream(self, key: str):
        """
        Returns a streaming body (botocore.response.StreamingBody).
        Caller can read() or iterate it.
        """
        resp = self.client.get_object(Bucket=self.bucket, Key=key)
        return resp["Body"], resp.get("ContentType", "application/octet-stream")

    def delete_object(self, key: str):
        self.client.delete_object(Bucket=self.bucket, Key=key)

    def ensure_bucket_exists(self):
        # For MinIO/local dev create bucket if not exists.
        try:
            self.client.head_bucket(Bucket=self.bucket)
        except Exception:
            # Try to create the bucket
            self.client.create_bucket(Bucket=self.bucket)
