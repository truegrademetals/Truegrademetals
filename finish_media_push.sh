#!/usr/bin/env bash
set -e
cd /c/Users/WIN10/STEELCHINA

# Push the already-committed media-128 commit first
git push origin chunked2:main

# Commit and push each remaining media item individually
for item in www/AEETHER/media/*; do
    # Skip items already tracked (media-128 / media-129)
    if git ls-files --error-unmatch "$item" >/dev/null 2>&1; then
        continue
    fi
    name=$(basename "$item")
    git add "$item"
    git commit -m "content: media ${name}"
    if ! git push origin chunked2:main; then
        echo "Retrying push for ${name}..."
        sleep 5
        git pull --no-edit origin main || true
        git push origin chunked2:main
    fi
done

# Add helper scripts at the end
if [ -n "$(git status --porcelain *.sh)" ]; then
    git add *.sh
    git commit -m "chore: helper scripts"
    git push origin chunked2:main
fi

echo "FINISH MEDIA PUSH COMPLETE"
