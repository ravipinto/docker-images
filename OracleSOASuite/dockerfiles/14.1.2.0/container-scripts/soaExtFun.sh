#!/bin/bash
#
# Copyright (c) 2025, Oracle and/or its affiliates.
#
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl
#
# Author: jagmohan.s.bisht@oracle.com
#

# Script to handle ext jars for SOA (safe when empty)

SRC_DIR="$DOMAIN_HOME/soa/oracle.soa.ext_11.1.1"
DST_DIR="$ORACLE_HOME/soa/soa/modules/oracle.soa.ext_11.1.1"

if [ ! -d "$SRC_DIR" ]; then
  echo "$SRC_DIR does not exist... creating it now..."
  mkdir -p "$SRC_DIR"
else
  echo "$SRC_DIR exists... copying files if any"
  echo "source = $SRC_DIR/"
  echo "dest   = $DST_DIR"
  mkdir -p "$DST_DIR"
  # Copy contents (including dotfiles) only if there are entries
  if find "$SRC_DIR" -mindepth 1 -maxdepth 1 -print -quit | grep -q .; then
    cp -r "$SRC_DIR"/. "$DST_DIR"/
  else
    echo "No files to copy in $SRC_DIR"
  fi
fi
