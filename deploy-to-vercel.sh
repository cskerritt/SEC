#!/bin/bash

echo "🚀 Deploying to Vercel..."

# Deploy to production with automatic yes to all prompts
npx vercel --prod --yes

echo "✅ Deployment complete!"
echo ""
echo "Your site should now be live!"
echo "Check the URL above to view your site."
echo ""
echo "To add custom domain:"
echo "1. Go to your Vercel dashboard"
echo "2. Select your project"
echo "3. Go to Settings → Domains"
echo "4. Add skerritteconomics.com"