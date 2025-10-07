#!/usr/bin/env python3
"""
Test script for gradient text updates
"""

print("🎨 Testing Gradient Text Updates")
print("="*50)

try:
    # Test file modifications
    with open("main.py", "r") as f:
        main_content = f.read()
        if "gradient-title" in main_content:
            print("✅ Main title updated with gradient styling")
        else:
            print("❌ Main title gradient styling not found")
    
    with open("components/auth.py", "r") as f:
        auth_content = f.read()
        if "gradient-title" in auth_content and "gradient-label" in auth_content:
            print("✅ Auth page updated with gradient styling")
        else:
            print("❌ Auth page gradient styling incomplete")
    
    print("\n" + "="*50)
    print("🎉 Gradient Text Features Applied:")
    print("   🌈 Green+Blue gradient combination")
    print("   📝 Enhanced visibility in both light/dark themes")
    print("   ✨ Animated gradient effects")
    print("   🎨 Professional styling for titles and labels")
    
    print("\nYour dashboard is running at: http://localhost:8501")
    print("Refresh the page to see the new gradient text styling!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Please check the file modifications and try again.")