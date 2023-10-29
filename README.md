# Advanced-Process-Manager-with-Process-Synchronization
Enhanced Task Coordinator with Concurrent Operations Support
Project Summary

This initiative seeks to devise and craft an Enhanced Task Coordinator focusing on concurrent operations handling. This system aims to empower users to spawn, control, and synchronize tasks within a threaded context. The interface will offer command-line functionalities for task creation, oversight, and synchronization while harnessing the power of system calls for thread and task regulation.
Key Features

    Task Spawning:
        Design a mechanism for users to initiate new tasks.
        Utilize system calls, notably fork and exec, for task inception.

    Task Oversight:
        Incorporate features to display, end, and oversee active tasks.
        Grant users the capability to inspect task attributes, such as Task ID, originating Task ID, and its current status.

    Threaded Operations:
        Augment the Task Coordinator to back multiple threads within a singular task.
        Facilitate thread initiation, ending, and concurrent regulation.
        Harness system calls for thread initiation (like pthread_create) and concurrency (mutexes, semaphores).

    Task-to-Task Dialogue (T2D):
        Roll out T2D strategies for tasks and threads to exchange data and interact.
        Delve into mechanisms like data transfer, communal memory, or conduits for T2D.
        Utilize system calls, such as pipe, msgget, and shmget, for T2D functionalities.

    Task Coordination:
        Introduce concurrent control tools like mutexes and semaphores.
        Exhibit the application of these tools in handling standard synchronization scenarios (e.g., supply-demand, reader-broadcaster).

    User Interface – CLI or GUI:
        Conceive an intuitive interface for engaging with the Task Coordinator.
        Permit functionalities like task initiation, thread generation, thread synchronization, and T2D operations.
        Offer lucid command structures and choices.

    Event Tracking & Analysis:
        Incorporate diagnostic and analytical tools to monitor and showcase task and thread behaviors.
        Chronicle pivotal occurrences, discrepancies, and relevant synchronization data.

Anticipated Acquired Proficiencies

Through this endeavor, participants will:

    Acquire mastery in handling tasks and threads across a spectrum of operations.
    Harness system calls adeptly to modulate tasks and threads in line with set objectives.
    Cultivate the knack to engineer software that functions seamlessly, mitigating clashes over system asset utilization.

Submission Components

    Codebase: Submit thoroughly documented source code, available as a Python (.py) or C (.c) file on GitHub.
    Project Analysis: Append an analytical report incorporating:
        Title of the initiative
        Enumeration of realized features
        Guidelines on installation and software operation
        Empirical data for every feature, enriched with visuals and narratives
        Insights and commentary on project outcomes
    GitHub Repository: Include the analytical report as a README (markdown format) and maintain the source code as distinct entities.
