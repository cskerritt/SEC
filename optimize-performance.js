#!/usr/bin/env node

/**
 * Website Performance Optimization Script
 * Optimizes CSS, JavaScript, images, and analyzes unused code
 */

const fs = require('fs');
const path = require('path');

// Configuration
const config = {
    cssFiles: [
        'css/styles.css',
        'css/contact.css',
        'css/about.css',
        'css/practice-areas.css',
        'css/services.css',
        'css/locations.css',
        'css/case-studies.css'
    ],
    jsFiles: [
        'js/main.js',
        'js/contact.js',
        'js/case-studies.js'
    ],
    htmlFiles: [
        'index.html',
        'contact.html',
        'about.html',
        'practice-areas.html',
        'services.html'
    ]
};

// Utility functions
function minifyCSS(css) {
    return css
        .replace(/\/\*[\s\S]*?\*\//g, '') // Remove comments
        .replace(/\s+/g, ' ') // Replace multiple spaces
        .replace(/;\s*}/g, '}') // Remove semicolon before closing brace
        .replace(/\s*{\s*/g, '{') // Remove spaces around braces
        .replace(/\s*}\s*/g, '}')
        .replace(/\s*:\s*/g, ':') // Remove spaces around colons
        .replace(/\s*;\s*/g, ';') // Remove spaces around semicolons
        .replace(/\s*,\s*/g, ',') // Remove spaces around commas
        .replace(/^\s+|\s+$/g, '') // Trim
        .replace(/\n/g, '') // Remove newlines
        .replace(/\t/g, ''); // Remove tabs
}

function minifyJS(js) {
    return js
        .replace(/\/\*[\s\S]*?\*\//g, '') // Remove block comments
        .replace(/\/\/.*$/gm, '') // Remove line comments
        .replace(/\s+/g, ' ') // Replace multiple spaces
        .replace(/;\s*}/g, '}') // Remove semicolon before closing brace
        .replace(/\s*{\s*/g, '{') // Remove spaces around braces
        .replace(/\s*}\s*/g, '}')
        .replace(/\s*\(\s*/g, '(') // Remove spaces around parentheses
        .replace(/\s*\)\s*/g, ')')
        .replace(/\s*;\s*/g, ';') // Remove spaces around semicolons
        .replace(/\s*,\s*/g, ',') // Remove spaces around commas
        .replace(/\s*=\s*/g, '=') // Remove spaces around equals
        .replace(/^\s+|\s+$/g, '') // Trim
        .replace(/\n/g, '') // Remove newlines
        .replace(/\t/g, ''); // Remove tabs
}

