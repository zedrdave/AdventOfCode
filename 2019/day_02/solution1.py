from os import path
from typing import List


def input_to_prog(data: str) -> List[int]:
    return [int(part) for part in data.strip().split(',')]


def run_program(prog: List[int], noun: int, verb: int) -> int:
    prog[1] = noun
    prog[2] = verb
    ptr = 0
    while prog[ptr] != 99:
        if prog[ptr] == 1:
            v1 = prog[prog[ptr + 1]]
            v2 = prog[prog[ptr + 2]]
            prog[prog[ptr + 3]] = v1 + v2
        elif prog[ptr] == 2:
            v1 = prog[prog[ptr + 1]]
            v2 = prog[prog[ptr + 2]]
            prog[prog[ptr + 3]] = v1 * v2
        else:
            raise RuntimeError(f'Unknown opcode {prog[ptr]} at index {ptr}')

        ptr += 4

    return prog[0]


def main() -> None:
    dirname = path.dirname(__file__)
    infile = path.join(dirname, 'input.txt')
    with open(infile, 'r') as input_file:
        init_state = input_to_prog(input_file.read())
        output = run_program(init_state, 12, 2)
        print(f'Solution : {output}')


if __name__ == '__main__':
    main()
