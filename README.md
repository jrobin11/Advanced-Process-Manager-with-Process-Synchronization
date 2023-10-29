# Advanced Process Manager with Process Synchronization

## Introduction

This endeavor seeks to craft a sophisticated Process Manager tailored for emphasizing synchronization. It aims to empower users with capabilities to spawn, oversee, and harmonize processes within a setting that champions multi-threading. The suite offers a CLI (or optionally, a GUI) interface, heavily anchored on system calls pertinent to process and thread orchestration.

## Capabilities

### Creation of Processes:
- Facilitate the genesis of new processes.
- Leverage system calls, notably fork and exec, for process origination.

### Overseeing Processes:
- Engineer features to catalog, cease, and scrutinize active processes.
- Grant users the privilege to access metadata of processes such as PID, progenitor PID, and current status.

### Threading:
- Augment the Manager to champion multi-threading per process.
- Architect mechanisms for thread initiation, cessation, and harmonization.
- Resort to system calls, particularly pthread_create, mutexes, and semaphores for threading activities.

### Communication Across Processes (IPC):
- Designate IPC channels for threads and processes to exchange information.
- Delve into modalities like message relays, collective memory, or pipeline structures for IPC.
- Employ system calls like pipe, msgget, and shmget for IPC undertakings.

### Harmonizing Processes:
- Design and integrate primitives such as mutexes and semaphores for synchronization.
- Exhibit the prowess of these mechanisms by tackling classic synchronization challenges, including scenarios like producer-consumer and reader-writer.

### User Interface (Choose between CLI or GUI):
- Sculpt an intuitive platform for users to engage with the Process Manager.
- Enable functionalities to spawn processes and threads, synchronize them, and manage IPC tasks.
- Ensure the command structure is lucid with comprehensive options.

### Monitoring and Documentation:
- Introduce features for vigilant monitoring and systematic logging of processes and threads in action.
- Record pivotal events, anomalies, and data linked to process synchronization.

## Skills to Acquire

Embarking on this journey, you stand to:
- Master the art of process and thread manipulation.
- Harness the power of system calls to navigate and control processes and threads.
- Cultivate the knack for developing robust software, minimizing system resource contention.

## Project Artifacts

- **Codebase:** The repository will house the thoroughly commented source code, be it in Python (.py) or C (.c).
  
- **Analysis Report:** This documentation will encapsulate:
  - Name of the project
  - A summary of features
  - Installation and user guide
  - Detailed test outcomes with visuals and dissections
  - Reflective discussions on outcomes and insights

- **GitHub Linkage:** The analysis report will find its place as a README (formatted in Markdown as readme.md) in the GitHub repository, with the source code residing separately.

For a complete submission, please share the GitHub repository link housing all the delineated artifacts.
