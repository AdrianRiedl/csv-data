#!/usr/bin/env bash
set -euo pipefail
SF=${1:-1}
SCRIPTDIR="$PWD"

if [[ "$OSTYPE" == "darwin"* ]]; then
  MACHINE="MACOS"
  CORES=$(sysctl -n hw.ncpu)
  GNUSED="gsed"
else
  MACHINE="LINUX"
  CORES=$(nproc)
  GNUSED="sed"
fi

echo "Generating TPC-H with scale factor $SF"

mkdir -p "scripts/tpch/data/sf$SF"
cd "scripts/tpch/data/"

echo '66e975965f803e4de665890b84f05b62d443569e9ae246e0106ff73f0c176b9c  tpch-kit.zip' | sha256sum --check --status 2>/dev/null || curl -OL https://db.in.tum.de/~fent/dbgen/tpch/tpch-kit.zip
echo '66e975965f803e4de665890b84f05b62d443569e9ae246e0106ff73f0c176b9c  tpch-kit.zip' | sha256sum --check --status
unzip -q -u tpch-kit.zip

# Reuse existing datasets
if [ -z "$(ls -A "sf$SF")" ]; then
  (
    cd tpch-kit-852ad0a5ee31ebefeed884cea4188781dd9613a3/dbgen
    rm -rf ./*.tbl
    # fix include
    $GNUSED -i 's/<malloc.h>/<stdlib.h>/' bm_utils.c
    MACHINE="$MACHINE" make -sj "$CORES" dbgen 2>/dev/null
    ./dbgen -f -s "$SF"
    for table in ./*.tbl; do
      $GNUSED 's/|$//' "$table" >"../../sf$SF/$table"
    done
  )
fi

cd "sf$SF"
