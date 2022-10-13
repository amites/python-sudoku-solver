# Sudoku Solver

Simple script to solve sudoku puzzles using a backtrace method.

Also validates that a puzzle is solvable.

Both aspects exposed as API endpoints see [openapi.yaml](https://editor.swagger.io/?url=https://raw.githubusercontent.com/amites/sudoku-solver/main/openapi.yaml) for specification

To use either

```
pip3 install -r requirements.txt
python3 src/app.py
```

OR use docker
```
docker build -t sudoku .

docker run -p 5000:5000 sudoku
```


No web UI so you'll need cURL / Postman / ... to submit.

cURL example
```
curl --location --request POST 'http://localhost:5000/solve' \
  --form 'board="..3..5..1 2..3...4. 1....7..5 ......... ......... .02..6... ......... 81....... ........."'
```


---------

Sudoku class is unit tested

```
cd src
python -m unittest test_sudoku.py
```

or run from command line directly

### TODO's

 - [ ] expand test suite for sudoku library
 - [ ] test suite for flask app
 - [ ] better sanitization of user input
