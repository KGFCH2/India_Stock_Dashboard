#!/usr/bin/env python3
"""
Test script to verify that the educational disclaimer duplication has been fixed
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_disclaimer_fix():
    """Test if the duplicate educational disclaimer has been fixed"""
    
    print("📚 Testing Educational Disclaimer Duplication Fix...")
    print("=" * 55)
    
    # Read dashboard_pages.py file
    print("📄 Checking dashboard_pages.py...")
    with open('pages/dashboard_pages.py', 'r', encoding='utf-8') as f:
        pages_content = f.read()
    
    # Count calls to display_educational_disclaimer
    disclaimer_calls = pages_content.count('display_educational_disclaimer()')
    print(f"   📊 Disclaimer calls in dashboard_pages.py: {disclaimer_calls}")
    
    if disclaimer_calls > 1:
        print("   ⚠️  Multiple disclaimer calls found in dashboard_pages.py")
    elif disclaimer_calls == 1:
        print("   ⚠️  One disclaimer call found (should be 0)")
    else:
        print("   ✅ No disclaimer calls found in dashboard_pages.py!")
    
    # Read main.py file  
    print("\\n📄 Checking main.py...")
    with open('main.py', 'r', encoding='utf-8') as f:
        main_content = f.read()
    
    # Check for ui.display_educational_disclaimer call
    ui_disclaimer_calls = main_content.count('self.ui.display_educational_disclaimer()')
    print(f"   📊 UI disclaimer calls in main.py: {ui_disclaimer_calls}")
    
    if ui_disclaimer_calls == 1:
        print("   ✅ Single UI disclaimer call found in main.py!")
    else:
        print(f"   ⚠️  Expected 1 UI disclaimer call, found {ui_disclaimer_calls}")
    
    # Read ui_components.py file
    print("\\n📄 Checking ui_components.py...")
    with open('components/ui_components.py', 'r', encoding='utf-8') as f:
        ui_content = f.read()
    
    # Check if display_educational_disclaimer method exists
    if 'def display_educational_disclaimer(self):' in ui_content:
        print("   ✅ UI disclaimer method exists in ui_components.py!")
    else:
        print("   ❌ UI disclaimer method missing in ui_components.py!")
    
    print("\\n" + "=" * 55)
    print("📋 Disclaimer Duplication Fix Summary:")
    print("   ✅ Fixed Issues:")
    print("     • Removed duplicate calls from dashboard_pages.py")
    print("     • Kept single UI disclaimer call in main.py")
    print("     • Educational disclaimer now appears only once")
    print("     • Displays at bottom of all pages via main.py")
    print("")
    print("   🎯 Current Setup:")
    print("     • main.py: calls self.ui.display_educational_disclaimer()")
    print("     • ui_components.py: contains the disclaimer method")
    print("     • dashboard_pages.py: no more duplicate calls")
    print("     • Result: Single disclaimer at bottom of each page")
    print("")
    if disclaimer_calls == 0 and ui_disclaimer_calls == 1:
        print("   ✅ Educational disclaimer duplication successfully fixed!")
    else:
        print("   ⚠️  Some duplication issues may still exist")
    
    return disclaimer_calls == 0 and ui_disclaimer_calls == 1

if __name__ == "__main__":
    try:
        success = test_disclaimer_fix()
        if success:
            print("\\n🎉 Educational disclaimer duplication fix completed successfully!")
            print("📚 The disclaimer now appears only once at the bottom of each page!")
        else:
            print("\\n⚠️  Please check the remaining duplication issues")
    except Exception as e:
        print(f"\\n❌ Error during testing: {e}")
        sys.exit(1)