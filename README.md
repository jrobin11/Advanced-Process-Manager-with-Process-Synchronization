# Advanced Process Manager with Process Synchronization

## Project Overview

This project's primary objective is to architect and bring to life an enhanced Task Controller that prioritizes task synchronization. This solution lets individuals establish, oversee, and synchronize tasks in an environment riddled with multiple threads. Moreover, it boasts a CLI (Command-Line Interface) for task creation, oversight, and synchronization. Underneath, the system leans on system calls to direct both tasks and threads.

## Implemented Functionalities
This Process Manager project includes the following functionalities:
1. Task Establishment
2. Overseeing Tasks (Overview, Halting, and Supervision)
3. Thread Features (Spawning Threads and Overview)
4. Task-to-Task Communication (T2T)
5. Task Syncing (Supply-Demand Problem)
6. Command-Line Operations (CLO)
7. Documentation and Analysis

## Installation Direction and Requirements
1. **Install Python 3.11.6 from the official Python website**: [Python Downloads](https://www.python.org/downloads/release/).

2. **Clone the repository and cd into it**:
   ```bash
      git clone https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization.git
      cd Advanced-Process-Manager-with-Process-Synchronization
   ```
3. Install psutil
   ``` bash
     pip install psutil
    ```
3. **Create a Virtual Environment** (recommended):
   - On macOS and Linux:
     - Open the Terminal.
     - Navigate to your project directory using the `cd` command.
     - Activate the virtual environment:
       ```bash
       source venv/bin/activate
       ```

## Option Menu

```bash
Options:
1. Create a new process
2. Initiate a new thread
3. View all processes
4. View threads within a process
5. Terminate a process
6. Terminate a thread
7. IPC: Send message to child processes
8. IPC: Fetch message from child process
9. IPC: Queue - Send data
10. IPC: Queue - Receive data
11. Produce an item
12. Signal a child process
13. Non-blocking read from a pipe
14. Wake up a sleeping thread
15. Exit the program
"Enter you choice (1-15)"
```

# Functionality Test with code: Process Creation
##  Procedure
1. Run the Process Manager
2. Select the option to create a new process
3. Enter the process name

## Expected Result
- A new process is created

## Explanation
- User Interaction: A prompt asks the user to input a name for the process.
- Backend Operation: The create_process method initializes a new process. Depending on the environment, this could be done using the fork system call in UNIX-like systems or using process APIs in other systems.
<img width="560" alt="Options" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/463c3059-28e7-438d-8c9a-9d25687a64bf">

# Functionality Test: Initiate New Thread

## Test Description
This test will check to see if the process manager is able to initate a new thread

## Test Procedure
1. Run the Process Manager
2. Enter the new thread name

## Expected Result
- A  thread with the specified name is created
  
## Explanation
- User Interaction: User is prompted to provide a name for the thread.
- Backend Operation: create_thread is called which, depending on the environment, will likely use threading libraries to initialize and start a thread within the current process context.
<img width="561" alt="Screenshot 2023-11-01 at 10 38 17 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/0d303e2d-20a5-490d-acc1-4d148058016d">

## Functionality Test: View all processes and threads within a process
1. Run the Process Manager.
2. Select option 3 to view all process
3. Then select option 4 to view all threads within a processer
   
## Expected Result
- should show all process and thread within a process

## Explanation
- User Interaction: Simply selecting this option.
- Backend Operation: list_processes method fetches a list of all running processes. This could be obtained using system commands or APIs that provide a list of processes.
- User Interaction: User selects the process for which they want to see threads.
- Backend Operation: The list_threads method gets a list of all active threads within the chosen process. Threading libraries or system-specific calls would be used for this.
<img width="554" alt="Screenshot 2023-11-01 at 10 43 30 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/47be0e20-797d-468d-ad9f-0757986505e7">
<img width="430" alt="Screenshot 2023-11-01 at 10 43 42 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/b3ed99e5-e9c5-4d49-a59a-e6f6508f6cad">

# Functionality Test: Thread and process Termination

## Test Description
Will check to see if it can terminate a thread and process

## Test Procedure
1. View all thread and process
2. Select 5 to terminate process
3. Select 6 to terminate thread
4. Enter the PID of the process

## Expected Result
- The specified thread is terminated
- The specified process is terminated

## Explanation
- User Interaction: User provides the Process ID (PID) of the process they want to terminate.
- Backend Operation: terminate_process is called which sends a termination signal to the specified process. Methods like kill can be used in UNIX-like systems.
- User Interaction: User specifies the thread name they want to stop.
- Backend Operation: terminate_thread method stops the particular thread using appropriate threading libraries or system calls.
<img width="539" alt="Screenshot 2023-11-01 at 10 46 55 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/2ae41e23-4c66-4432-913e-6772c6ed0fb6">
<img width="409" alt="Screenshot 2023-11-01 at 10 47 14 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/d2e6f958-7e39-40c6-b2a7-dbafaa38f29e">
<img width="432" alt="Screenshot 2023-11-01 at 10 47 44 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/62d7b758-0c40-4bc7-b27b-bd59a9eb5d51">
<img width="370" alt="Screenshot 2023-11-01 at 10 47 59 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/7cc98f73-37bf-4818-a5e3-3e9dcd7ea52e">


# Functionality Test: IPC - Send message to child process and fetch message from child process

## Test Description
Will check to see if IPC sends message to child process

## Test Procedure
1. Select 7 to send message
2. Select 8 to check if message sent

## Expected Result
- The message will appear
  
## Explanation
User Interaction: User chooses among sending/receiving messages or data.
- Backend Operations:
- send_message and receive_message are for message-based communication between processes. This might be implemented using message queues.
- send_data and receive_data methods are for sending and receiving data, perhaps through pipes or shared memory.
<img width="650" alt="Screenshot 2023-11-01 at 10 51 26 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/ea49646a-bdf0-4c7c-97a7-6c0edad013a9">
<img width="487" alt="Screenshot 2023-11-01 at 10 51 36 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/5b9a39ab-a159-4af1-919e-487bade447bf">

# Functionality Test: IPC: Queue - Send data and receive Data

## Test Description
Will check if IPC queue sends data and receives it

## Test Procedure
1. Select 9 to send data
2. Select 10 to receive the data that was sent

## Expected Result
- The data was sent
- The data displayed

## Explanation
This test validates the Process Manager's ability to send messages between processes using IPC. It uses named pipes (FIFOs) for inter-process communication and non-blocking reads to receive messages.

<img width="283" alt="Screenshot 2023-11-01 at 10 54 13 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/81d25db7-d853-479e-886b-088976be05c9">
<img width="351" alt="Screenshot 2023-11-01 at 10 54 29 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/62f1f4a6-11cf-46ed-a02a-63f049a764fa">

# Functionality Test: Produce an item

## Test Description
will check to see if a item can be produced
## Test Procedure:
1. Select 11
2. Pick option 1 to produce

## Expected Result
- It will produce an item

## Explanation
- User Interaction: Simply selecting this option.
- Backend Operation: An item (data) is produced and stored in a buffer. This simulates the producer side of the producer-consumer problem.
<img width="331" alt="Screenshot 2023-11-01 at 10 55 55 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/679df88a-39b9-4a60-8df1-955696beab0c">

# Functionality Test: Signal a child process

## Test Description
Will check to see if a child process can be signaled

## Test Procedure
1. Select 12
2. Enter the PID of the child process

## Expected Result
- It should send a signal to the child process

## Explanation
- User Interaction: User specifies which child process to signal.
- Backend Operation: A signal (like SIGUSR1) is sent to the specified child process. This might be used to inform or interrupt the child process.
<img width="438" alt="Screenshot 2023-11-01 at 11 00 44 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/9d1d06ef-44e9-432b-81dc-17d6514b4223">

# Functionality Test: Non-blocking read from a pipe

## Test Description
Will check Non-blocking readings from a pipe

## Test Procedure
1. Select 13

## Expected Result
- It should return the readings from the pipe

## Explanation
- User Interaction: Simply selecting this option.
- Backend Operation: An attempt is made to read a message from a pipe. If the pipe is empty, the function returns immediately without blocking.
<img width="278" alt="Screenshot 2023-11-01 at 11 03 47 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/9862d228-d441-4d51-b6a5-62f5f84161fb">

# Functionality Test: Wake up a sleeping thread

## Test Description
- Will wake up a thread

## Test Procedure
1. Select 14
2. Enter the name of the thread that you want to wake up

## Expected Result
- It should wake up the thread

## Explanation
- User Interaction: This option is not yet implemented.
- Backend Operation: In the future, this would likely involve sending a signal or using some threading library call to wake up a specified thread that's currently in a sleep or wait state.
<img width="438" alt="Screenshot 2023-11-01 at 11 05 13 PM" src="https://github.com/jrobin11/Advanced-Process-Manager-with-Process-Synchronization/assets/73866458/16cb2299-6ddf-46fa-86ce-f6f0977d2b90">


# Documentation and Records

The Advanced Process Manager leverages detailed documentation mechanisms to record pertinent information regarding processes, threads, inter-process interactions, and synchronization incidents. This documented data is stored in `processes.log`.

## Documentation Insights

- **Initiation of Process and Threads: On the creation of any process or thread, specifics like process ID (PID), thread ID (TID), name, and current status are diligently noted in the log.

- **Thread Conclusion: On the event of a thread's cessation, the log captures the activity, taking note of the ceased thread's name.

- **Inter-Process Interactions (IPC): Every IPC message is logged with details of the sender process, receiver process, and the content of the message. This gives a thorough overview of IPC undertakings within the Process Manager.

- **Synchronization Process (Producer-Consumer): Instances in the producer-consumer scenario, be it the generation or use of items, are chronicled to show the synchronization dynamics between producing and consuming threads.

- **Cataloging Processes and Threads: Logs capture details of processes and threads, irrespective of whether they are derived from the script or are from the system-wide list.

- **Log Reset: A "Clear log file" function is present, facilitating a fresh start for subsequent log sessions.

## Review and Study

The log file, `processes.log`, stands as an instrumental resource in scrutinizing the behaviors of processes and threads, rectifying anomalies, and grasping the synchronization facets within the Process Manager. It's a gateway for users to revisit previous operations, dissect discrepancies, and chronologically follow events across individual and multi-threaded modules.
## Accessing the Log File

The `processes.log` file is created in the root directory of the Process Manager project. Users can access this file to view and analyze the logged information.

### Retrieving the Log Data
`processes.log` is anchored in the primary directory of the Process Manager initiative. Users can delve into this log for insights.

```
Advanced-Process-Manager/
├── processes.log
├── ...
```
# Overview
- The Advanced Process Manager exemplifies a thorough and intricate platform for overseeing processes and threads within multi-threaded configurations. This section delves into the core achievements of the project, spanning its functionalities, structural design, and the wider reach of its potential.

## Holistic Capabilities
- The platform adeptly facilitates the inception of fresh processes, granting each its unique interactional menu. Such a granular approach to process initiation augments the system's capacity to handle diverse operations or services. A suite of controls, from listing to terminating processes, accentuates governance over these modules.

## Thread Integration
- Embedding threads within processes amplifies the functional spectrum of the project. This integration exemplifies the adeptness to manage applications running multiple threads, potentially seeding more intricate computational tasks. The finesse in initiating and concluding threads elucidates the Process Manager's authoritative command over them.

## Inter-Process Dialogue (IPC)
- The inclusion of IPC, sanctioning communication amongst processes, stands out as an invaluable asset. This champions cohesive operations and data sharing across processes. Especially in expansive and networked systems, IPC's relevance escalates, and this utility underscores its practicality.

## Synchronized Operations
- A standout element within the project is the portrayal of process synchronization through the Producer-Consumer paradigm. By emulating real-world synchronization hurdles, the prowess of the Process Manager in directing intricate thread interplays comes to the fore. Semaphore-oriented synchronization guarantees singular thread access to communal resources, an elemental tenet in concurrent computing.

## Documentation and Insights
- Integrating a meticulous documentation system, where all relevant actions are penned in processes.log, boosts the project's traceability and clarity. This document offers a historical overview, aiding in troubleshooting, efficiency analytics, and deriving systemic insights. The "Log Reset" function equips users to commence fresh logging sessions, upholding log purity.

## Applicability in Practical Scenarios
Beyond being a conceptual showcase, the Advanced Process Manager manifests as a pragmatic instrument. Its versatility spans:
- System Governance: Offering a panoramic view of all active processes, it aids administrators in system supervision.
- Concurrent Computations: With its affinity for multi-threaded applications and IPC, it's pivotal in concurrent computing where tasks are parallelized for enhanced efficiency.
- Networked Architectures: In systems spread across machines, IPC's role is indispensable.
- Educative Resource: It can double up as an instructive asset, elucidating process governance and synchronization tenets.

## Future Expansions
Despite the Advanced Process Manager's formidable suite of tools, there's an expansive horizon for augmentation:
- Augmented IPC: Enriching IPC with evolved communication paradigms such as shared memory or messaging queues.
- User Experience: Sculpting a graphical user interface (GUI) for an intuitive user journey.
- Resource Surveillance: Integrating monitors for resources like CPU or memory will be invaluable for administrative oversight.

## Summary

The Advanced Process Manager stands as a robust platform, proficient in process governance, thread management, IPC, and synchronized operations. Beyond its functionality, it embodies the essence of process governance and synchronization philosophies. The rigorous documentation ensures a transparent and accountable system experience. The foundation laid by this initiative primes it for further evolutionary strides in process governance and concurrent computational utilities, promising to cater to administrators, coders, and educators alike.
