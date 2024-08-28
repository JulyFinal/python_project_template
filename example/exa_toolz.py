from loguru import logger
from toolz import compose_left
from toolz import pipe


def add(x: int) -> int:
    logger.info(f"add {x} and {x}")
    return x + x


def convert_num(x: int) -> str:
    logger.info(f"convert number {x} to string {x}")
    return str(x)


def convert_str(x: str) -> int:
    logger.info(f"convert string {x} to int {x}")
    return int(x)


run_line = compose_left(add, convert_num, convert_str)

print(run_line(1))

print(pipe(1, run_line))
