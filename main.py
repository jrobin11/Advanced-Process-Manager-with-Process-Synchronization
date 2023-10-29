# Import necessary libraries and modules
import os
import signal
import sys
import logging
import multiprocessing
import ctypes
import time
import random
import threading
import fcntl
import errno
from enum import Enum
from queue import Queue

# Enum for process state representation
class ProcessState(Enum):
    RUNNING = "RUNNING"
    SLEEPING = "SLEEPING"

# Main ProcessManager class
class ProcessManager:
    def __init__(self):
        # Initializations
        self.running_processes = {}  # Dictionary to store running processes
        self.process_threads = {}    # Dictionary to store threads within processes
        self.threads = []            # List to store all threads
        self.pipe_conn, self.child_conn = multiprocessing.Pipe()  # IPC pipe connections
        self.shared_queue = Queue()  # IPC shared queue
        self.mutex = threading.Semaphore(1)  # Semaphore for mutual exclusion
        self.read_pipe, self.write_pipe = os.pipe()  # Pipes for IPC
        self.buffer = []  # Buffer for producer-consumer problem
        self.empty = threading.Semaphore(5)  # Semaphore indicating empty slots in buffer
        self.filled = threading.Semaphore(0)  # Semaphore indicating filled slots in buffer
        self.setup_logging()  # Initialize logging
        self.read_pipe, self.write_pipe = os.pipe()  # Pipes for IPC

        # Set the read pipe to non-blocking
        flags = fcntl.fcntl(self.read_pipe, fcntl.F_GETFL)
        fcntl.fcntl(self.read_pipe, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    def setup_logging(self):
        # Set up logging configurations
        logging.basicConfig(filename='processes.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        self.process_log = logging.getLogger('processes')
        self.process_log.setLevel(logging.INFO)

    def create_thread(self, thread_name):
        # Create a new thread within the current process
        process_pid = os.getpid()
        thread_id = ctypes.c_long()
        libc = self.get_libc()

        def thread_func():
            # The main function executed by the thread
            self.process_log.info(f"Thread '{thread_name}' running")

        thread_func_ptr = ctypes.CFUNCTYPE(None)(thread_func)
        if libc.pthread_create(ctypes.byref(thread_id), None, thread_func_ptr, None) == 0:
            self.threads.append((thread_id, thread_name))
            self.process_threads.setdefault(process_pid, []).append((thread_id, thread_name))
            self.process_log.info(f"Thread '{thread_name}' created successfully")
        else:
            self.process_log.error("Failed to create thread")

    @staticmethod
    def get_libc():
        # Get appropriate C library based on the platform
        if sys.platform.startswith('win'):
            return ctypes.CDLL('msvcrt')
        elif sys.platform.startswith('linux'):
            return ctypes.CDLL('libc')
        elif sys.platform == 'darwin':
            return ctypes.CDLL('libc.dylib')
        else:
            raise OSError("Unsupported platform")

    def list_threads(self):
        # List threads within the current process
        process_pid = os.getpid()
        threads = self.process_threads.get(process_pid, [])
        if not threads:
            print("No threads in this process.")
        else:
            print("Threads in this process:")
            for thread_id, thread_name in threads:
                print(f"Thread ID: {thread_id}, Name: {thread_name}")

    def create_process(self, process_name):
        # Create a new child process
        pid = os.fork()
        if pid == 0:
            # Child process code
            self.state = ProcessState.RUNNING
            self.parent_pid = os.getppid()
            try:
                os.execlp(process_name, process_name)
            except Exception as e:
                self.process_log.error(
                    f"Child process '{process_name}' with PID {os.getpid()} encountered an error: {str(e)}")
                self.state = ProcessState.SLEEPING
            os._exit(1)
        else:
            with self.mutex:
                # Store process information
                self.running_processes[pid] = {"name": process_name, "state": ProcessState.RUNNING,
                                               "parent_id": os.getpid()}
            self.process_log.info(f"Child process '{process_name}' with PID {pid} created.")

    def list_processes(self):
        # List all running processes
        if not self.running_processes:
            print("No running processes.")
        else:
            print("Running processes:")
            for pid, process_info in self.running_processes.items():
                print(
                    f"PID: {pid}, Name: {process_info['name']}, State: {process_info['state'].value}, Parent PID: {process_info['parent_id']}")

    def producer(self):
        # Produce an item for the producer-consumer problem
        item = random.randint(1, 100)
        self.empty.acquire()
        self.buffer.append(item)
        self.filled.release()
        print(f"Produced item: {item}")
        self.process_log.info(f"Produced item: {item}")

    def consumer(self):
        # Consume an item for the producer-consumer problem
        self.filled.acquire()
        item = self.buffer.pop(0)
        self.empty.release()
        print(f"Consumed item: {item}")
        self.process_log.info(f"Consumed item: {item}")

    def terminate_process(self):
        # Terminate a specified process
        pid = int(input("\nEnter the PID of the process to terminate: "))
        if pid in self.running_processes:
            try:
                os.kill(pid, signal.SIGTERM)
                del self.running_processes[pid]
                print(f"Process with PID {pid} terminated.")
            except Exception as e:
                print(f"Failed to terminate the process with PID {pid}. Error: {e}")
        else:
            print(f"No process found with PID {pid}")

    def terminate_thread(self):
        # Terminate a specified thread
        thread_name = input("\nEnter the thread name to terminate: ")
        thread_tuple = next((t for t in self.threads if t[1] == thread_name), None)
        if thread_tuple:
            # Terminate the thread using ctypes
            libc = self.get_libc()
            retval = libc.pthread_cancel(thread_tuple[0])
            if retval == 0:
                self.threads.remove(thread_tuple)
                print(f"Thread '{thread_name}' terminated.")
            else:
                print(f"Failed to terminate thread '{thread_name}'")
        else:
            print(f"No thread found with name {thread_name}")

    def send_message(self):
        # Send a message to child processes through IPC
        message = input("Enter the message to send to the child processes: ")
        self.pipe_conn.send(message)

    def receive_message(self, timeout=5):
        # Receive message from child processes with a specified timeout
        start_time = time.time()
        while True:
            if self.child_conn.poll(0.5):  # Check every half second
                print(f"Received message from child: {self.child_conn.recv()}")
                break
            elif time.time() - start_time > timeout:
                print("No message received within the timeout period.")
                break

    def send_data(self):
        # Send data using a shared queue (IPC mechanism)
        data = random.randint(1, 100)
        self.shared_queue.put(data)
        print(f"Sent data: {data}")

    def receive_data(self):
        # Receive data using a shared queue (IPC mechanism)
        if not self.shared_queue.empty():
            print(f"Received data: {self.shared_queue.get()}")
        else:
            print("No data available to receive.")

    def producer_consumer_demo(self):
        choice = int(input("\n1. Produce\n2. Consume\nEnter your choice: "))
        if choice == 1:
            self.producer()
        elif choice == 2:
            self.consumer()

    def signal_child_process(self):
        pid = int(input("Enter the PID of the child process: "))
        if pid in self.running_processes:
            os.kill(pid, signal.SIGUSR1)
            print(f"Signal sent to child process with PID {pid}")
        else:
            print(f"No process found with PID {pid}")

    def non_blocking_read(self):
        try:
            message = os.read(self.read_pipe, 1024).decode('utf-8')
            print(f"Message received: {message}")
        except OSError as e:
            if e.errno == errno.EAGAIN or e.errno == errno.EWOULDBLOCK:
                print("No message available")
                return
            raise e

    def wake_up_thread(self):
        thread_name = input("Enter the name of the thread to wake up: ")
        thread_tuple = next((t for t in self.threads if t[1] == thread_name), None)
        if thread_tuple:
            # TODO: Logic to wake up a sleeping thread
            print(f"Thread '{thread_name}' woken up.")
        else:
            print(f"No thread found with name {thread_name}")

    def run(self):
        while True:
            print("+---------------------------------------------------+")
            print("|                 Process Manager v1.0              |")
            print("|                                                   |")
            print("|    Manage and synchronize processes & threads.    |")
            print("|    Use IPC to communicate between entities.       |")
            print("+---------------------------------------------------+")
            print("  ")
            print("   -> 1.  Create a new process")
            print("   -> 2.  Initiate a new thread")
            print("   -> 3.  View all processes")
            print("   -> 4.  View threads within a process")
            print("   -> 5.  Terminate a process")
            print("   -> 6.  Terminate a thread")
            print("   -> 7.  IPC: Send message to child processes")
            print("   -> 8.  IPC: Fetch message from child process")
            print("   -> 9.  IPC: Queue - Send data")
            print("   -> 10. IPC: Queue - Receive data")
            print("   -> 11. Produce an item")
            print("   -> 12. Signal a child process")
            print("   -> 13. Non-blocking read from a pipe")
            print("   -> 14. Wake up a sleeping thread")
            print("   -> 15. Exit the program")
            choice = input("\nEnter your choice (1-15): ")

            if choice == "1":
                process_name = input("\nEnter the process name: ")
                self.create_process(process_name)
            elif choice == "2":
                thread_name = input("\nEnter the thread name: ")
                self.create_thread(thread_name)
            elif choice == "3":
                print("\n")
                self.list_processes()
            elif choice == "4":
                print("\n")
                self.list_threads()
            elif choice == "5":
                self.terminate_process()
            elif choice == "6":
                self.terminate_thread()
            elif choice == "7":
                self.send_message()
            elif choice == "8":
                self.receive_message()
            elif choice == "9":
                self.send_data()
            elif choice == "10":
                self.receive_data()
            elif choice == "11":
                self.producer_consumer_demo()
            elif choice == "12":
                self.signal_child_process()
            elif choice == "13":
                self.non_blocking_read()
            elif choice == "14":
                self.wake_up_thread()
            elif choice == "15":
                print("\nExited successfully.")
                exit(0)
            else:
                print("\nInvalid option. Try again.")

if __name__ == "__main__":
    manager = ProcessManager()
    manager.run()
