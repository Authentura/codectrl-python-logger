#!/usr/bin/env bash

if [[ ! -d ./protos || ! "$(ls -A ./protos)" ]]; then
  git submodule init protos
fi

if ! command -v python3 >/dev/null; then
  echo "Please install python3"
  exit 1
fi

if ! command -v pip >/dev/null; then
  echo "Please install pip"
  exit 1
fi

pip install -r ./requirements.txt

python3 -m grpc_tools.protoc \
  -I=./protos/ \
  --python_out=./codectrl/protos/ \
  --pyi_out=./codectrl/protos/ \
  ./protos/log.proto \
  ./protos/backtrace_data.proto

python3 -m grpc_tools.protoc \
  -I=./protos/ \
  --python_out=./codectrl/protos/ \
  --pyi_out=./codectrl/protos/ \
  --grpc_python_out=./codectrl/protos \
  ./protos/cc_service.proto \
  ./protos/auth.proto
