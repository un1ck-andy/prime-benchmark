# Benchmarking Prime Number Generators
## Brute Force vs Sieve of Eratosthenes
## Parallel benchmark tests of algorithms to compute prime numbers

## How to run:
`python main.py -n NUMBER`
options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        the maximum value to which the calculation will be carried out

Usage example:
`python main.py -n 100`

## Few comments:
1. I used generators for prime numbers to save memory and because the task was literally to compare generators.
2. I used parallel processes, not threads. The example in the task tells to use 'threads' for parallel running, but threads in Java and Python work very differently because of Global Interpreter Lock, which is in Python and is absent in Java. In fact, multithreading in python doesn't allow the utilization of multiple cores, so I used multiprocessing, which allows it to run in parallel. I used concurrent.futures library, so it can be easily switched between multithreading and multiprocessing just by replacing `concurrent.futures.ProcessPoolExecutor()` with `concurrent.futures.ThreadPoolExecutor()` on line 50 on main.py.
3. The structure is a bit overkill, as well as usage of poetry here, but I wanted to show my regular workflow.
4. I used pre-commit hook to run linters and formaters before upload.

## Follow-up Questions:
1. Is there any measurable difference between the two algorithms for small values of N?
It depends on the hardware and what we count 'small' values. On my machine, there is a measurable difference when N is around 20, but we are talking about 0.000001 seconds. With a smaller N on my machine, the execution time is practically equal (within the margin of error).

2. Approximately at what value of N, if any, does the performance gap become significant?
If you use N=20, the performance gap is ~20%, but it's still 0.000001 seconds, so if this algo is used for one end user - they won't see any difference. With N=30,000, the Sieve algo is still nearly instant (0.003 s), while brute force takes 1.25 s, which is already being felt. With N=1,000,000 the Sieve algo took 0.15s, while brute force 1141s (19min, I was curious) it’s a 76000 times difference.
Again, when we talk about something that is I/O dependent, especially networks with its latency, the difference may not be seen by the end user. But when making an app with thousands or even millions of such operations, you should look at Big O, not at the absolute fractions of a second.

3. Do you think it was a good idea to benchmark the two algorithms in parallel? Why or why not?
It depends on the task and the hardware. A parallel run is a must with I/O dependant tasks, like reading/writing to disk or network, when waiting for the response could take a lot of time. A parallel run reduces the total execution time literally times in the number of such parallel processes. These algorithms are not I/O dependent, they fully utilize the CPU for calculations. If the CPU has enough idling cores, these tasks won't affect each other. For example, 4 core CPU can run these 2 algorithms in parallel easily without interfering with each other. If there were 4 algorithms on 2 core CPUs, they would interfere with each other, and the result will be different from a non-parallel run (slower). 

P.S. Threads are not the same as cores, so 2 core/4thread CPU is far from 4c/4t of the same architecture, but still is about 30% faster in multitasking than 2c/2t. Also, you should consider the overhead of multitasking and the resources needed for the OS itself.

4. In general, does it always make sense to use the algorithms with the best O(n) performance in our code? Describe some scenarios where it could make sense to choose a slower algorithm.
I should mention that O(n) is not the best performance, there is O(log n) or even O(1). Also, when we talk about performance, we should mention Big Omega and Big Theta notations, as well as memory usage (that is where generators come in handy).
If you're a perfectionist, you would love to use an algorithm with maximum efficiency. But when we are talking about business tasks, you should seek a balance between the cost of development and the cost of execution. So if the benefit of coding a faster algorithm does not bring adequate benefit, then it is better to abandon it in favor of a simpler implementation. Optimizing a not-very-important task for fractions of a millisecond requires hundreds of person-hours of work is obviously not justified. 
Basically, it takes more time (and development time = money) to implement a more complicated but more efficient algorithm and vice versa. It is a demanding manager choice each time. I love the Agile philosophy, and I try to always bring things to a state of minimum value product (MVP), then see what can be improved, and most importantly, whether or not this improvement will benefit clients and the company than doing another task.The general rule is that there is always a limit, a bottleneck, by directing the effort to which you can achieve a significant effect. I am a fan of Goldratt's theory of constraints not only in my work but also in my personal life. When writing code, of course, you should always try to calculate what the Big O will be and prefer more productive algorithms. Also, the code should be as clear as possible to make it easier to find the bottleneck. 

P.S. It was interesting for me to have a retrospective look at on how approaches to programming periodically changed. At first programs were written in low-level languages, squeezing the maximum out of weak processors and available kilobytes of memory. Then, by all the laws of Moore, productivity doubled every year, and the development time began to be more precious than execution time, so we came to more high-level languages (and less polished solutions). A top computer from 2005 today is not powerful enough to run a modern browser and even the basic tasks of the typewriter. But once upon a time, a spaceship to the moon was driven by a chip with 4kb of memory and a frequency of 512kHz...
Now begins the boom of the IoT, which also has limited memory and processor, and therefore, in my opinion, the need for more accurate and efficient programming will increase.