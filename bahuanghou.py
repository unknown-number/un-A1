{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nested = [[1, 2], [3, 4], [5]]\n",
    "def flatten(nested): \n",
    "    for sublist in nested: \n",
    "         for element in sublist: \n",
    "            yield element "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nested = [[1, 2], [3, 4], [5]]\n",
    "for num in flatten(nested):\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(flatten(nested))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sum(i ** 2 for i in range(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "clear"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def conflict(state, nextX): \n",
    "    nextY = len(state) \n",
    "    for i in range(nextY): \n",
    "        if abs(state[i] - nextX) in (0, nextY - i): \n",
    "            return True \n",
    "    return False\n",
    "def queens(num, state): \n",
    "    if len(state) == num-1: \n",
    "        for pos in range(num): \n",
    "            if not conflict(state, pos): \n",
    "                yield pos\n",
    "list(queens(4,(1,3,0)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(queens(4,(1,3)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def conflict(state, nextX): \n",
    "    nextY = len(state) \n",
    "    for i in range(nextY): \n",
    "        if abs(state[i] - nextX) in (0, nextY - i): \n",
    "            return True \n",
    "    return False\n",
    "def queens(num=8, state=()): \n",
    "    for pos in range(num): \n",
    "        if not conflict(state, pos): \n",
    "            if len(state) == num-1: \n",
    "                yield (pos,) \n",
    "            else: \n",
    "                for result in queens(num, state + (pos,)): \n",
    "                    yield (pos,) + result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(queens(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(queens(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list(queens(8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prettyprint(solution): \n",
    "    def line(pos, length=len(solution)): \n",
    "        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1) \n",
    "    for pos in solution: \n",
    "        print(line(pos))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random \n",
    "prettyprint(random.choice(list(queens(8))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
