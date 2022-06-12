# bash function
title () {
  printf "\n\n"
  printf "**************************\n"
  printf "* $1\n"
  printf "**************************\n"
}

HOST=http://127.0.0.1
PORT=8888


title "/items/"
curl -s ${HOST}:${PORT}/items/

title "/items/start_id=1?end_id=3"
curl -s ${HOST}:${PORT}/items/?start_id=1&end_id=3 | json_pp
