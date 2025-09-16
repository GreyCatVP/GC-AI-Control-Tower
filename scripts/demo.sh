#!/bin/bash
set -e
echo "🎬 Recording demo..."
peek -d 30 -o docs/demo.gif
echo "✅ GIF saved to docs/demo.gif"
