#!/bin/bash

# Script to push repository to GitHub
# Usage: bash push_to_github.sh

echo "=================================================="
echo "  Pushing Abacus-VitD-DM2 to GitHub"
echo "=================================================="
echo ""

cd /home/ubuntu/github_repos/Abacus-VitD-DM2

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Not in the correct directory"
    exit 1
fi

# Check git status
echo "📋 Current git status:"
git status
echo ""

# Check if authenticated
echo "🔐 Checking GitHub authentication..."
if gh auth status &>/dev/null; then
    echo "✅ GitHub CLI authenticated!"
else
    echo "⚠️  Not authenticated with GitHub CLI"
    echo "   Please authenticate first using one of these methods:"
    echo "   1. gh auth login --web"
    echo "   2. Use a Personal Access Token"
    echo ""
    echo "   See PUSH_TO_GITHUB.md for detailed instructions"
    exit 1
fi

# Push to GitHub
echo ""
echo "🚀 Pushing to GitHub..."
git push -u origin master

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "  ✅ Successfully pushed to GitHub!"
    echo "=================================================="
    echo ""
    echo "🌐 View your repository at:"
    echo "   https://github.com/ej777spirit/Abacus-VitD-DM2"
    echo ""
    echo "📊 Repository contents:"
    echo "   • Literature review"
    echo "   • Omics datasets inventory"
    echo "   • Research templates"
    echo "   • Complete aims paper"
    echo "   • Computational analysis pipeline"
    echo "   • Thesis presentation"
    echo "   • 27 files total"
    echo ""
else
    echo ""
    echo "=================================================="
    echo "  ❌ Push failed"
    echo "=================================================="
    echo ""
    echo "📖 See PUSH_TO_GITHUB.md for troubleshooting help"
    exit 1
fi
