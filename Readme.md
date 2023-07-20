# Chapter 7.3 Exercises: Asynchronous Programming

These exercises require python 3.10 or higher.
To run the demo code from the lecture, you need to install the packages from the requirements.txt in the root folder of this repository.

## Exercise 0:
Get the code shown in the lecture and try to understand it.
Start by comparing `web_api_demo_0.py` with `web_api_demo_3.py`.
What changed and how why? You can follow the code development in the lecture starting from `web_api_demo_0.py` to `web_api_demo_3.py`.

Now, think back to the lecture and start out at `web_api_demo_0.py` and try to transform the program to the non blocking asynchronous version yourself.

## Exercise 1: web page downloader

This is just like in the lectures. For this, see the code in the folder lectures.
Write a program that downloads the content of multiple web pages concurrently using `async` and `await`.
The program should take a list of URLs as input and retrieve the content of each URL using asynchronous requests.
Once all the web pages are downloaded, print the length of the html files.

## Exercise 2: await syntax with threads

Check out the wrapper function function ```async_http_get_random_chuck``` from the utils.py file from the lecture.
Check out what the function does and check exactly what the use of ascynio.to_thread does in this case.

```python
import asyncio
asyncio.to_thread(func, *args, **kwargs)
```

## Exercise 3: Pitfalls

In case you don't remember from the last lectures, here is a short recap of what a deadlocks and a race condition is.

### Deadlock
A deadlock is a situation in concurrent programming where two or more processes or threads are unable to proceed because each is waiting for the other to release a resource or complete a task.
In other words, it's a state where processes or threads become stuck indefinitely, leading to a halt in the execution of a program.

### Race condition
A race condition is a situation in concurrent programming where the behavior or outcome of a program depends on the relative timing or interleaving of multiple concurrent operations.
It arises when two or more threads or processes access shared data or resources in an uncoordinated manner, leading to unpredictable results.

### Create a simple python program, that creates a deadlock?

Under what conditions does this happen?
How would we avoid this?

### Can you create a simple python program, that creates a race condition?

Under what conditions does this happen?
How would we avoid this?

## Exercise 4: Blocking to non blocking GUI

There is a simple `tkinter`-based GUI program in the file `blocking_gui.py`.
Once you press the button "Calculate Sync" you can see, that the animation on top freezes.
This is GUI element is blocked by the calculation and updating the other part of the GUI.

Change the program, so that the GUI is not blocked anymore.

For this create a second button and link it with a non blocking version of the ```calculate_sync``` function.
Do this using asycnio.
Remember to use `asyncio` to run the program and that only async functions can be awaited.

Bonus: Use asyncio to slow down the animation at the top of the GUI

## Cheat sheet:
```python
import asyncio

async def my_async_func(): # define native coroutine that can be run on the even loop
	await asyncio.sleep(5) # suspend code execution, yield away control to the event loop

asyncio.run() # run asynchronous program

task = asyncio.create_task(my_async_func()) # create a task and submit it to the eventloop
await task # await task, code does not run beyond this point unless task is completed

asyncio.gather([my_async_func(), my_async_func()]) # create multiple tasks which can be awaited 
```