#!/usr/bin/env bash

find ./codectrl/protos \
  -name *_pb2*.py \
  -exec sed -i -E 's/^import (\w+_{1}pb2)/from \. import \1/g' {} \;
