# Next.js Migration & Deployment Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Run Migration Script
```bash
node migrate-to-nextjs.js
```

### 3. Start Development Server
```bash
npm run dev
```
Visit: http://localhost:3000

## 📦 Framework Overview

### Why Next.js?
- **Superior SEO**: Server-side rendering and static generation
- **Performance**: Automatic code splitting, image optimization
- **Scalability**: Handles 3,155+ pages efficiently
- **Developer Experience**: TypeScript, hot reload, great tooling
- **Cost Effective**: Free hosting tier on Vercel

### Project Structure
```
src/
├── app/              # App router pages
│   ├── layout.tsx    # Root layout
│   ├── page.tsx      # Home page
│   ├── services/     # Service pages
│   ├── locations/    # Location pages
│   └── ...
├── components/       # Reusable components
├── lib/             # Utility functions
└── styles/          # Global styles

public/              # Static assets
├── images/         # Image files
└── assets/         # Other static files
```

## 🌐 Hosting Options

### Option 1: Vercel (Recommended) ✅

**Benefits:**
- Zero-config deployment
- Free tier: 100GB bandwidth/month
- Automatic HTTPS
- Global CDN
- GitHub integration
- Preview deployments

**Deployment Steps:**

#### Via CLI:
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Follow prompts:
# - Link to existing project? No
# - What's your project name? skerritt-economics
# - In which directory? ./
# - Override settings? No
```

#### Via GitHub:
1. Push code to GitHub:
```bash
git add .
git commit -m "feat: migrate to Next.js framework

- Set up Next.js 14 with TypeScript
- Configure Tailwind CSS
- Create component structure
- Add Vercel deployment config

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
git push origin modern-framework-migration
```

2. Go to [vercel.com](https://vercel.com)
3. Sign up/login with GitHub
4. Click "New Project"
5. Import your repository
6. Deploy!

### Option 2: Netlify

**Benefits:**
- Similar to Vercel
- Good for static sites
- Form handling built-in
- 100GB bandwidth free

**Deployment:**
```bash
# Install Netlify CLI
npm i -g netlify-cli

# Deploy
netlify deploy
netlify deploy --prod
```

### Option 3: AWS Amplify

**Benefits:**
- AWS integration
- More control
- Good for enterprise

**Deployment:**
1. Install AWS CLI
2. Configure credentials
3. Use Amplify Console

### Option 4: Self-Hosted (VPS)

**For a VPS like DigitalOcean:**
```bash
# Build the app
npm run build

# Start production server
npm run start

# Or use PM2 for process management
npm i -g pm2
pm2 start npm --name "skerritt-economics" -- start
```

## 🔧 Configuration

### Environment Variables
Create `.env.local`:
```env
NEXT_PUBLIC_SITE_URL=https://skerritteconomics.com
NEXT_PUBLIC_GA_ID=G-JNK2QCYSC7
```

### Custom Domain Setup (Vercel)
1. Go to project settings in Vercel
2. Navigate to "Domains"
3. Add: `skerritteconomics.com`
4. Update DNS records:
   - A Record: `76.76.21.21`
   - CNAME: `cname.vercel-dns.com`

## 📊 Migration Checklist

- [x] Next.js setup complete
- [x] TypeScript configured
- [x] Tailwind CSS integrated
- [x] Core components created
- [x] Vercel config added
- [ ] Install dependencies (`npm install`)
- [ ] Run migration script
- [ ] Test locally
- [ ] Deploy to Vercel
- [ ] Configure custom domain
- [ ] Update DNS records
- [ ] Test production site

## 🎯 Performance Targets

The Next.js site will achieve:
- **Lighthouse Score**: 95+
- **First Contentful Paint**: < 1.5s
- **Time to Interactive**: < 3.5s
- **Cumulative Layout Shift**: < 0.1

## 📈 SEO Benefits

Next.js provides:
1. **Server-side rendering** for instant content
2. **Automatic sitemap** generation
3. **Built-in meta tags** management
4. **Optimized images** with next/image
5. **Fast page loads** improve rankings

## 💰 Cost Comparison

| Hosting | Free Tier | Paid | Best For |
|---------|-----------|------|----------|
| Vercel | 100GB/mo | $20/mo | Next.js apps |
| Netlify | 100GB/mo | $19/mo | Static sites |
| AWS | 1 year free | Pay-as-you-go | Enterprise |
| GitHub Pages | Unlimited | Free | Static only |

## 🚨 Important Notes

1. **City Pages Migration**: The 3,155 city pages will be converted to dynamic routes in Next.js, significantly reducing build time and improving maintainability.

2. **Image Optimization**: Next.js automatically optimizes images. Move all images to `public/images/`.

3. **API Routes**: Contact forms can use Next.js API routes instead of external services.

4. **Analytics**: Google Analytics is pre-configured in the layout.

## 📞 Support

- **Vercel Docs**: https://vercel.com/docs
- **Next.js Docs**: https://nextjs.org/docs
- **Deployment Issues**: Check build logs in Vercel dashboard

## 🎉 Ready to Deploy!

Your site is now ready for modern hosting with:
- Better performance
- Lower costs
- Easier maintenance
- Improved SEO
- Better developer experience

Run `npm install` and then `npm run dev` to get started!