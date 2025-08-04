#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

// Migration script to convert Jekyll content to Next.js
console.log('🚀 Starting Jekyll to Next.js migration...\n');

// Create pages directory structure
const createDirectories = () => {
  const dirs = [
    'src/app/services',
    'src/app/practice-areas',
    'src/app/locations',
    'src/app/locations/cities',
    'src/app/about',
    'src/app/contact',
    'src/app/blog',
    'src/app/resources',
    'src/app/tools',
    'src/app/case-studies',
    'public/images',
    'public/assets',
    'src/data',
    'src/lib',
    'src/types'
  ];

  dirs.forEach(dir => {
    const fullPath = path.join(__dirname, dir);
    if (!fs.existsSync(fullPath)) {
      fs.mkdirSync(fullPath, { recursive: true });
      console.log(`✅ Created directory: ${dir}`);
    }
  });
};

// Convert Jekyll markdown to Next.js component
const convertMarkdownToComponent = (filePath, outputDir) => {
  const content = fs.readFileSync(filePath, 'utf8');
  const { data, content: mdContent } = matter(content);
  
  const componentName = path.basename(filePath, '.md').replace(/-/g, '');
  const capitalizedName = componentName.charAt(0).toUpperCase() + componentName.slice(1);
  
  // Create page.tsx for the route
  const pageContent = `import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: '${data.title || capitalizedName} | Skerritt Economics',
  description: '${data.description || ''}',
}

export default function ${capitalizedName}Page() {
  return (
    <div className="container py-20">
      <h1 className="text-4xl font-bold mb-8">${data.title || capitalizedName}</h1>
      <div className="prose max-w-none">
        ${mdContent.replace(/```/g, '`')}
      </div>
    </div>
  )
}`;

  const outputPath = path.join(outputDir, 'page.tsx');
  fs.writeFileSync(outputPath, pageContent);
  console.log(`✅ Converted: ${filePath} → ${outputPath}`);
};

// Copy static assets
const copyStaticAssets = () => {
  // Copy images
  if (fs.existsSync('assets/images')) {
    const images = fs.readdirSync('assets/images');
    images.forEach(image => {
      fs.copyFileSync(
        path.join('assets/images', image),
        path.join('public/images', image)
      );
    });
    console.log(`✅ Copied ${images.length} images to public/images`);
  }

  // Copy other assets
  const staticFiles = [
    'Christopher-Skerritt-1-636x960-1.jpg',
    'sec-logo.png',
    'favicon.ico',
    'manifest.json',
    'robots.txt'
  ];

  staticFiles.forEach(file => {
    if (fs.existsSync(file)) {
      fs.copyFileSync(file, path.join('public', file));
      console.log(`✅ Copied ${file} to public/`);
    }
  });
};

// Main migration function
const migrate = async () => {
  console.log('📁 Creating directory structure...\n');
  createDirectories();

  console.log('\n📄 Converting markdown files...\n');
  
  // Convert main pages
  const mainPages = ['about.md', 'contact.md', 'resources.md'];
  mainPages.forEach(page => {
    if (fs.existsSync(page)) {
      const outputDir = path.join('src/app', path.basename(page, '.md'));
      if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
      }
      convertMarkdownToComponent(page, outputDir);
    }
  });

  console.log('\n🖼️ Copying static assets...\n');
  copyStaticAssets();

  console.log('\n✨ Migration preparation complete!');
  console.log('\n📋 Next steps:');
  console.log('1. Run: npm install');
  console.log('2. Run: npm run dev (to start development server)');
  console.log('3. Visit: http://localhost:3000');
  console.log('\n🚀 To deploy to Vercel:');
  console.log('1. Install Vercel CLI: npm i -g vercel');
  console.log('2. Run: vercel');
  console.log('3. Follow the prompts to deploy');
  console.log('\nOr push to GitHub and connect to Vercel for automatic deployments!');
};

// Run migration
migrate().catch(console.error);