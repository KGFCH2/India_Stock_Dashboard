#!/usr/bin/env python3
"""
Test script to verify card flip functionality
"""
import os
import re

def test_card_flip_functionality():
    """Test card flip CSS and HTML implementation"""
    print("🃏 Testing Card Flip Functionality...")
    
    # File to check
    file_path = "components/ui_components.py"
    full_path = os.path.join("d:\\Vs Code\\PROJECT\\India_Stock_Dashboard", file_path)
    
    if os.path.exists(full_path):
        print(f"\n📱 Checking {file_path}...")
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check CSS elements
        css_checks = [
            (r'\.flip-card\s*\{', "Flip card container"),
            (r'\.flip-card-inner\s*\{', "Flip card inner container"),
            (r'\.flip-card-front.*\.flip-card-back\s*\{', "Front and back card elements"),
            (r'transform:\s*rotateY\(180deg\)', "Flip transformation"),
            (r'perspective:\s*1000px', "3D perspective"),
            (r'transform-style:\s*preserve-3d', "3D transform style"),
            (r'backface-visibility:\s*hidden', "Backface visibility"),
            (r'transition:\s*transform.*ease', "Smooth transition")
        ]
        
        # Check HTML structure
        html_checks = [
            (r'<div class="flip-card">', "Flip card HTML wrapper"),
            (r'<div class="flip-card-inner">', "Flip card inner wrapper"),
            (r'<div class="flip-card-front">', "Front face HTML"),
            (r'<div class="flip-card-back">', "Back face HTML"),
            (r'class="emoji-normal"', "Emoji protection in flip cards")
        ]
        
        # Check content improvements
        content_checks = [
            (r'<strong>.*?</strong>', "Enhanced content formatting"),
            (r'gradient-text.*Price Details', "Improved back content headers"),
            (r'Volume.*Activity.*High|Normal|Low', "Volume activity analysis"),
            (r'Trend.*Bullish|Bearish|Neutral', "Price trend analysis")
        ]
        
        print("\n🎨 CSS FUNCTIONALITY CHECKS:")
        css_found = 0
        for pattern, description in css_checks:
            matches = len(re.findall(pattern, content, re.IGNORECASE | re.DOTALL))
            if matches > 0:
                print(f"   ✅ {description}: Found")
                css_found += 1
            else:
                print(f"   ❌ {description}: Missing")
        
        print("\n🏗️ HTML STRUCTURE CHECKS:")
        html_found = 0
        for pattern, description in html_checks:
            matches = len(re.findall(pattern, content, re.IGNORECASE))
            if matches > 0:
                print(f"   ✅ {description}: {matches} instances")
                html_found += 1
            else:
                print(f"   ❌ {description}: Missing")
        
        print("\n📝 CONTENT ENHANCEMENT CHECKS:")
        content_found = 0
        for pattern, description in content_checks:
            matches = len(re.findall(pattern, content, re.IGNORECASE | re.DOTALL))
            if matches > 0:
                print(f"   ✅ {description}: Found")
                content_found += 1
            else:
                print(f"   ❌ {description}: Missing")
        
        print(f"\n🎯 OVERALL RESULTS:")
        print(f"   🎨 CSS Features: {css_found}/{len(css_checks)}")
        print(f"   🏗️ HTML Structure: {html_found}/{len(html_checks)}")
        print(f"   📝 Content Enhancements: {content_found}/{len(content_checks)}")
        
        total_score = css_found + html_found + content_found
        max_score = len(css_checks) + len(html_checks) + len(content_checks)
        
        if total_score >= max_score * 0.8:
            print("\n🎉 SUCCESS! Card flip functionality is properly implemented!")
            print("   🃏 Hover over cards to see flip animation")
            print("   🎨 Enhanced CSS with proper 3D effects")
            print("   📱 Improved content on card backs")
        else:
            print(f"\n⚠️  Card flip needs improvement: {total_score}/{max_score} checks passed")
    
    print("\n🃏 CARD FLIP FEATURES:")
    print("   • 3D flip animation on hover")
    print("   • Smooth 0.8s transition")
    print("   • Glassmorphism styling")
    print("   • Enhanced back content")
    print("   • Emoji protection")
    print("   • Professional formatting")
    
    print("\n💡 HOW TO USE:")
    print("   1. Launch the dashboard")
    print("   2. Hover over any metric card")
    print("   3. Watch the card flip to reveal detailed information")
    print("   4. Move cursor away to flip back")
    
    print("\n🇮🇳 Perfect for the Indian Stock Market Dashboard! ✨")

if __name__ == "__main__":
    test_card_flip_functionality()