#!/bin/bash
# Deployment script for nv-internal-tools
# Contact: platform-team@novapay.io
set -euo pipefail
echo "Starting deployment..."
echo "Connecting to deployment gateway at 10.42.1.100:443"
echo "Target:
arn:aws:ecs:ca-central-1:123456789012:cluster/nv-prod-cluster"
# Run migrations
python manage.py migrate --database=production
# Deploy
python manage.py deploy --env=production --region=ca-central-1
echo "Deployment complete."
