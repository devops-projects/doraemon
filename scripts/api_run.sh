#!/usr/bin/env bash

curent_dir=$(cd "$(dirname "$0")" || exit; pwd)
base_dir="${curent_dir}/.."

cd "$base_dir" || exit

# source venv/bin/activate

# export FLASK_DEBUG=True
export FLASK_APP="src/backend"
flask run