function analyzeUnusedCSS(cssContent, htmlContent) {
    const selectors = cssContent.match(/[^{}]+(?=\s*{)/g) || [];
    const unusedSelectors = [];
    
    selectors.forEach(selector => {
        const cleanSelector = selector.trim().split(',')[0].trim();
        
        // Skip media queries, keyframes, and pseudo-selectors
        if (cleanSelector.startsWith('@') || 
            cleanSelector.includes('keyframes') ||
            cleanSelector.includes(':hover') ||
            cleanSelector.includes(':focus') ||
            cleanSelector.includes(':active') ||
            cleanSelector.includes('::')) {
            return;
        }
        
        // Extract class names and IDs
        const classMatch = cleanSelector.match(/\.([\w-]+)/);
        const idMatch = cleanSelector.match(/#([\w-]+)/);
        const tagMatch = cleanSelector.match(/^(\w+)/);
        
        let found = false;
        
        if (classMatch && htmlContent.includes(`class="${classMatch[1]}"`)) {
            found = true;
        } else if (idMatch && htmlContent.includes(`id="${idMatch[1]}"`)) {
            found = true;
        } else if (tagMatch && htmlContent.includes(`<${tagMatch[1]}`)) {
            found = true;
        }
        
        if (!found && cleanSelector.length > 0) {
            unusedSelectors.push(cleanSelector);
        }
    });
    
    return unusedSelectors;
}

function getBundledCSS() {
    let bundled = '';
    config.cssFiles.forEach(file => {
        if (fs.existsSync(file)) {
            const content = fs.readFileSync(file, 'utf8');
            bundled += `/* ${file} */\n${content}\n\n`;
        }
    });
    return bundled;
}

function getBundledJS() {
    let bundled = '';
    config.jsFiles.forEach(file => {
        if (fs.existsSync(file)) {
            const content = fs.readFileSync(file, 'utf8');
            bundled += `/* ${file} */\n${content}\n\n`;
        }
    });
    return bundled;
}

// Main optimization function
function optimize() {
    console.log('🚀 Starting website performance optimization...\n');
    
    // 1. Create bundled and minified CSS
    console.log('📦 Bundling and minifying CSS files...');
    const bundledCSS = getBundledCSS();
    const minifiedBundleCSS = minifyCSS(bundledCSS);
    fs.writeFileSync('css/bundle.min.css', minifiedBundleCSS);
    console.log(`✓ Created css/bundle.min.css (${minifiedBundleCSS.length} bytes)`);
    
    // 2. Create bundled and minified JS
    console.log('\n📦 Bundling and minifying JavaScript files...');
    const bundledJS = getBundledJS();
    const minifiedBundleJS = minifyJS(bundledJS);
    fs.writeFileSync('js/bundle.min.js', minifiedBundleJS);
    console.log(`✓ Created js/bundle.min.js (${minifiedBundleJS.length} bytes)`);
    
    // 3. Analyze unused CSS
    console.log('\n🔍 Analyzing unused CSS...');
    let allHTML = '';
    config.htmlFiles.forEach(file => {
        if (fs.existsSync(file)) {
            allHTML += fs.readFileSync(file, 'utf8');
        }
    });
    
    const unusedSelectors = analyzeUnusedCSS(bundledCSS, allHTML);
    console.log(`Found ${unusedSelectors.length} potentially unused CSS selectors`);
    
    if (unusedSelectors.length > 0) {
        fs.writeFileSync('unused-css-report.txt', 
            'Potentially Unused CSS Selectors:\n' + 
            unusedSelectors.map(s => `- ${s}`).join('\n')
        );
        console.log('✓ Saved unused CSS report to unused-css-report.txt');
    }
    
    // 4. Generate performance report
    const originalSizes = {
        css: config.cssFiles.reduce((total, file) => {
            if (fs.existsSync(file)) {
                return total + fs.statSync(file).size;
            }
            return total;
        }, 0),
        js: config.jsFiles.reduce((total, file) => {
            if (fs.existsSync(file)) {
                return total + fs.statSync(file).size;
            }
            return total;
        }, 0)
    };
    
    const optimizedSizes = {
        css: fs.statSync('css/bundle.min.css').size,
        js: fs.statSync('js/bundle.min.js').size
    };
    
    const savings = {
        css: Math.round((1 - optimizedSizes.css / originalSizes.css) * 100),
        js: Math.round((1 - optimizedSizes.js / originalSizes.js) * 100)
    };
    
    console.log('\n📊 Performance Optimization Report:');
    console.log(`CSS: ${originalSizes.css} bytes → ${optimizedSizes.css} bytes (${savings.css}% reduction)`);
    console.log(`JS: ${originalSizes.js} bytes → ${optimizedSizes.js} bytes (${savings.js}% reduction)`);
    console.log(`Total savings: ${(originalSizes.css + originalSizes.js) - (optimizedSizes.css + optimizedSizes.js)} bytes`);
    
    console.log('\n✅ Optimization complete!');
    console.log('\n📝 Next steps:');
    console.log('1. Update HTML files to use bundle.min.css and bundle.min.js');
    console.log('2. Review unused-css-report.txt and remove unnecessary styles');
    console.log('3. Test website functionality with optimized files');
    console.log('4. Monitor performance with browser dev tools');
}

// Run optimization
if (require.main === module) {
    optimize();
}

module.exports = { optimize, minifyCSS, minifyJS, analyzeUnusedCSS };