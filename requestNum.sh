#!/bin/sh
for i in `cat /var/log/nginx/access.log | awk '{print $1}' | uniq`; do  printf $i' => ' && cat /var/log/nginx/access.log | grep $i | wc -l; done | sort -r -k3 -u
