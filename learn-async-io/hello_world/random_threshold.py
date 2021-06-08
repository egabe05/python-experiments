import asyncio
import random

c = (
    "\33[0m",   # end of color
    "\33[36m",  # cyan
    "\33[91m",  # red
    "\33[35m",  # magenta
)


async def makerandom(idx:int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}.")
    print(f"{idx}: threshold == {threshold}")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
