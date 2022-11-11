#!/usr/bin/env bash

if ! command -v python3 >/dev/null; then
  echo "python3 not found, please install python3 per your distribution's package manager."
  exit 1
fi

if [[ -d "./.venv" ]]; then
  echo "Virtualenv already exists"
  exit 1
fi

python3 -m venv .venv

echo "Virtual env created, please issue source ./.venv to enter Python Virtualenv"
