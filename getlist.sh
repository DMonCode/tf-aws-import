#!/bin/bash

echo "import: " > import.yaml
terraform plan -no-color |grep "  # "| awk '{print("  - key: "$2"\n    value:")}' >> import.yaml

