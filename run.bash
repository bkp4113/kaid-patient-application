python3=`which python3`

python3 -m pip install -r ./requirements.txt

cd src
export PYTHON_PATH="${cwd}/src"

python3 ./server.py 2>&1> ../log/server.log &

sleep 5

python3 ../test.py

pkill -P $$