#დაწერეთ ორი ასინქრონული ფუნქცია, ერთ-ერთი დააყოვნეთ 2 წამი,
# მეორე 5 წამი, დაბეჭდეთ მათი დაწყება და დასრულება, თასქები შექმენით ცალ-ცალკე და გაუშვით.
#
import asyncio
import time
async  def square_numbers(num):
    print(f"listing square of numbers from 1 to {num} has started")
    for i in range(1,num+1):
        print(i**2)
    await asyncio.sleep(2)
    print("listing square of numbers has ended")

async def cube_numbers(num):
    print(f"listing cube of numbers from 1 to {num} has started")
    for i in range(1,num+1):
        print(i**3)
    await asyncio.sleep(5)
    print("listing cube of numbers has ended")

async def main():
    print("Start an asynchronous process")
    num = 100
    all_task = await asyncio.gather(square_numbers(num), cube_numbers(num))
    print(all_task)
start_1 = time.time()
asyncio.run(main())
print("End of asynchronous process")
print(time.time()-start_1)

# დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს
# და დაბეჭდავს მთელ რიცხვებს 0-დან რენდომულ რიცხვამდე

import asyncio
import time
import random
async def list_integers():
    print("Starting counting of integers")
    k = random.randint(20,50)
    await asyncio.sleep(1)
    print("Ending counting of integers")
    print(f"listing of integers from 0 to {k-1}")

    for i in range(k):
        print(i)
    await asyncio.sleep(random.randint(1,3))
    print("End listing of integers")
async def main():
    print("Start of asynchronous process")
    all_task = await asyncio.gather(list_integers())
    print(all_task)
start_2 = time.time()
asyncio.run(main())
print("End of asynchronous process")
print(time.time()-start_2)