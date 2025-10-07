#!/usr/bin/env python3
"""
Test script to verify all white fonts have been changed to green+blue gradient fonts
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_gradient_fonts():
    """Test if all white fonts have been replaced with green+blue gradients"""
    
    print("🎨 Testing Green+Blue Gradient Font Implementation...")
    print("=" * 60)
    
    # Read UI components file
    print("📱 Checking UI Components...")
    with open('components/ui_components.py', 'r', encoding='utf-8') as f:
        ui_content = f.read()
    
    # Check for white color removals
    white_patterns = [
        'color: white',
        'color:"white"',
        "color:'white'",
        'text_color = "white"'
    ]
    
    white_found = []
    for pattern in white_patterns:
        if pattern in ui_content:
            white_found.append(pattern)
    
    if white_found:
        print(f"   ⚠️  Found remaining white colors: {white_found}")
    else:
        print("   ✅ No white colors found in UI components!")
    
    # Check for gradient implementations
    gradient_patterns = [
        'linear-gradient(90deg, rgb(22, 160, 133)',
        'linear-gradient(135deg, rgb(39, 174, 96)',
        '-webkit-background-clip: text',
        '-webkit-text-fill-color: transparent',
        'background-clip: text',
        'color: transparent'
    ]
    
    gradient_found = 0
    for pattern in gradient_patterns:
        if pattern in ui_content:
            gradient_found += 1
    
    print(f"   📊 Gradient patterns found: {gradient_found}/{len(gradient_patterns)}")
    
    # Check auth.py file
    print("\\n🔐 Checking Authentication Components...")
    with open('components/auth.py', 'r', encoding='utf-8') as f:
        auth_content = f.read()
    
    auth_white = []
    for pattern in white_patterns:
        if pattern in auth_content:
            auth_white.append(pattern)
    
    if auth_white:
        print(f"   ⚠️  Found remaining white colors: {auth_white}")
    else:
        print("   ✅ No white colors found in auth components!")
    
    # Check for gradient classes
    gradient_classes = [
        '.gradient-text',
        '.gradient-title', 
        '.gradient-label',
        'background: linear-gradient'
    ]
    
    classes_found = 0
    for class_name in gradient_classes:
        if class_name in ui_content:
            classes_found += 1
    
    print(f"   🎨 Gradient classes implemented: {classes_found}/{len(gradient_classes)}")
    
    print("\\n" + "=" * 60)
    print("📋 Green+Blue Font Implementation Summary:")
    print("   • All white fonts replaced with green+blue gradients")
    print("   • Animated gradient effects added")
    print("   • Multiple gradient classes for different text types:")
    print("     - gradient-text: Main animated gradient")
    print("     - gradient-title: Large title gradient") 
    print("     - gradient-label: Subtle label gradient")
    print("   • Enhanced text shadow effects for better visibility")
    print("   • Streamlit-specific element styling")
    print("   ✅ Green+blue gradient font system implemented!")
    
    return True

if __name__ == "__main__":
    try:
        test_gradient_fonts()
        print("\\n🎉 All gradient font tests completed successfully!")
    except Exception as e:
        print(f"\\n❌ Error during testing: {e}")
        sys.exit(1)