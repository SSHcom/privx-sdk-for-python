#!/usr/bin/env bash

set -e

linter_path="$*"

if [  $# -eq 0 ];
then
  linter_path="privx_api";
fi

# --- flake8 ---
flake8 $linter_path --config ./linter_config.cfg --exit-zero

# --- black ---
black $linter_path

# --- isort ---
isort $linter_path --settings-path ./linter_config.cfg

# --- radon ---
radon mi -s -n B $linter_path

exit
