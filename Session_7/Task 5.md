#### What is Fragmentation ?

- Fragmentation refers to the phenomenon in computer systems where available memory or storage space becomes divided into smaller, non-contiguous blocks, leading to inefficiencies in resource utilization and performance degradation. Fragmentation can occur in both memory (RAM) and storage (disk) contexts. There are two main types of fragmentation: memory fragmentation and disk fragmentation. \

  ## Extenal Fragmentation :

  - This occurs when free memory blocks are scattered throughout the memory space, leaving small gaps that are individually too small to be useful for memory allocation. Even though there might be sufficient total free memory, the gaps prevent larger programs or data from being loaded.

  ## Internal Fragmentation :

  - This occurs when allocated memory blocks are larger than the actual amount of data they hold. As a result, there is unused space within allocated memory blocks. This is particularly common in memory allocation strategies that allocate memory in fixed-size blocks, leading to wasted memory.
