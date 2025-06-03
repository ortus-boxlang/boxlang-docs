---
description: >-
  BoxLang ships with an enterprise Caching Engine and Cache Agnostic API
  Aggregator!
icon: server
---

# Caching

## BoxLang Cache Engine

<figure><img src="../.gitbook/assets/BxCache Overview (1).png" alt=""><figcaption><p>BoxCache Diagram</p></figcaption></figure>

The BoxLang Cache Engine is a high-performance caching solution designed to optimize data retrieval speeds for applications using the BoxLang programming language. By leveraging advanced caching algorithms and memory management techniques, it minimizes latency, enhances scalability, and improves the overall efficiency of data access. Whether handling frequent read operations or reducing server load, the BoxLang Cache Engine serves as an essential component for deploying robust and responsive applications.

## BoxLang Cache Aggregation

<figure><img src="../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

The BoxLang Cache Engine also functions as a powerful cache aggregator. This capability allows it to aggregate various cache providers under a single, unified interface, simplifying the management and operation of caching systems. By providing a centralized API, BoxLang Cache Engine streamlines access to multiple caching solutions, ensuring seamless integration and enhanced flexibility. This feature is particularly beneficial for applications that require a diverse set of caching tactics, as it reduces complexity and boosts overall system coherence.

## Features at a Glance <a href="#features-at-a-glance" id="features-at-a-glance"></a>

* **Cache Aggregator**
  * Ability to aggregate different caching engines via our `ICacheProvider` interface
  * Ability to aggregate different configurations of the same caches
  * Rich aggregation event model
  * Granular logging
* **Fast and Simple to use**
  * Simple API and configuration parameters
  * Small Footprint
* **Solid Core**
  * Multi-Threaded
  * Based on Java Concurrency Classes
  * Multiple [Eviction Policies](http://en.wikipedia.org/wiki/Cache_algorithms): FIFO, LFU, LIFO, LRU, MFU, MRU, Random
  * Memory Management & Memory Sensitive Caching based on [Java Soft References](http://docs.oracle.com/javase/7/docs/api/java/lang/ref/SoftReference.html)
* **Extensible & Flexible**
  * CachelListeners for event broadcasting
  * Create custom eviction policies
  * Create custom cache providers
  * Create custom cache key filters
  * Create custom object storages
* **Highly Configurable**
  * JVM Threshold Checks
  * Object Limits
  * Ability to time-expire objects
  * Eternal (singletons) and time-lived objects
  * Fully configurable at runtime via dynamic configurations and hot updates

## Configuration

The main BoxLang configuration file configures the BoxCache `boxlang.json` which can be found in your `$BOXLANG_HOME/config/boxlang.json`.  You can find all the [documentation about configuration in the caches area](../getting-started/configuration/caches.md).
