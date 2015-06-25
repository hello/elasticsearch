#!/bin/bash

clear

echo "Start installing plugins"

# To be run in root es directory
bin/plugin -install royrusso/elasticsearch-HQ
bin/plugin -install elasticsearch/elasticsearch-cloud-aws/2.6.0
bin/plugin -install mobz/elasticsearch-head


echo "Finish installing plugins"









