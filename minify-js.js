const fs = require('fs');

// Simple JavaScript minifier
function minifyJS(code) {
    // Remove comments
    code = code.replace(/\/\*[\s\S]*?\*\//g, ''); // Remove block comments
    code = code.replace(/\/\/.*$/gm, ''); // Remove line comments
    
    // Remove unnecessary whitespace while preserving necessary spaces
    code = code.replace(/\s+/g, ' '); // Replace multiple spaces with single space
    code = code.replace(/\s*([{}();,:])\s*/g, '$1'); // Remove spaces around punctuation
    code = code.replace(/;\s*}/g, '}'); // Remove semicolon before closing brace
    
    // Remove trailing semicolons before closing braces
    code = code.replace(/;}/g, '}');
    
    // Trim the result
    code = code.trim();
    
    return code;
}

// Read the main.js file
const inputFile = './js/main.js';
const outputFile = './js/main.min.js';

try {
    const content = fs.readFileSync(inputFile, 'utf8');
    const minified = minifyJS(content);
    
    // Add a comment at the top
    const finalContent = `/* Minified ${new Date().toISOString()} */\n${minified}`;
    
    fs.writeFileSync(outputFile, finalContent);
    
    const originalSize = Buffer.byteLength(content, 'utf8');
    const minifiedSize = Buffer.byteLength(finalContent, 'utf8');
    const savings = originalSize - minifiedSize;
    const percentage = ((savings / originalSize) * 100).toFixed(1);
    
    console.log(`Original size: ${(originalSize / 1024).toFixed(1)} KB`);
    console.log(`Minified size: ${(minifiedSize / 1024).toFixed(1)} KB`);
    console.log(`Savings: ${(savings / 1024).toFixed(1)} KB (${percentage}%)`);
} catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
}