# Advanced-Process-Manager-with-Process-Synchronization
Enhanced Task Coordinator with Concurrent Operations Support

Project Brief

This project aims to architect and bring to life a Sophisticated Task Supervisor centered around concurrent operations. This system will empower users to spawn, oversee, and synchronize tasks in a multi-threaded context. It's designed to provide a command-line interface (or optionally a GUI) for task initiation, administration, and synchronization, leveraging system calls for the supervision of tasks and threads.
Essential Features:

    Task Initiation:
        Devise a mechanism enabling users to spawn new tasks.
        Employ system calls, notably fork and exec, for task inception.

    Task Administration:
        Integrate capabilities to enumerate, conclude, and surveil active tasks.
        Facilitate users to inspect details like Task ID, the initiating Task ID, and its current status.

    Threaded Integration:
        Broaden the Task Supervisor to back multiple threads within a single task.
        Facilitate mechanisms for thread initiation, conclusion, and concurrent regulation.
        Leverage system calls like pthread_create for thread initiation and tools like mutexes and semaphores for synchronization.

    Task-to-Task Relay (T2R):
        Roll out mechanisms for tasks and threads to engage and relay information.
        Investigate methods like data messaging, shared memory realms, or conduits for T2R.
        Employ system calls, such as pipe, msgget, and shmget, to facilitate T2R operations.

    Task Synchronization:
        Integrate concurrent control tools, notably mutexes and semaphores.
        Showcase the application of these tools to address standard synchronization challenges (e.g., supply-demand dynamics, reader-publisher scenarios).

    User Interface (CLI/GUI):
        Craft an intuitive interface for the Sophisticated Task Supervisor.
        Enable users to initiate tasks, spawn threads, synchronize them, and execute T2R operations.
        Offer lucid command structures and directives.

    Event Documentation & Analysis:
        Embed tools to log and review the behavior of tasks and threads.
        Chronicle crucial events, anomalies, and concurrent operation data.

Proficiencies To Be Acquired:

Through this venture, participants will:

    Master the nuances of supervising tasks and threads across varied operations.
    Develop aptitude in utilizing system calls to modulate tasks and threads aligned with objectives.
    Gain proficiency in crafting software that performs seamlessly, ensuring minimized resource contention.

Submission Requisites:

    Codebase: The fully annotated source code, available as a Python (.py) or C (.c) file on GitHub.
    Project Synopsis: This includes:
        Initiative's title
        Catalog of realized features
        Installation and usage guidelines
        Empirical evaluations for every feature, enriched with illustrations and narratives
        Reflections and insights on project findings
    GitHub Repository: The project synopsis should be represented as a README (markdown format) with the source code maintained separately.
