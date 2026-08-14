# Day 76: Multiprocessing

## Concept
Multiprocessing allows Python programs to run **CPU-heavy tasks in parallel** by using multiple processes.  
Unlike multithreading, multiprocessing bypasses Python's GIL and utilizes multiple CPU cores.

## Why Multiprocessing?
- Run CPU-intensive tasks faster  
- Each process has its **own memory space**  
- Avoids Global Interpreter Lock (GIL) limitations  
- Useful for data processing, image/video processing, simulations  

## Basic Terminology
- **Process**: Independent execution unit with separate memory  
- **Pool**: Manage multiple processes efficiently  
- **GIL**: Global Interpreter Lock, limits threads but not processes  

## Creating Processes
1. Import `multiprocessing` module  
2. Define a function for the task  
3. Create a `Process` object  
4. Start the process  

### Use Cases
* Data processing (large datasets)
* Image or video processing
* Scientific computations
* Simulation tasks
### Why Learn Multiprocessing?
* Improve CPU-bound program performance
* Essential for data-intensive applications
* Complements multithreading for mixed workloads