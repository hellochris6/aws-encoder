# AWS Encoder

This simple Python script reads a CSV file containing S3 bucket names and object keys, URL-encodes the keys, and outputs a new CSV with the encoded values. It's particularly useful for preparing S3 object keys for use in APIs or web contexts where special characters must be percent-encoded.

## Features

- Reads CSV input in the format: `bucket,key`
- URL-encodes the S3 object key using `urllib.parse.quote`
- Outputs a new CSV with encoded keys

## Requirements

- Python 3.x (no external dependencies)

## Setup

Clone the repo and ensure you're running Python 3.

```bash
git clone https://github.com/yourusername/aws-encoder.git
cd aws-encoder
