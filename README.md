### Elasticsearch
Version: 1.6.0

### Requirements

1. JDK: 6.0 (or above) but JDK 8 (at least u20 or higher) or JDK 7 (u55) is best recommended
2. Hardware: at least 8Gb memory, cpu does not matter much
3. Set number of open file to 64000
4. Heap size to be less than half of memory but not more than 64 Gb
5. Disable memory swap (can use es settings)

### Init steps 

1. Download & unpack (debian): https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.6.0.deb
2. Replace config/elasticsearch.yml by [elasticsearch.yml](https://github.com/hello/elasticsearch/blob/master/elasticsearch.yml) and config/logging.yml by [logging.yml](https://github.com/hello/elasticsearch/blob/master/logging.yml) from this repo.
3. Install plugins with the install plugin -b 
4. Run ./elasticsearch (with optional heapsize settings: -Xmx2G -Xms2G)
5. Go to http://<domain>:9200/_plugin/HQ to see cluster status


### Backup

1. Register a repository with a PUT to  /_snapshot/<REPO_NAME> with body as in [repo_s3_register.json](https://github.com/hello/elasticsearch/blob/master/repo_s3_register.json)
2. Make a POST to /_snapshot/<REPO_NAME>/<SNAPSHOT_NAME> with optional body as in [backup_settings.json](https://github.com/hello/elasticsearch/blob/master/backup_settings.json). Add ?wait_for_complete=true if you want to wait & see backup summary

### Restore

1. If on another machine/cluster register a repository with a PUT to `/_snapshot/<REPO_NAME>` with body as in [repo_s3_register.json](https://github.com/hello/elasticsearch/blob/master/repo_s3_register.json)
2. View available snapshots by GET to `/_snapshot/<REPO_NAME>/_all`
3. Make a POST to `/_snapshot/<REPO_NAME>/<SNAPSHOT_NAME>/_restore` with optional body as in [restore_settings.json](https://github.com/hello/elasticsearch/blob/master/restore_settings.json). Add ?wait_for_complete=true if you want to wait & see restore summary
4. Note that searching will not be available on under-recovery shards.

### Search
1. Basic queries can be done via GET to `/<INDEX_NAME>/<DOC_TYPE>/_search?q=<FIELD_NAME>:<SEARCH_KEYWORD>`
2. Complex queries must be done by POST to `/<INDEX_NAME>/<DOC_TYPE>/_search` with a body carrying specifications
