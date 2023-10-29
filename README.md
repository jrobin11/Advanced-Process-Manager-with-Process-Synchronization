# Advanced Process Manager with Process Synchronization

## Project Overview

The goal of this project is to design and implement an advanced Process Manager with an emphasis on process synchronization. This Process Manager will allow users to create, manage, and synchronize processes in a multi-threaded environment. It will provide a command-line interface for process creation, management, and synchronization, and it will use system calls for process and thread control.

## Required Functionalities

### Process Creation:
- Implement a process creation mechanism that allows users to create new processes.
- Use system calls (e.g., fork, exec) for process creation.

### Process Management:
- Develop functionalities to list, terminate, and monitor running processes.
- Allow users to view information about each process, such as its process ID (PID), parent process ID, and state.

### Thread Support:
- Extend the Process Manager to support multiple threads within a process.
- Implement thread creation, termination, and synchronization mechanisms.
- Use system calls for thread creation (e.g., pthread_create) and synchronization (e.g., mutexes, semaphores).

### Inter-Process Communication (IPC):
- Implement IPC mechanisms to allow processes and threads to communicate and share data.
- Explore methods like message passing, shared memory, or pipes for IPC.
- Use system calls for IPC operations (e.g., pipe, msgget, shmget).

### Process Synchronization:
- Implement synchronization primitives such as mutexes and semaphores.
- Demonstrate the use of synchronization mechanisms to solve common synchronization problems (e.g., producer-consumer, reader-writer).

### Command-Line Interface (CLI) or Graphic User Interface (GUI):
- Develop a user-friendly interface for interacting with the Process Manager.
- Allow users to create processes, create threads, synchronize threads, and perform IPC operations.
- Provide clear and informative command syntax and options.

### Logging and Reporting:
- Implement logging and reporting features to track and display the execution of processes and threads.
- Log significant events, errors, and information related to process synchronization.

## Expected Skills Gained

By working on this project, you will gain the following skills:
- Manipulating processes and threads in various aspects.
- Exploiting system calls to manipulate processes and threads to achieve specific goals.
- Developing software that operates reliably while reducing conflicts in using system resources.

## Deliverables

- **Source Code:** Provide the source code, including comments explaining the design and implementation, as a Python (.py) or C (.c) file uploaded to GitHub.

- **Project Report:** Include a project report with the following:
  - Project title
  - List of implemented functionalities
  - Description of how to install and use the application
  - Test results for each functionality, accompanied by figures and explanations
  - Discussion on the project results

- **GitHub Repository Link:** The project report should be included as a README file (Markdown format, readme.md) within the GitHub repository. The source code should be loaded as a separate file.

Please submit your project via a GitHub Repository link that contains the above deliverables.
