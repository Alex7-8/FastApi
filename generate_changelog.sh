# generate_changelog.sh
VERSION=$(git tag | sort -V | tail -1)
DATE=$(date +"%Y-%m-%d")

echo "## [$VERSION] - $DATE" >> CHANGELOG.md
git log $(git describe --tags --abbrev=0)..HEAD --oneline >> CHANGELOG.md