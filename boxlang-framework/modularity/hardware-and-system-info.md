---
description: This module allows you to interact with hardware and the operating system.
icon: microchip
---

# OSHI - Operating System + Hardware

### Welcome to BoxLang OSHI

This module is based on the great work of the [`oshi` library](https://github.com/oshi/oshi?tab=readme-ov-file#documentation). You can use this module to get information about the operating system and hardware of your machine. This is a great way to get sensor or embedded system information like batteries, Raspberry Pi, etc.

> OSHI is a free JNA-based (native) Operating System and Hardware Information library for Java. It does not require the installation of any additional native libraries and aims to provide a cross-platform implementation to retrieve system information, such as OS version, processes, memory and CPU usage, disks and partitions, devices, sensors, etc.

{% @github-files/github-code-block url="https://github.com/oshi/oshi" %}

{% embed url="https://www.oshi.ooo/oshi-core-java11/apidocs/com.github.oshi/oshi/package-summary.html" %}

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-oshi

# Using CommandBox to install for web servers.
box install bx-oshi
```

### Supported Features

* Computer System and firmware, baseboard
* Operating System and Version/Build
* Physical (core) and Logical (hyperthreaded) CPUs, processor groups, NUMA nodes
* System and per-processor load, usage tick counters, interrupts, uptime
* Process uptime, CPU, memory usage, user/group, command line args, thread details
* Physical and virtual memory used/available
* Mounted filesystems (type, usable and total space, options, reads and writes)
* Disk drives (model, serial, size, reads and writes) and partitions
* Network interfaces (IPs, bandwidth in/out), network parameters, TCP/UDP statistics
* Battery state (% capacity, time remaining, power usage stats)
* USB Devices
* Connected displays (with EDID info), graphics and audio cards
* Sensors (temperature, fan speeds, voltage) on some hardware

### Contributed Functions

Here are the contributed functions in this module:

* `getSystemInfo()` : Get the main entry point for the OSHI system: https://www.oshi.ooo/oshi-core-java11/apidocs/com.github.oshi/oshi/SystemInfo.html
* `getOperatingSystem()` : Get the Operating System information: https://www.oshi.ooo/oshi-core-java11/apidocs/com.github.oshi/oshi/software/os/OperatingSystem.html
* `getHardware()` : Get the Hardware information: https://www.oshi.ooo/oshi-core-java11/apidocs/com.github.oshi/oshi/hardware/HardwareAbstractionLayer.html

The following are also contributed functions provided by convenience:

* `getCpuUsage( [interval] )` : Gets the CPU usage of the system with a custom interval
* `getFreeSpace( path )` : Gets the free space of a drive
* `getTotalSpace( path )` : Gets the total space of a drive
* `getSystemFreeMemory()` : Gets the free memory of the operating system
* `getSystemTotalMemory()` : Gets the total memory of the operating system
* `getJVMFreeMemory()` : Gets the free memory of the JVM
* `getJVMTotalMemory()` : Gets the total memory of the JVM

Please note that you can get a lot more information by having access to the hardware and operating system. Please visit the OSHI documentation for more details: [https://www.oshi.ooo/oshi-core-java11/apidocs/com.github.oshi/oshi/package-summary.html](https://www.oshi.ooo/oshi-core-java11/apidocs/com.github.oshi/oshi/package-summary.html)

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-oshi) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27026\&issuetype=1).
