# Day 75: Multithreading

## Concept
Multithreading allows Python programs to run **multiple tasks at the same time** (concurrently).  
The `threading` module provides a way to create and manage threads.

## Why Multithreading?
- Run multiple tasks without waiting for one to finish  
- Useful for **I/O-bound tasks** (like downloading files, reading/writing)  
- Improves program efficiency  

## Basic Terminology
- **Thread**: Smallest unit of execution  
- **Main thread**: Default thread of a program  
- **Daemon thread**: Background thread that stops when main thread ends  

## Creating Threads

1. Import `threading` module  
2. Define a function for the task  
3. Create a `Thread` object  
4. Start the thread  

### Use Cases
* Download multiple files at the same time
* Handle multiple user requests in a server
* Real-time data fetching
* GUI applications
### Why Learn Multithreading?
* Essential for I/O-bound optimization
* Frequently used in automation, web scraping, and server apps