#!/bin/bash

mkdir -p results

declare -a profiles=("low" "high")
declare -a delays=(10 200)
declare -a traces=("50Mbps" "1Mbps")
declare -a algos=("bbr" "cubic" "copa")

for i in "${!profiles[@]}"; do
  profile="${profiles[$i]}"
  delay="${delays[$i]}"
  trace="${traces[$i]}"

  for ((j=0; j<${#algos[@]}; j++)); do
    for ((k=j+1; k<${#algos[@]}; k++)); do
      a1="${algos[$j]}"
      a2="${algos[$k]}"
      dir="results/${a1}_vs_${a2}_${profile}"
      echo "Running $a1 vs $a2 on $profile profile..."
      python3 src/experiments/test_schemes.py
        --schemes "$a1 $a2" \
        --uplink-trace traces/${trace}.trace \
        --downlink-trace traces/${trace}.trace \
        --prepend-mm-cmds "mm-delay $delay" \
        --data-dir "$dir" \
        --runtime 60
    done
  done
done
