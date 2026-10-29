# Troubleshoot slow performance

Source: https://documentation.s3ns.fr/filestore/docs/troubleshooting
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/filestore/docs/tpc-differences) for more details.














- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Filestore

](https://documentation.s3ns.fr/filestore/docs)






- 








[

Guides

](https://documentation.s3ns.fr/filestore/docs/overview)












# Troubleshoot slow performance 















This page provides troubleshooting information to help address slow performance
issues you might encounter while using Filestore.

## Slow read or write performance

- 

Ensure that you are using the
[recommended machine type](/filestore/docs/performance#client-machine)
for the client VM.

- 

If your client VM is running Linux, confirm that you're using the
[default mount options](/filestore/docs/performance#linux_client_mount_options).

- 

Ensure that the client VM is located in the same region as the
Filestore instance. Mounting across regions not only reduces
performance, it also incurs a [networking cost](https://documentation.s3ns.fr/vpc/network-pricing).

- 

Ensure that your Filestore instance isn't at or near full
capacity. When capacity is nearly full, any remaining space is highly
fragmented, causing read and write operations to slow down. The amount of
free space needed to avoid this scenario is case-dependent. We recommend
setting up
[low disk space alerts](/filestore/docs/monitoring-instances#low-disk-space).

For more information, see [Troubleshoot capacity issues](/filestore/docs/capacity-issues).

- 

[Test the performance](/filestore/docs/performance#testing_performance)
of your Filestore instance using the `fio` tool.

If the test results show abnormally slow performance, contact your account
representative. If the test results show similar or greater performance than
expected, continue to the next section.

## Use cases that cause slow performance

Here are some use cases and scenarios that cause poor performance:

### Workloads involving high volumes of small files

- 

Filestore file shares use the `sync` export option for data safety
and NFS protocol compliance. For most data-modifying operations, the
Filestore instance waits for the data to be committed to storage
before replying to requests from the client VM. When many files are involved
in an operation, the client makes a long series of synchronous operations
and the cumulative latency adds up.

An example of this scenario is when you extract an archive on the file share,
like tar files. TAR makes many synchronous operations in a series when
extracting an archive containing many files. As a result, performance is
reduced.

If you're trying to copy many small files to a file share, try parallelizing
file creation with a tool like the [Google Cloud CLI](/sdk/gcloud/reference/storage/rsync):


```
mkdir -p /mnt/nfs/many_files_rsync/
time gcloud storage rsync many_files /mnt/nfs/many_files_rsync/ --recursive
```


- 

Each file stored on the file share consumes one inode. If the file system
runs out of inodes, you won't be able to store more files on the file share
even if you haven't reached the maximum allocated capacity. However, reaching
the maximum number of inodes is rare and is only a concern if you need to
store numerous small files.

For more information, see [Inode usage](/filestore/docs/scale#inode-usage).

### Copying data between Cloud Storage and Filestore

Copying data from Cloud Storage to a Filestore instance using the
gcloud CLI is known to be slow. For detailed information on how to
improve performance, see
[Improve performance across Cloud de Confiance resources](/filestore/docs/performance#across-resources).

## What's next

- [Troubleshoot capacity issues](/filestore/docs/capacity-issues)

- [Improve performance across Cloud de Confiance resources](/filestore/docs/performance#across-resources).

- [Scale capacity](/filestore/docs/scale).