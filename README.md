# Sudoku Solver

Simple script to solve sudoku puzzles using a backtrace method.

Also validates that a puzzle is solvable.

Both aspects exposed as API endpoints see openapi.yaml for specification

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


No web UI so you'll need CURL / Postman / ... to submit.

Working example wih cURL
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

### TODO's

 - [ ] test suite for sudoku library
 - [ ] better sanitization of user input
 - 