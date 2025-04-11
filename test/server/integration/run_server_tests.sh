#!/bin/bash

echo "Running integration tests..."

ROOT_DIR="$(dirname "$0")"
IN_DIR="$ROOT_DIR/in"
OUT_DIR="$ROOT_DIR/out"
TMP_DIR=$(mktemp)
pass=true

strip_timestamps() {
    # Strip ISO timestamps like 2025-04-11T06:53:54.930996 and
    # human-readable timestamps like 2025-04-11 06:53:54.930996
    sed -E \
        -e "s/[0-9]{4}-[0-9]{2}-[0-9]{2}[ T][0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}//g"
}

for infile in "$IN_DIR"/*.in; do
    testname=$(basename "$infile" .in)
    expected="$OUT_DIR/$testname.out"

    echo "▶️  Running $testname..."

    # 👇 Adjust this based on your project structure
    python3 -m server < "$infile" > "$TMP_DIR" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "❌ $testname failed to run (server error)"
        pass=false
        continue
    fi

    if ! diff -u <(strip_timestamps < "$expected") <(strip_timestamps < "$TMP_DIR") > /tmp/diff_output; then
        echo "❌ $testname failed"
        echo "----- Diff -----"
        cat /tmp/diff_output
        pass=false
    else
        echo "✅ $testname passed"
    fi
done

rm -f "$TMP_DIR" /tmp/diff_output

if $pass; then
    echo "✅ All integration tests passed."
    exit 0
else
    echo "❌ Some integration tests failed."
    exit 1
fi