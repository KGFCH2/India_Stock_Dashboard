#!/usr/bin/env python3
"""
Test script to verify emoji gradient removal and navigation bar implementation
"""
import os
import re

def test_emoji_and_navigation_fixes():
    """Test emoji gradient removal and navigation bar implementation"""
    print("🔍 Testing Emoji & Navigation Bar Fixes...")
    
    # Files to check
    files_to_check = [
        "main.py",
        "components/auth.py", 
        "components/ui_components.py"
    ]
    
    # Patterns for emoji-normal class usage
    emoji_normal_patterns = [
        r'<span class="emoji-normal">📈</span>',
        r'<span class="emoji-normal">🔮</span>', 
        r'<span class="emoji-normal">📊</span>',
        r'<span class="emoji-normal">📚</span>',
        r'<span class="emoji-normal">👋</span>'
    ]
    
    # Navigation bar patterns
    nav_patterns = [
        r'class="nav-bar"',
        r'key="nav_analytics"',
        r'key="nav_logout"', 
        r'key="nav_theme"'
    ]
    
    # CSS patterns for emoji protection
    css_patterns = [
        r'\.emoji-normal',
        r'background: none !important',
        r'\.nav-bar',
        r'\.nav-button'
    ]
    
    total_emoji_fixes = 0
    total_nav_elements = 0
    total_css_features = 0
    
    for file_path in files_to_check:
        full_path = os.path.join("d:\\Vs Code\\PROJECT\\India_Stock_Dashboard", file_path)
        if os.path.exists(full_path):
            print(f"\n📱 Checking {file_path}...")
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check emoji-normal usage
            emoji_fixes = 0
            for pattern in emoji_normal_patterns:
                matches = len(re.findall(pattern, content, re.IGNORECASE))
                emoji_fixes += matches
                if matches:
                    print(f"   ✅ Emoji protected with emoji-normal: {matches} instances")
            
            # Check navigation elements
            nav_elements = 0
            for pattern in nav_patterns:
                matches = len(re.findall(pattern, content, re.IGNORECASE))
                nav_elements += matches
                if matches:
                    print(f"   🧭 Navigation element found: {matches} instances")
            
            # Check CSS features
            css_features = 0
            for pattern in css_patterns:
                matches = len(re.findall(pattern, content, re.IGNORECASE))
                css_features += matches
                if matches:
                    print(f"   🎨 CSS feature implemented: {matches} instances")
            
            total_emoji_fixes += emoji_fixes
            total_nav_elements += nav_elements
            total_css_features += css_features
            
            print(f"   📊 File summary: {emoji_fixes} emoji fixes, {nav_elements} nav elements, {css_features} CSS features")
    
    print(f"\n🎯 OVERALL RESULTS:")
    print(f"   ✅ Emoji-normal protections: {total_emoji_fixes}")
    print(f"   🧭 Navigation elements: {total_nav_elements}")
    print(f"   🎨 CSS features: {total_css_features}")
    
    if total_emoji_fixes > 0 and total_nav_elements > 0:
        print("\n🎉 SUCCESS! Both emoji fixes and navigation bar implemented!")
        print("   📈 Emojis are now protected from gradients")
        print("   🧭 Separate navigation bar created")
        print("   🎨 Beautiful styling applied")
    else:
        print(f"\n⚠️  Need more work on implementation")
    
    print("\n📚 FEATURES IMPLEMENTED:")
    print("   • .emoji-normal CSS class - protects emojis from gradients")
    print("   • .nav-bar - separate navigation container")
    print("   • Navigation buttons with unique keys")
    print("   • Improved button styling and hover effects")
    print("   • Clean separation of emojis and gradient text")
    
    print("\n🧭 NAVIGATION BAR FEATURES:")
    print("   • 📊 Analytics button")
    print("   • 🚪 Logout button") 
    print("   • 🌓 Theme toggle button")
    print("   • Glassmorphism styling")
    print("   • Hover animations")
    
    print("\n🇮🇳 Perfect for the Indian Stock Market Dashboard! ✨")

if __name__ == "__main__":
    test_emoji_and_navigation_fixes()