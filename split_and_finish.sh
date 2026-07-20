#!/usr/bin/env bash
set -e
cd /c/Users/WIN10/STEELCHINA

# Undo the 33 MB media-128 commit so we can push it file-by-file
git reset --mixed HEAD~1

# Push each file of media-128 individually
for f in www/AEETHER/media/media-128/*; do
    name=$(basename "$f")
    git add "$f"
    git commit -m "content: media-128 ${name}"
    if ! git push origin chunked2:main; then
        echo "Retrying ${name}..."
        sleep 5
        git pull --no-edit origin main || true
        git push origin chunked2:main
    fi
done

# Push each remaining untracked media item individually
for item in www/AEETHER/media/*; do
    if git ls-files --error-unmatch "$item" >/dev/null 2>&1; then
        continue
    fi
    name=$(basename "$item")
    git add "$item"
    git commit -m "content: media ${name}"
    if ! git push origin chunked2:main; then
        echo "Retrying ${name}..."
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

echo "SPLIT AND FINISH COMPLETE"
