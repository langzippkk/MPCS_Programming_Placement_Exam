# NP-problem
# The solution could be verified in polynomial complexity

import sys

fhand = sys.stdin
lines = fhand.readlines()

N = int(lines[0].strip())

# Initialize the board
board = list()
for i in xrange(len(lines)-1):
    board.append(([0] * N))

# Put the queen on the board
for i in xrange(len(lines)-1):
    x = int(lines[i+1].strip().split(' ')[0])
    y = int(lines[i+1].strip().split(' ')[1])
    board[x][y] = 1

correctness = True

def correctness_check(board):
    correctness = True
    # Check rows
    for i in xrange(N):
        num_queen = 0
        for j in xrange(N):
            num_queen += board[i][j]
        if num_queen > 1:
            correctness = False
            #print 1
            return correctness

    # Check columns
    for j in xrange(N):
        num_queen = 0
        for i in xrange(N):
            num_queen += board[i][j]
        if num_queen > 1:
            correctness = False
            #print 2
            return correctness


    # Check one diagnal
    for i in xrange(N):
        num_queen = 0
        for j in xrange(N-i):
            num_queen += board[i+j][0+j]
        if num_queen > 1:
            correctness = False
            #print 3
            return correctness

    for j in xrange(N):
        num_queen = 0
        for i in xrange(N-j):
            num_queen += board[0+i][j+i]
        if num_queen > 1:
            correctness = False
            #print 4
            return correctness

    # Check the other diagnal
    for i in xrange(N):
        num_queen = 0
        for j in xrange(i):
            num_queen += board[i-j][0+j]
        if num_queen > 1:
            correctness = False
            #print 5
            return correctness

    for j in xrange(N):
        num_queen = 0
        for i in xrange(N-j):
            num_queen += board[N-1-i][j+i]
        if num_queen > 1:
            correctness = False
            #print 6
            return correctness

    return correctness

if correctness_check(board = board) == True:
    print('CORRECT')
else:
    print('INCORRECT')