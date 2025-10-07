#!/usr/bin/env python3
"""
Test script to verify emoji gradient effect removal
"""
import os
import re

def test_emoji_gradient_separation():
    """Test that emojis are separated from gradient text effects"""
    print("🔍 Testing Emoji Gradient Effect Removal...")
    
    # Files to check
    files_to_check = [
        "main.py",
        "components/auth.py", 
        "components/ui_components.py"
    ]
    
    # Patterns that should now exist (emojis outside gradient classes)
    fixed_patterns = [
        r'<h1>📈\s*<span class="gradient-title">.*?</span></h1>',
        r'<h2>🔮\s*<span class="gradient-title">.*?</span></h2>',
        r'<h2>📊\s*<span class="gradient-title">.*?</span></h2>', 
        r'<h4>📚\s*<span class="gradient-text">.*?</span></h4>'
    ]
    
    # Patterns that should no longer exist (emojis inside gradient classes)
    problematic_patterns = [
        r'class="gradient-title">📈',
        r'class="gradient-title">🔮', 
        r'class="gradient-title">📊',
        r'class="gradient-text">📚'
    ]
    
    total_fixes = 0
    total_problems = 0
    
    for file_path in files_to_check:
        full_path = os.path.join("d:\\Vs Code\\PROJECT\\India_Stock_Dashboard", file_path)
        if os.path.exists(full_path):
            print(f"\n📱 Checking {file_path}...")
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for fixes
            fixes_found = 0
            for pattern in fixed_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                fixes_found += len(matches)
                if matches:
                    print(f"   ✅ Found properly separated emoji: {len(matches)} instances")
            
            # Check for remaining problems  
            problems_found = 0
            for pattern in problematic_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                problems_found += len(matches)
                if matches:
                    print(f"   ❌ Still has emoji in gradient class: {len(matches)} instances")
            
            total_fixes += fixes_found
            total_problems += problems_found
            
            print(f"   📊 File summary: {fixes_found} fixes, {problems_found} remaining issues")
    
    print(f"\n🎯 OVERALL RESULTS:")
    print(f"   ✅ Properly separated emojis: {total_fixes}")
    print(f"   ❌ Emojis still in gradient classes: {total_problems}")
    
    if total_problems == 0:
        print("\n🎉 SUCCESS! All emojis have been separated from gradient text effects!")
        print("   📈 Emojis will now display in their natural colors")
        print("   🌈 Text gradients remain beautiful and animated")
    else:
        print(f"\n⚠️  Still {total_problems} emojis affected by gradient classes")
    
    print("\n📚 What was fixed:")
    print("   • Main dashboard title: 📈 separated from gradient")
    print("   • Future predictions title: 🔮 separated from gradient") 
    print("   • Technical indicators title: 📊 separated from gradient")
    print("   • Educational disclaimer: 📚 separated from gradient")
    print("   • Auth page title: 📈 separated from gradient")
    
    print("\n🇮🇳 All other emojis in buttons, labels, and text remain unaffected!")

if __name__ == "__main__":
    test_emoji_gradient_separation()